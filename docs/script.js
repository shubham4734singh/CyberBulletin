async function fetchPosts() {
    const container = document.getElementById('feed-container');
    try {
        const response = await fetch('posts.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const posts = await response.json();

        if (!posts || posts.length === 0) {
            container.innerHTML = "<p>No intel reports found yet.</p>";
            return;
        }

        container.innerHTML = ''; // Clear loading text

        posts.forEach(post => {
            const postCard = document.createElement('div');
            postCard.className = 'post-card';

            postCard.innerHTML = `
                <h3><a onclick="loadPost('${post.filename}')">
                    ${post.title || "View Intel Report"}
                </a></h3>
                <p class="summary">Generated on: ${post.date}</p>
            `;
            container.appendChild(postCard);
        });
    } catch (error) {
        console.error(error);
        container.innerHTML = "<p>Error loading feed. Make sure you have run the python script to generate the posts.json file.</p>";
    }
}

async function loadPost(filename) {
    document.getElementById('feed-container').style.display = 'none';
    document.getElementById('post-view').style.display = 'block';
    const contentDiv = document.getElementById('post-content');

    contentDiv.innerHTML = "Loading post content...";
    contentDiv.style.display = 'block';

    try {
        const response = await fetch(`../posts/${filename}`);
        if (!response.ok) throw new Error("Failed to load post");

        let markdown = await response.text();

        // Strip YAML frontmatter from markdown before displaying
        markdown = markdown.replace(/^---[\s\S]*?---/, '');

        contentDiv.innerHTML = marked.parse(markdown);
    } catch (error) {
        console.error(error);
        contentDiv.innerHTML = "<p>Error loading post content.</p>";
    }
}

function showFeed() {
    document.getElementById('post-view').style.display = 'none';
    document.getElementById('post-content').style.display = 'none';
    document.getElementById('feed-container').style.display = 'block';
}

// Initialize fetching on page load
fetchPosts();
