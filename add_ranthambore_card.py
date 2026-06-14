import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# ── 1. Update price in ranthambore-tiger-safari.js ──────────────────────
js_file = os.path.join(repo_path, 'ranthambore-tiger-safari.js')
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('price: "On Request"', 'price: "₹14,000 per person"')
js = js.replace("price: 'On Request'", "price: '₹14,000 per person'")

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)
print("✅ Updated price in JS")

# ── 2. New Ranthambore card HTML ─────────────────────────────────────────
ranthambore_card = """<!-- Card: Ranthambore Tiger Safari -->
              <div class="journey-card reveal reveal-delay-1">
                  <div class="card-img-container">
                      <img src="assets/ranthambore_tiger_hero.png" alt="Ranthambore Tiger Safari" class="journey-img">
                      <div class="card-badge">Wildlife Adventure</div>
                  </div>
                  <div class="card-content">
                      <div class="card-meta">
                          <span class="duration">3 Days · 2 Nights</span>
                          <span class="divider">|</span>
                          <span class="location">Delhi · Ranthambore</span>
                      </div>
                      <h3 class="card-title">Ranthambore Tiger Safari</h3>
                      <p class="card-text">Two thrilling jeep safaris into the heart of Ranthambore National Park with an expert naturalist guide. Private A/C transport from Delhi included.</p>
                      <ul class="card-highlights">
                          <li>2 Jeep Safaris — Expert Guide</li>
                          <li>Bengal Tiger · Leopard · Sloth Bear</li>
                          <li>Private A/C Car from Delhi</li>
                      </ul>
                      <div class="card-footer">
                          <span class="price">₹14,000 <span class="pp">/ person <small style="font-size:0.7em;opacity:0.75;">(min. 2 pax)</small></span></span>
                          <a href="ranthambore-tiger-safari.html" class="btn btn-outline btn-sm">View Tour</a>
                      </div>
                  </div>
              </div>
              """

# ── 3. Inject card into index.html right before Card 1: Golden Triangle ──
index_file = os.path.join(repo_path, 'index.html')
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<!-- Card 1: Golden Triangle -->'
if 'Ranthambore Tiger Safari' not in html and target in html:
    html = html.replace(target, ranthambore_card + target)
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Added Ranthambore card to index.html")
else:
    print("ℹ️  Card already in index.html or target not found")

# ── 4. Also inject into all-tours.html ──────────────────────────────────
all_tours_file = os.path.join(repo_path, 'all-tours.html')
with open(all_tours_file, 'r', encoding='utf-8') as f:
    html2 = f.read()

if 'Ranthambore Tiger Safari' not in html2 and target in html2:
    html2 = html2.replace(target, ranthambore_card + target)
    with open(all_tours_file, 'w', encoding='utf-8') as f:
        f.write(html2)
    print("✅ Added Ranthambore card to all-tours.html")
else:
    print("ℹ️  Card already in all-tours.html or target not found")

print("\nAll done!")
