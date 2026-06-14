import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific broken paragraphs in the related tours section
bad_p1 = '<p>Experience the vibrant contrasts of Old and New Delhi, and witness the <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a> at sunrise.</p>'
good_p1 = '<p>Experience the vibrant contrasts of Old and New Delhi, and witness the Taj Mahal at sunrise.</p>'

bad_p2 = '<p>Combine the architectural brilliance of the <a href="agra-day-tour.html" class="seo-internal-link">Taj Mahal</a> with an exhilarating <a href="tiger-tour-jaipur.html" class="seo-internal-link">Tiger Safari</a> in <a href="tiger-tour-jaipur.html" class="seo-internal-link">Ranthambore</a>.</p>'
good_p2 = '<p>Combine the architectural brilliance of the Taj Mahal with an exhilarating Tiger Safari in Ranthambore.</p>'

if bad_p1 in content:
    content = content.replace(bad_p1, good_p1)
    
if bad_p2 in content:
    content = content.replace(bad_p2, good_p2)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed nested anchor tags in related tours.")
