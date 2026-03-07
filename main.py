import feedparser
import os
import hashlib
import google.generativeai as genai
from datetime import datetime

# --- CONFIGURATION ---
# Get your key from https://aistudio.google.com/
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

RSS_SOURCES = [
    "https://thehackernews.com/rss",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.darkreading.com/rss.xml" # Note: darkreading rss might need checking if the URL is precise
]

def get_content_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def generate_bulletin(entry):
    prompt = f"""
    Act as a Senior Cybersecurity Architect. Transform this into a technical blog post.
    Title: {entry.title}
    Link: {entry.link}
    Description: {entry.description}
    
    Use the Markdown format:
    ---
    title: "{entry.title}"
    date: {datetime.now().strftime('%Y-%m-%d')}
    category: "[Malware/Vulnerabilities/Data Breach/Threat Intelligence]"
    source_link: "{entry.link}"
    ---
    ## ⚡ Quick Summary
    ## 🛠 Technical Analysis
    ## 🛡 Mitigation & Impact
    """
    response = model.generate_content(prompt)
    return response.text

def main():
    if not os.path.exists("posts"): os.makedirs("posts")
    
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
                try:
                    markdown_content = generate_bulletin(entry)
                    filename = f"posts/{datetime.now().strftime('%Y%m%d')}-{article_hash[:8]}.md"
                    
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(markdown_content)
                    
                    new_hashes.append(article_hash)
                    success_count += 1
                except Exception as e:
                    print(f"Error processing {entry.title}: {e}")
                    error_count += 1

    # Update history only if we have new hashes
    if new_hashes:
        with open(history_file, "a") as f:
            for h in new_hashes:
                f.write(h + "\n")

    if success_count == 0 and error_count > 0:
        print(f"\nCRITICAL: Failed to process any of the {error_count} new articles. Please check your GEMINI_API_KEY and quota.")
        exit(1)

if __name__ == "__main__":
    main()
