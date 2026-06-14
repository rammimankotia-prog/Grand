import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
index_html = os.path.join(repo_path, 'index.html')
all_tours_html = os.path.join(repo_path, 'all-tours.html')

new_card_html = '''<!-- Card 1b: 8 Days Golden Triangle with Varanasi -->
              <div class="journey-card reveal reveal-delay-2">
                  <div class="card-img-container">
                      <img src="assets/varanasi_ghats.png" alt="Varanasi Ghats" class="journey-img" onerror="this.src='assets/golden_triangle_hero.png';">
                      <div class="card-badge">Spiritual &amp; Heritage</div>
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
                          <li>Premium A/C Transport &amp; Flights</li>
                          <li>Sunrise Boat Ride in Varanasi</li>
                          <li>Ganga Aarti Ceremony</li>
                      </ul>
                      <div class="card-footer">
                          <span class="price">₹22,050 <span class="pp">/ person</span></span>
                          <a href="8-days-golden-triangle-varanasi-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                      </div>
                  </div>
              </div>
              '''

for html_file in [index_html, all_tours_html]:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert right before Card 1b
    target = '<!-- Card 1b: 5 Days Golden Triangle Tour -->'
    if target in content and '8 Days Golden Triangle with Varanasi' not in content:
        content = content.replace(target, new_card_html + target)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added card to {os.path.basename(html_file)}")
    else:
        # If Card 1b is not found, maybe Card 2
        target2 = '<!-- Card 2: Himalayan -->'
        if target2 in content and '8 Days Golden Triangle with Varanasi' not in content:
            content = content.replace(target2, new_card_html + target2)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added card to {os.path.basename(html_file)} (fallback)")
        else:
            print(f"Could not find injection point in {os.path.basename(html_file)}")
