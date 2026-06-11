import re
import shutil
import os
import glob

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\imperial_rajasthan_hero_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\imperial_rajasthan_hero.png")

# Update imperial-rajasthan.html
with open('imperial-rajasthan.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero image
html = html.replace('assets/rajasthan.png', 'assets/imperial_rajasthan_hero.png')
html = html.replace('alt="Rajasthan Palace Tour Banner"', 'alt="Imperial Rajasthan Tour Banner"')

with open('imperial-rajasthan.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Target specifically the card for Imperial Rajasthan Tour
cards = re.split(r'(<!-- Card \d+.*?-->)', index_html)
new_index_html = ""
for chunk in cards:
    if 'href="imperial-rajasthan.html"' in chunk and not 'dropdown-item' in chunk:
        chunk = chunk.replace('assets/rajasthan.png', 'assets/imperial_rajasthan_hero.png')
    new_index_html += chunk

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)
