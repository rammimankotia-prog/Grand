import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
varanasi_html = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')
index_html = os.path.join(repo_path, 'index.html')
all_tours_html = os.path.join(repo_path, 'all-tours.html')

# --- FIX 1 & 2: Update Varanasi HTML ---
with open(varanasi_html, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Route Overview Title
content = content.replace(
    '<h2 class="gt-map-title">8 Days Golden Triangle Route</h2>', 
    '<h2 class="gt-map-title">8-Day Golden Triangle & Varanasi Route</h2>'
)
content = content.replace(
    '<p class="gt-map-subtitle">Three iconic cities. One legendary journey across heritage, royalty and wonder.</p>',
    '<p class="gt-map-subtitle">Four iconic cities. One legendary journey across heritage, royalty and spirituality.</p>'
)

# Add Varanasi City Card (No 04)
# Find the end of Jaipur card
jaipur_end = '''<div class="city-card-tags"><span>Amber Fort</span><span>Hawa Mahal</span><span>City Palace</span></div>
                    </div>'''
varanasi_card = '''
                    <div class="gt-city-card">
                        <div class="city-card-num">04</div>
                        <div class="city-card-icon">🛕</div>
                        <h3 class="city-card-name">Varanasi</h3>
                        <p class="city-card-desc">The spiritual heart of India. Witness the sacred Ganga Aarti, sunrise boat rides, and ancient temples along the river.</p>
                        <div class="city-card-tags"><span>Ganges River</span><span>Sarnath</span><span>Kashi Vishwanath</span></div>
                    </div>'''

if '04</div>' not in content:
    content = content.replace(jaipur_end, jaipur_end + varanasi_card)

with open(varanasi_html, 'w', encoding='utf-8') as f:
    f.write(content)

# --- FIX 3: Update Cards in index.html & all-tours.html ---

new_card_html = '''<!-- Card: 8 Days Golden Triangle with Varanasi -->
              <div class="journey-card reveal reveal-delay-2">
                  <div class="card-img-container">
                      <img src="assets/varanasi_ghats.png" alt="Varanasi Ghats" class="journey-img" onerror="this.src='assets/golden_triangle_hero.png';">
                      <div class="card-badge">Spiritual Journey</div>
                  </div>
                  <div class="card-content">
                      <div class="card-meta">
                          <span class="duration">8 Days / 7 Nights</span>
                          <span class="divider">|</span>
                          <span class="location">Delhi • Agra • Jaipur • Varanasi</span>
                      </div>
                      <h3 class="card-title">8-Day Golden Triangle with Varanasi</h3>
                      <p class="card-text">Experience the majestic Golden Triangle combined with the spiritual heart of India. Includes private chauffeured drives and domestic flights.</p>
                      <ul class="card-highlights">
                          <li>Premium A/C Transport & Flights</li>
                          <li>Sunrise Boat Ride in Varanasi</li>
                          <li>Ganga Aarti Ceremony</li>
                      </ul>
                      <div class="card-footer">
                          <span class="price">₹22,050 <span class="pp">/ person</span></span>
                          <a href="8-days-golden-triangle-varanasi-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                      </div>
                  </div>
              </div>'''

# Regex to find the old Varanasi card in index and all-tours
pattern = re.compile(r'<!-- Card: 8 Days Golden Triangle with Varanasi -->.*?<a href="8-days-golden-triangle-varanasi-tour\.html" class="btn btn-outline btn-sm">View Tour</a>\s*</div>\s*</div>\s*</div>', re.DOTALL)

for html_file in [index_html, all_tours_html]:
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    if pattern.search(html_content):
        html_content = pattern.sub(new_card_html, html_content)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Replaced card in {os.path.basename(html_file)}")
    else:
        print(f"Could not find card in {os.path.basename(html_file)}")

print("Done with all 3 fixes.")
