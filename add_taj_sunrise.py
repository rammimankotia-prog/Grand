import os, re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# ── 1. Add to mega menu: inject before Same Day Agra Tour ──────────────
old_agra = (
    '<a class="dropdown-item" href="agra-day-tour.html">'
    '<span class="item-icon">\U0001f54d</span>'
    '<span class="item-text">'
    '<span class="item-name">Same Day Agra Tour</span>'
    '<span class="item-sub">Taj Mahal \u00b7 Agra Fort</span>'
    '</span>'
    '</a>'
)
new_sunrise_item = (
    '<a class="dropdown-item" href="taj-mahal-sunrise-tour.html">'
    '<span class="item-icon">\U0001f305</span>'
    '<span class="item-text">'
    '<span class="item-name">Taj Mahal Sunrise Tour</span>'
    '<span class="item-sub">Express Entry \u00b7 Skip the Line</span>'
    '</span>'
    '</a>'
)

menu_updated = 0
for fname in os.listdir(repo_path):
    if not fname.endswith('.html') or fname == 'taj-mahal-sunrise-tour.html':
        continue
    fpath = os.path.join(repo_path, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_agra in content and 'taj-mahal-sunrise-tour.html' not in content:
        content = content.replace(old_agra, new_sunrise_item + '\n                                    ' + old_agra, 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        menu_updated += 1

print(f'Updated mega menu in {menu_updated} files')

# ── 2. Add homepage card ─────────────────────────────────────────────────
card = (
    '<!-- Card: Taj Mahal Sunrise Tour -->\n'
    '              <div class="journey-card reveal reveal-delay-1">\n'
    '                  <div class="card-img-container">\n'
    '                      <img src="assets/taj_mahal_sunrise.png" alt="Taj Mahal Express Entry Sunrise Tour" class="journey-img">\n'
    '                      <div class="card-badge">Iconic Experience</div>\n'
    '                  </div>\n'
    '                  <div class="card-content">\n'
    '                      <div class="card-meta">\n'
    '                          <span class="duration">Half Day \u00b7 2.5 Hours</span>\n'
    '                          <span class="divider">|</span>\n'
    '                          <span class="location">Agra \u00b7 Taj Mahal</span>\n'
    '                      </div>\n'
    '                      <h3 class="card-title">Taj Mahal Sunrise Tour</h3>\n'
    '                      <p class="card-text">See the Taj Mahal at sunrise with express skip-the-line entry and an expert local guide. Private hotel pickup and drop-off included.</p>\n'
    '                      <ul class="card-highlights">\n'
    '                          <li>Express Entry \u2014 Skip the Queue</li>\n'
    '                          <li>Golden Sunrise Light &amp; Small Crowds</li>\n'
    '                          <li>Expert Guide &amp; Private Transfer</li>\n'
    '                      </ul>\n'
    '                      <div class="card-footer">\n'
    '                          <span class="price">On Request</span>\n'
    '                          <a href="taj-mahal-sunrise-tour.html" class="btn btn-outline btn-sm">View Tour</a>\n'
    '                      </div>\n'
    '                  </div>\n'
    '              </div>\n'
    '              \n'
)

target = '<!-- Card: Ranthambore Tiger Safari -->'

for fname in ['index.html', 'all-tours.html']:
    fpath = os.path.join(repo_path, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    marker = '<!-- Card: Taj Mahal Sunrise Tour -->'
    if marker not in html and target in html:
        html = html.replace(target, card + target, 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Card added to {fname}')
    else:
        print(f'Skipped: {fname}')

print('Done!')
