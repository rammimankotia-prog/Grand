import glob
import os
import re

# 1. Update footers in all HTML files
html_files = glob.glob("*.html")

for file_path in html_files:
    # skip blog.html if it exists
    if file_path == 'blog.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<a href="blog.html">Blog</a>' in content:
        continue # already added
        
    # Inject Blog link after Contact in the Explore column
    contact_link1 = '<a href="contact.html">Contact</a>'
    contact_link2 = '<a href="contact.html">Contact Us</a>'
    
    new_content = content
    if contact_link1 in new_content:
        # Check if it's in the footer by looking for a nearby known footer string like "Explore"
        # Using a regex replacement to ensure we don't mess up the header contact link if there is one.
        # However, usually the header contact link is different or has class="nav-link".
        # Let's replace only the one without class="nav-link".
        new_content = re.sub(r'(<a href="contact\.html">Contact</a>)(?!.*nav-link)', r'\1\n<a href="blog.html">Blog</a>', new_content)
    elif contact_link2 in new_content:
        new_content = re.sub(r'(<a href="contact\.html">Contact Us</a>)(?!.*nav-link)', r'\1\n<a href="blog.html">Blog</a>', new_content)
    else:
        print(f"Warning: Could not find Contact link in {file_path}")
        
    # Simple replacement if regex above didn't work and it's definitely the footer
    # Footer has '<div class="footer-links-col">\n<h4>Explore</h4>'
    explore_section = '<div class="footer-links-col">\n<h4>Explore</h4>'
    if explore_section in new_content and '<a href="blog.html">Blog</a>' not in new_content:
        # replace delhi travel guide
        dtg = '<a href="delhi-travel-guide.html">Delhi Travel Guide</a>'
        if dtg in new_content:
            new_content = new_content.replace(dtg, '<a href="blog.html">Blog</a>\n' + dtg)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {file_path}")

# 2. Create blog.html by reading about.html, extracting head, header, footer, and inserting blog content
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract from start to </header>
header_match = re.search(r'^(.*?</header>)', about_content, re.DOTALL)
header_part = header_match.group(1) if header_match else ''

# Extract footer to end
footer_match = re.search(r'(<footer class="luxury-footer">.*)$', about_content, re.DOTALL)
footer_part = footer_match.group(1) if footer_match else ''

# Create the blog body
blog_body = """
<!-- Blog Hero Section -->
<section class="about-hero" style="min-height: 40vh; display: flex; align-items: center; justify-content: center;">
<div class="about-hero-content" style="text-align: center;">
<span class="about-badge">OUR JOURNAL</span>
<h1 class="about-main-title">Travel Stories &amp; Insights</h1>
<p class="about-hero-subtitle">Discover the latest news, guides, and inspiration for your next luxury journey in India.</p>
</div>
</section>

<!-- Blog Grid Section -->
<section class="blog-section" style="padding: 5rem 0; background-color: #fdfaf6;">
<div class="container">
    <div class="section-header text-center">
        <h2 class="section-title">Latest Articles</h2>
        <div class="title-divider"></div>
    </div>
    
    <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
        
        <!-- Blog Post 1 Placeholder -->
        <div class="blog-card glass-card" style="border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <img src="assets/hero_banner.png" alt="Blog Post" style="width: 100%; height: 200px; object-fit: cover;">
            <div class="blog-content" style="padding: 1.5rem;">
                <span class="blog-date" style="font-size: 0.85rem; color: #A67C31; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">August 27, 2026</span>
                <h3 style="margin: 0.5rem 0 1rem; font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #18130E;">The Golden Triangle: A First-Timer's Guide</h3>
                <p style="color: #6B5F54; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Everything you need to know before embarking on India's most iconic travel route through Delhi, Agra, and Jaipur.</p>
                <a href="#" class="btn btn-outline btn-sm" style="display: inline-block;">Read More</a>
            </div>
        </div>

        <!-- Blog Post 2 Placeholder -->
        <div class="blog-card glass-card" style="border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <img src="assets/taj_mahal.png" alt="Blog Post" style="width: 100%; height: 200px; object-fit: cover;">
            <div class="blog-content" style="padding: 1.5rem;">
                <span class="blog-date" style="font-size: 0.85rem; color: #A67C31; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">August 15, 2026</span>
                <h3 style="margin: 0.5rem 0 1rem; font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #18130E;">5 Best Places to See the Sunrise at the Taj Mahal</h3>
                <p style="color: #6B5F54; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Discover the secret viewpoints and exact timings to catch the most magical sunrise over this world wonder.</p>
                <a href="#" class="btn btn-outline btn-sm" style="display: inline-block;">Read More</a>
            </div>
        </div>

        <!-- Blog Post 3 Placeholder -->
        <div class="blog-card glass-card" style="border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <img src="assets/ranthambore_tiger_hero.png" alt="Blog Post" style="width: 100%; height: 200px; object-fit: cover;">
            <div class="blog-content" style="padding: 1.5rem;">
                <span class="blog-date" style="font-size: 0.85rem; color: #A67C31; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">July 22, 2026</span>
                <h3 style="margin: 0.5rem 0 1rem; font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #18130E;">Wildlife Safaris: Ranthambore Travel Tips</h3>
                <p style="color: #6B5F54; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">A comprehensive guide to spotting Bengal tigers and preparing for your luxury jungle safari experience.</p>
                <a href="#" class="btn btn-outline btn-sm" style="display: inline-block;">Read More</a>
            </div>
        </div>

    </div>
</div>
</section>
"""

# Update header_part Title and Meta
header_part = re.sub(r'<title>.*?</title>', '<title>Travel Journal & Blog | Grand Holiday Tours</title>', header_part)
header_part = re.sub(r'<meta name="description" content=".*?"/>', '<meta name="description" content="Read the latest travel stories, tips, and news from Grand Holidays. Discover luxury travel inspiration for your next trip to India."/>', header_part)
# Also change nav-link active class
header_part = header_part.replace('<a href="about.html" class="nav-link active">About Us</a>', '<a href="about.html" class="nav-link">About Us</a>')

# Combine parts
blog_full = header_part + "\n" + blog_body + "\n" + footer_part

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_full)

print("Created blog.html successfully.")
