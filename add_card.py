import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
files = ['index.html', 'all-tours.html']

new_card = '''
              <!-- Card: 8 Days Golden Triangle with Varanasi -->
              <div class="journey-card reveal reveal-delay-2">
                  <div class="card-img-container">
                      <img src="assets/varanasi_ghats.png" alt="Varanasi Ghats" class="journey-img" onerror="this.src='assets/golden_triangle_hero.png';">
                      <div class="card-badge">Spiritual Journey</div>
                  </div>
                  <div class="card-content">
                      <h3 class="card-title">8 Days Golden Triangle & Varanasi</h3>
                      <p class="card-desc">Experience the majestic Golden Triangle combined with the spiritual heart of India. Includes private chauffeured drives and domestic flights.</p>
                      <ul class="card-features">
                          <li><span class="feature-icon">⏱</span> 8 Days / 7 Nights</li>
                          <li><span class="feature-icon">📍</span> Delhi, Agra, Jaipur, Varanasi</li>
                          <li><span class="feature-icon">✈️</span> Includes Flights</li>
                      </ul>
                      <div class="card-footer">
                          <span class="price">₹22,050 <span class="pp">/ person</span></span>
                          <a href="8-days-golden-triangle-varanasi-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                      </div>
                  </div>
              </div>'''

for fname in files:
    filepath = os.path.join(repo_path, fname)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert inside journey grid if not already added
    if '8 Days Golden Triangle & Varanasi' not in content:
        content = content.replace('<div class="journey-grid">', '<div class="journey-grid">' + new_card)
        
    # Also add it to the dropdown menu!
    dropdown_target = '<a class="dropdown-item" href="8-days-golden-triangle-tour.html">Golden Triangle Tour</a>'
    if dropdown_target in content and '8 Days Golden Triangle & Varanasi' not in content:
        content = content.replace(dropdown_target, dropdown_target + '\n                          <a class="dropdown-item" href="8-days-golden-triangle-varanasi-tour.html">8 Days Golden Triangle & Varanasi</a>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Added cards successfully.')
