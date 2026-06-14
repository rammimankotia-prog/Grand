import os
import glob
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

pattern = re.compile(r'<button class="btn btn-ghost btn-hero" id="playVideoBtn">\s*<svg.*?</svg>\s*Our Philosophy\s*</button>', re.DOTALL)

modified_files = []

for filepath in glob.glob(os.path.join(repo_path, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if pattern.search(content):
        new_content = pattern.sub('', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_files.append(os.path.basename(filepath))

print(f"Removed 'Our Philosophy' button from {len(modified_files)} files: {', '.join(modified_files)}")
