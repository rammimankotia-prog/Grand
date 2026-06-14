import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace H1
content = content.replace('<h1 class="tour-main-title">8 Days Golden Triangle Tour</h1>', '<h1 class="tour-main-title">8-Day Golden Triangle with Varanasi by Flight</h1>')

# Replace Title
content = content.replace('<title>8 Days Golden Triangle & Varanasi Tour | Grand Holidays</title>', '<title>8-Day Golden Triangle with Varanasi by Flight | Grand Holidays</title>')

# Replace Schema Names
content = content.replace('"name": "8 Days Golden Triangle & Varanasi Tour"', '"name": "8-Day Golden Triangle with Varanasi by Flight"')

# Replace Breadcrumb
content = content.replace('<li aria-current="page" style="font-weight: 500;">8 Days Golden Triangle & Varanasi Tour</li>', '<li aria-current="page" style="font-weight: 500;">8-Day Golden Triangle with Varanasi by Flight</li>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated title.')
