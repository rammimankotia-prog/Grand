import re
import shutil
import os

# Copy the image
source_image = r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\mehrangarh_fort_1781089487435.png"
dest_image = r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\mehrangarh_fort.png"
if os.path.exists(source_image):
    shutil.copy2(source_image, dest_image)

# Update marvellous-marwar-tour.html
with open('marvellous-marwar-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('assets/rajasthan.png', 'assets/mehrangarh_fort.png')

with open('marvellous-marwar-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace specifically in Marvellous Marwar Tour card
pattern = r'(<img src="assets/)(rajasthan.png)(" alt="Marvellous Marwar Tour")'
index_html = re.sub(pattern, r'\g<1>mehrangarh_fort.png\g<3>', index_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
