import re

# --- Update all-tours.html ---
with open('all-tours.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add to dropdown menu (after Tiger Tour)
dropdown_item = '                        <a href="haridwar-rishikesh-tour.html" class="dropdown-item">Haridwar & Rishikesh Spiritual Tour</a>\n'
html = html.replace(
    '<a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>\n',
    '<a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>\n' + dropdown_item
)

# Add to the tour grid (after Tiger Tour card)
tour_card = """
                <!-- Card: Haridwar & Rishikesh -->
                <div class="journey-card reveal reveal-delay-3">
                    <div class="card-img-container">
                        <img src="assets/haridwar_rishikesh_hero.png" alt="Haridwar Rishikesh Tour" class="journey-img">
                        <div class="card-badge">Spiritual & Heritage</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">3 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Delhi – Haridwar – Rishikesh</span>
                        </div>
                        <h3 class="card-title">Haridwar & Rishikesh Spiritual Tour</h3>
                        <p class="card-text">Experience divine Ganga Aarti, sacred temples, and spiritual vibes in a 3 Days 2 Nights journey.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Ganga Aarti at Har Ki Pauri</li>
                            <li>Ram Jhula & Laxman Jhula</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="haridwar-rishikesh-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

# Find the Tiger Tour card and insert after it
# This might match multiple times if there are duplicates, so we just replace the first closing tag of the Tiger Tour card
tiger_card_end = '<!-- Card: Tiger Tour With Jaipur -->'
# Actually, since Tiger Tour is the last card before the closing tag, let's insert it before the closing section/div.
# A simpler way is to find a unique point. In the output from grep, Tiger Tour With Jaipur is the last card.
# Let's use regex to find the end of the Tiger Tour card
pattern = re.compile(r'(<h3 class="card-title">Tiger Tour With Jaipur</h3>.*?</div>\s*</div>\s*</div>)', re.DOTALL)
html = pattern.sub(r'\1' + '\n' + tour_card, html)

with open('all-tours.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated all-tours.html")

# --- Update sitemap.xml ---
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_url = """
    <url>
        <loc>https://grandholidaytours.com/haridwar-rishikesh-tour.html</loc>
        <lastmod>2026-06-11</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>"""

if 'haridwar-rishikesh-tour.html' not in sitemap:
    sitemap = sitemap.replace('</urlset>', new_url + '\n</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Added to sitemap.xml")
