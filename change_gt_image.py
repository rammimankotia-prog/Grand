import re
import shutil
import os
import glob

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\golden_triangle_hero_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\golden_triangle_hero.png")

# Update golden-triangle.html
with open('golden-triangle.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero image
html = re.sub(r'(<img src=")assets/[^"]+(" alt="Taj Mahal Golden Triangle Banner" class="tour-hero-img">)', r'\g<1>assets/golden_triangle_hero.png\g<2>', html)

with open('golden-triangle.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace image for the Golden Triangle Tour card
# Look for <a href="golden-triangle.html" and update the image right above it inside the card.
# The card structure is:
# <div class="journey-card ...">
#   <div class="card-img-container">
#       <img src="..." alt="Golden Triangle Tour" ...>
# ...
#   <a href="golden-triangle.html" ...>
# We can just match the block if we need to. But let's just replace all "assets/taj_mahal.png" with "assets/golden_triangle_hero.png" in index.html, wait, NO. "5 Days Golden Triangle Tour" also uses taj_mahal.png.
# Let's target the exact image tag for the first Golden Triangle Tour.
# Let's just find the card that contains `href="golden-triangle.html"` and replace its image.

cards = re.split(r'(<!-- Card \d+.*?-->)', index_html)
new_index_html = ""
for chunk in cards:
    if 'href="golden-triangle.html"' in chunk and not 'dropdown-item' in chunk:
        # This is the card for Golden Triangle Tour
        chunk = re.sub(r'<img src="assets/[^"]+"', r'<img src="assets/golden_triangle_hero.png"', chunk)
    new_index_html += chunk

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)
