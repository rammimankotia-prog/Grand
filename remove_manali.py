import re

with open('tiger-tour-jaipur.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to remove the hanging Manali card
manali_pattern = r'<div class="gt-city-card">\s*<div class="city-card-num">03</div>\s*<div class="city-card-icon">&#9978;</div>\s*<h3 class="city-card-name">Manali</h3>\s*<p class="city-card-desc">.*?</p>\s*<div class="city-card-tags">.*?</div>\s*</div>'

html = re.sub(manali_pattern, '', html, flags=re.DOTALL)

with open('tiger-tour-jaipur.html', 'w', encoding='utf-8') as f:
    f.write(html)
