import os
import sys

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# Update price in JS
js_file = os.path.join(repo_path, 'ranthambore-tiger-safari.js')
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('price: "On Request"', 'price: "\u20b914,000 per person"')
js = js.replace("price: 'On Request'", "price: '\u20b914,000 per person'")

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)
print('Price updated in JS')

card = (
    '<!-- Card: Ranthambore Tiger Safari -->\n'
    '              <div class="journey-card reveal reveal-delay-1">\n'
    '                  <div class="card-img-container">\n'
    '                      <img src="assets/ranthambore_tiger_hero.png" alt="Ranthambore Tiger Safari" class="journey-img">\n'
    '                      <div class="card-badge">Wildlife Adventure</div>\n'
    '                  </div>\n'
    '                  <div class="card-content">\n'
    '                      <div class="card-meta">\n'
    '                          <span class="duration">3 Days / 2 Nights</span>\n'
    '                          <span class="divider">|</span>\n'
    '                          <span class="location">Delhi to Ranthambore</span>\n'
    '                      </div>\n'
    '                      <h3 class="card-title">Ranthambore Tiger Safari</h3>\n'
    '                      <p class="card-text">Two thrilling jeep safaris into the heart of Ranthambore National Park with an expert naturalist guide. Private A/C transport from Delhi included.</p>\n'
    '                      <ul class="card-highlights">\n'
    '                          <li>2 Jeep Safaris with Expert Guide</li>\n'
    '                          <li>Bengal Tiger, Leopard &amp; Sloth Bear</li>\n'
    '                          <li>Private A/C Car from Delhi</li>\n'
    '                      </ul>\n'
    '                      <div class="card-footer">\n'
    '                          <span class="price">\u20b914,000 <span class="pp">/ person <span style="font-size:0.75em;opacity:0.7;">(min. 2 pax)</span></span></span>\n'
    '                          <a href="ranthambore-tiger-safari.html" class="btn btn-outline btn-sm">View Tour</a>\n'
    '                      </div>\n'
    '                  </div>\n'
    '              </div>\n'
    '              '
)

target = '<!-- Card 1: Golden Triangle -->'

for fname in ['index.html', 'all-tours.html']:
    fpath = os.path.join(repo_path, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'Ranthambore Tiger Safari' not in html and target in html:
        html = html.replace(target, card + target)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Card added to ' + fname)
    else:
        print('Skipped (already exists or target not found): ' + fname)

print('Done!')
