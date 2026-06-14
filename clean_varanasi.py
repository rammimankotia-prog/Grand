import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
filepath = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old schema
content = re.sub(r'<!-- JSON-LD Schema -->.*?</script>', '', content, flags=re.DOTALL)

# Remove old breadcrumbs
content = re.sub(r'<nav aria-label="breadcrumb"[^>]*>.*?</nav>', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Cleaned up Varanasi HTML.')
