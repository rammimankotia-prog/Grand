import os
import glob

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# 1. Rename files
old_html = os.path.join(repo_path, 'golden-triangle.html')
new_html = os.path.join(repo_path, '8-days-golden-triangle-tour.html')
if os.path.exists(old_html):
    os.rename(old_html, new_html)

old_js = os.path.join(repo_path, 'golden-triangle.js')
new_js = os.path.join(repo_path, '8-days-golden-triangle-tour.js')
if os.path.exists(old_js):
    os.rename(old_js, new_js)

old_css = os.path.join(repo_path, 'golden-triangle.css')
new_css = os.path.join(repo_path, '8-days-golden-triangle-tour.css')
if os.path.exists(old_css):
    os.rename(old_css, new_css)

# 2. Update new_html references
if os.path.exists(new_html):
    with open(new_html, 'r', encoding='utf-8') as f:
        html_content = f.read()

    html_content = html_content.replace('golden-triangle.js', '8-days-golden-triangle-tour.js')
    html_content = html_content.replace('golden-triangle.css', '8-days-golden-triangle-tour.css')
    html_content = html_content.replace('<h1 class="tour-main-title">The Golden Triangle Reimagined</h1>', '<h1 class="tour-main-title">8 Days Golden Triangle Tour</h1>')
    html_content = html_content.replace('<title>Luxury Golden Triangle Tour | Delhi, Agra, Jaipur | Grand Holidays</title>', '<title>8 Days Golden Triangle Tour | Grand Holidays</title>')

    with open(new_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

# 3. Update all links in the repository pointing to golden-triangle.html
for filepath in glob.glob(os.path.join(repo_path, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'golden-triangle.html' in content:
        content = content.replace('golden-triangle.html', '8-days-golden-triangle-tour.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print('Migration complete')
