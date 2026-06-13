import os
from bs4 import BeautifulSoup

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '4-days-golden-triangle-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Remove the mode selector
modes_container = soup.find('div', class_='tour-modes')
if modes_container:
    modes_container.decompose()

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))
