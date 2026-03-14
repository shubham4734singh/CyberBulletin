import feedparser
import os
import hashlib
import time
import re
import requests
from groq import Groq
from datetime import datetime
import json
import yaml

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

RSS_SOURCES = [
    "https://thehackernews.com/rss",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.darkreading.com/rss.xml" # Note: darkreading rss might need checking if the URL is precise
]

def get_content_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

def extract_image_url(entry):
    # Try media_content (common in RSS)
    if hasattr(entry, 'media_content') and entry.media_content:
        return entry.media_content[0]['url']
    # Try links for image types
    if hasattr(entry, 'links'):
        for link in entry.links:
            if link.get('type', '').startswith('image/') or link.get('href', '').endswith(('.jpg', '.png', '.jpeg')):
                return link.get('href')
    # Try parsing description for img tags
    content = entry.get('description', '') or entry.get('summary', '')
    match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    return None

def download_image(url, save_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception:
        return False
    return False

def generate_bulletin(entry, image_path=""):
    # Sanitize title for YAML frontmatter to avoid errors with quotes
    sanitized_title = entry.title.replace('"', '\\"')

    prompt = f"""
    Act as a Senior Cybersecurity Architect. Analyze the article summary below and generate a technical blog post in Markdown format.

    **Article Information:**
    - Title: {entry.title}
    - Link: {entry.link}
    - Summary from RSS: {entry.summary}

    **Instructions for your output:**
    1.  Create YAML frontmatter.
    2.  The `title` key must be: "{sanitized_title}"
    3.  The `date` key must be today's date: {datetime.now().strftime('%Y-%m-%d')}
    4.  The `category` key should be a YAML list classifying the article into one or more of the following: `Malware`, `Vulnerabilities`, `Data Breach`, `Threat Intelligence`, `Legal`, `Industry News`. Example: `category: [Threat Intelligence, Malware]`
    5.  The `thumbnail` key must be: "{image_path}"
    6.  The `source_link` key must be: "{entry.link}"
    7.  After the frontmatter, create three Markdown sections: `## ⚡ Quick Summary`, `## 🛠 Technical Analysis`, and `## 🛡 Mitigation & Impact`.
    8.  Fill in these sections by expanding on the provided summary, providing insights from the perspective of a cybersecurity expert.

    Begin your output directly with the `---` of the frontmatter. Do not include any other text or explanation before or after the markdown content.
    """
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a Senior Cybersecurity Architect creating technical blog posts. You follow instructions precisely and only output the requested Markdown content, starting with the YAML frontmatter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-70b-8192",
    )
    
    return response.choices[0].message.content

def generate_posts_json():
    POSTS_DIR = "docs/posts"
    posts = []
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), "r", encoding="utf-8") as f:
                content = f.read()
                # Extract frontmatter
                try:
                    _, frontmatter_str, _ = content.split("---", 2)
                    frontmatter = yaml.safe_load(frontmatter_str)
                    posts.append({
                        "title": frontmatter.get("title", "No Title"),
                        "date": str(frontmatter.get("date", "No Date")),
                        "category": frontmatter.get("category", "Uncategorized"),
                        "thumbnail": frontmatter.get("thumbnail", ""),
                        "source_link": frontmatter.get("source_link", ""),
                        "filename": filename
                    })
                except Exception as e:
                    print(f"Error processing frontmatter for {filename}: {e}")
    
    # Sort posts by date, newest first
    posts.sort(key=lambda x: x["date"], reverse=True)

    if not os.path.exists("docs"):
        os.makedirs("docs")

    with open("docs/posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)

def main():
    if not os.path.exists("docs/posts"): os.makedirs("docs/posts")
    if not os.path.exists("docs/assets/images"): os.makedirs("docs/assets/images")
    
    # Load history to save money/tokens
    history_file = "processed.log"
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            processed_hashes = set(f.read().splitlines())
    else:
        processed_hashes = set()

    new_hashes = []
    success_count = 0
    error_count = 0

    for url in RSS_SOURCES:
        print(f"Fetching from {url}...")
        feed = feedparser.parse(url)
        
        for entry in feed.entries[:5]: # Process top 5 per source
            article_hash = get_content_hash(entry.link)
            
            if article_hash not in processed_hashes:
                print(f"New Intel Found: {entry.title}")
                
                slug = slugify(entry.title)
                image_path_for_md = ""
                
                # Attempt to find and download image
                img_url = extract_image_url(entry)
                if img_url:
                    ext = os.path.splitext(img_url.split('?')[0])[1]
                    if not ext or len(ext) > 5: ext = ".jpg"
                    img_filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}{ext}"
                    save_path = os.path.join("docs/assets/images", img_filename)
                    if download_image(img_url, save_path):
                        image_path_for_md = f"assets/images/{img_filename}" # Relative path for website

                try:
                    markdown_content = generate_bulletin(entry, image_path_for_md)
                    md_filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}.md"
                    full_md_path = os.path.join("docs/posts", md_filename)
                    
                    with open(full_md_path, "w", encoding="utf-8") as f:
                        f.write(markdown_content)
                    
                    new_hashes.append(article_hash)
                    success_count += 1
                    
                    # Sleep to respect Free Tier API Limits (15 RPM)
                    print("Sleeping 5 seconds to respect rate limits...")
                    time.sleep(5) 
                except Exception as e:
                    print(f"Error processing {entry.title}: {e}")
                    error_count += 1

    # Update history only if we have new hashes
    if new_hashes:
        with open(history_file, "a") as f:
            for h in new_hashes:
                f.write(h + "\n")
    
    # Generate the posts.json file
    generate_posts_json()
    abs_path = os.path.abspath("docs/posts.json")
    print(f"✅ Process completed. Feed generated at: {abs_path}")

    if success_count == 0 and error_count > 0:
        print(f"\nCRITICAL: Failed to process any of the {error_count} new articles. Please check your GEMINI_API_KEY and quota.")
        exit(1)

if __name__ == "__main__":
    main()
