import re
import shutil
import os
import glob

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\hawa_mahal_hero_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\hawa_mahal_hero.png")

# Update golden-triangle.html
with open('golden-triangle.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero image
html = html.replace('assets/golden_triangle_hero.png', 'assets/hawa_mahal_hero.png')
html = html.replace('alt="Taj Mahal Golden Triangle Banner"', 'alt="Hawa Mahal Golden Triangle Banner"')

with open('golden-triangle.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace image for the Golden Triangle Tour card
# Last time we changed it to assets/golden_triangle_hero.png in index.html as well for the Golden Triangle Tour card.
cards = re.split(r'(<!-- Card \d+.*?-->)', index_html)
new_index_html = ""
for chunk in cards:
    if 'href="golden-triangle.html"' in chunk and not 'dropdown-item' in chunk:
        # This is the card for Golden Triangle Tour
        chunk = chunk.replace('assets/golden_triangle_hero.png', 'assets/hawa_mahal_hero.png')
    new_index_html += chunk

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)
