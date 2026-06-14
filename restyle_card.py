import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
index_html = os.path.join(repo_path, 'index.html')
all_tours_html = os.path.join(repo_path, 'all-tours.html')
index_css = os.path.join(repo_path, 'index.css')

# 1. Update CSS
css_to_add = '''
/* Modern Card Style based on reference */
.modern-card {
    background: #fff;
    border-radius: 0;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease;
    border: 1px solid #f0f0f0;
}
.modern-card:hover {
    transform: translateY(-5px);
}
.modern-card-img-wrapper {
    position: relative;
    width: 100%;
    height: 280px;
    overflow: hidden;
}
.modern-card-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.modern-card-badge {
    position: absolute;
    top: 1.2rem;
    left: 1.2rem;
    background: #b89047;
    color: #fff;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.modern-card-content {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}
.modern-card-meta {
    display: flex;
    align-items: center;
    font-size: 0.8rem;
    font-family: 'Outfit', sans-serif;
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
    text-transform: uppercase;
}
.modern-card-meta .meta-days {
    color: #b89047;
    font-weight: 700;
}
.modern-card-meta .meta-sep {
    color: #ccc;
    margin: 0 0.5rem;
}
.modern-card-meta .meta-locs {
    color: #999;
    font-weight: 500;
}
.modern-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #111;
    margin: 0 0 1rem 0;
    font-weight: 700;
}
.modern-card-desc {
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
    margin: 0 0 1.5rem 0;
}
.modern-card-divider {
    border: 0;
    border-top: 1px solid #eaeaea;
    margin: 0 0 1.5rem 0;
}
.modern-card-highlights {
    list-style: none;
    padding: 0;
    margin: 0;
}
.modern-card-highlights li {
    font-size: 0.95rem;
    color: #333;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
}
.modern-card-highlights li::before {
    content: '—';
    color: #b89047;
    font-weight: bold;
}
'''

with open(index_css, 'r', encoding='utf-8') as f:
    current_css = f.read()

if 'modern-card' not in current_css:
    with open(index_css, 'a', encoding='utf-8') as f:
        f.write('\n' + css_to_add)

# 2. Update HTML
new_card_html = '''<!-- Card: 8 Days Golden Triangle with Varanasi -->
              <div class="modern-card reveal reveal-delay-2">
                  <div class="modern-card-img-wrapper">
                      <a href="8-days-golden-triangle-varanasi-tour.html">
                          <img src="assets/varanasi_ghats.png" alt="Varanasi Ghats" onerror="this.src='assets/golden_triangle_hero.png';">
                      </a>
                      <div class="modern-card-badge">SPIRITUAL & HERITAGE</div>
                  </div>
                  <div class="modern-card-content">
                      <div class="modern-card-meta">
                          <span class="meta-days">8 DAYS</span>
                          <span class="meta-sep">|</span>
                          <span class="meta-locs">DELHI • AGRA • JAIPUR • VARANASI</span>
                      </div>
                      <a href="8-days-golden-triangle-varanasi-tour.html" style="text-decoration: none;"><h3 class="modern-card-title">8-Day Tour With Varanasi</h3></a>
                      <p class="modern-card-desc">Experience the majestic Golden Triangle combined with the spiritual heart of India in Varanasi. Includes private chauffeured drives and domestic flights.</p>
                      <hr class="modern-card-divider">
                      <ul class="modern-card-highlights">
                          <li>Premium A/C Transport & Flights</li>
                          <li>Sunrise Boat Ride & Ganga Aarti</li>
                      </ul>
                  </div>
              </div>'''

# Regex to find the old Varanasi card
pattern = re.compile(r'<!-- Card: 8 Days Golden Triangle with Varanasi -->.*?<a href="8-days-golden-triangle-varanasi-tour\.html" class="btn btn-outline btn-sm">View Tour</a>\s*</div>\s*</div>\s*</div>', re.DOTALL)

for html_file in [index_html, all_tours_html]:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if pattern.search(content):
        content = pattern.sub(new_card_html, content)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully replaced Varanasi card in {os.path.basename(html_file)}")
    else:
        print(f"Could not find the Varanasi card in {os.path.basename(html_file)}")
