import os
from bs4 import BeautifulSoup

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
target_html = os.path.join(repo_path, 'golden-triangle.html')

with open(target_html, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

mode_switcher = soup.find('div', class_='mode-switcher-container')
if mode_switcher:
    mode_switcher.decompose()

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully removed mode switcher from golden-triangle.html")
