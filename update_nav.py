import os
import re

for file in os.listdir('C:/Users/raman/.gemini/antigravity/scratch/grand_repo'):
    if file.endswith('.html'):
        path = os.path.join('C:/Users/raman/.gemini/antigravity/scratch/grand_repo', file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'href="delhi-museum-tour.html"' not in content:
            content = re.sub(r'<a[^>]*href=\"delhi-sightseeing\.html\"[^>]*>Delhi Sightseeing Tour</a>', 
                             lambda m: m.group(0) + '\n                          <a href="delhi-museum-tour.html" class="dropdown-item">Delhi Museum Tour</a>', 
                             content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
print("Updated all HTML files.")
