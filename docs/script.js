/**
 * CyberBulletin - Frontend Logic
 */

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    fetchPosts();
});

/**
 * Fetch and display the list of posts (intel feed)
 */
async function fetchPosts() {
    const container = document.getElementById('feed-container');
    
    // Ensure marked is configured for safety and styling
    marked.setOptions({
        gfm: true,
        breaks: true,
        headerIds: true,
    });

    try {
        const response = await fetch('posts.json');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const posts = await response.json();

        if (!posts || posts.length === 0) {
            container.innerHTML = `
                <div class="error-message">
                    <i class="fa-solid fa-folder-open text-muted"></i>
                    <h3>No Intelligence Found</h3>
                    <p>The system hasn't generated any intel reports yet. Run the backend fetcher.</p>
                </div>`;
            container.style.display = 'block';
            return;
        }

        container.innerHTML = ''; // Clear loading skeletons

        posts.forEach(post => {
            // Determine a category if one is provided
            let categoryHTML = '';
            if (post.category) {
                const catStr = Array.isArray(post.category) ? post.category[0] : post.category.split(',')[0].replace(/[\[\]]/g, '');
                categoryHTML = `<span class="card-category">${catStr}</span>`;
            }

            // Estimate read time or file size randomly for UI aesthetic
            const readMins = Math.max(2, Math.floor(Math.random() * 8));

            const postCard = document.createElement('div');
            postCard.className = 'post-card';
            postCard.onclick = () => loadPost(post.filename);

            postCard.innerHTML = `
                <div class="card-meta">
                    <span class="date"><i class="fa-regular fa-calendar" style="margin-right: 6px;"></i>${post.date}</span>
                    ${categoryHTML}
                </div>
                <h3>${post.title || "Untitled Intelligence Report"}</h3>
                
                <div class="card-footer">
                    <span>Read Report</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </div>
            `;
            
            container.appendChild(postCard);
        });

    } catch (error) {
        console.error(error);
        container.style.display = 'block'; // Reset grid for error message
        
        if (window.location.protocol === 'file:') {
            container.innerHTML = `
                <div class="error-message">
                    <i class="fa-solid fa-shield-virus"></i>
                    <h3>CORS Blocked (Local Access)</h3>
                    <p>Browsers block reading local JSON files for security.</p>
                    <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; margin-top: 10px; font-family: monospace;">
                        python -m http.server
                    </div>
                </div>`;
        } else {
            container.innerHTML = `
                <div class="error-message">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                    <h3>Data Retrieval Failed</h3>
                    <p>${error.message}</p>
                    <p class="text-muted" style="font-size: 0.85em">Verify that <code>posts.json</code> exists and is accessible.</p>
                </div>`;
        }
    }
}

/**
 * Load and display a specific markdown post
 * @param {string} filename 
 */
async function loadPost(filename) {
    document.getElementById('feed-view').style.display = 'none';
    const postView = document.getElementById('post-view');
    const contentDiv = document.getElementById('post-content');
    
    postView.style.display = 'block';
    
    // Show loading state
    contentDiv.innerHTML = `<div class="loading-post"><i class="fa-solid fa-circle-notch fa-spin"></i></div>`;
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    try {
        // BUG FIX: Was `../posts/${filename}`, properly requested as `posts/${filename}`
        // Since script.js runs on index.html, which is IN the docs/ folder.
        const response = await fetch(`posts/${filename}`);
        
        if (!response.ok) {
            throw new Error(`Failed to load post (${response.status})`);
        }

        let markdown = await response.text();

        // Strip YAML frontmatter
        markdown = markdown.replace(/^---[\s\S]*?---/, '');

        // Parse markdown to HTML
        const rawHtml = marked.parse(markdown);
        
        // Sanitize generated HTML using DOMPurify
        const safeHtml = DOMPurify.sanitize(rawHtml);
        
        // Render content
        // Adding a slight delay for smooth transition feel
        setTimeout(() => {
            contentDiv.innerHTML = safeHtml;
        }, 150);

    } catch (error) {
        console.error(error);
        contentDiv.innerHTML = `
            <div class="error-message" style="margin-top: 2rem;">
                <i class="fa-solid fa-file-circle-xmark"></i>
                <h2>Error Loading Report</h2>
                <p>Could not retrieve the intelligence file. It may have been moved or deleted.</p>
                <code style="display:block; margin-top:1em; padding:10px; background:rgba(0,0,0,0.2)">${error.message}</code>
            </div>`;
    }
}

/**
 * Return to the feed view
 */
function showFeed() {
    document.getElementById('post-view').style.display = 'none';
    document.getElementById('feed-view').style.display = 'block';
    
    // Smooth scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
