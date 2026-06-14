import os
import glob
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

gtag_snippet = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-JQZ228N6MG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-JQZ228N6MG');
</script>"""

modified_files = []

for filepath in glob.glob(os.path.join(repo_path, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already installed
    if 'G-JQZ228N6MG' in content:
        continue
        
    # Replace the first <head> tag
    # Use regex to handle potential attributes in <head>, though usually it's just <head>
    new_content, count = re.subn(r'(<head[^>]*>)', r'\1' + gtag_snippet, content, count=1, flags=re.IGNORECASE)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_files.append(os.path.basename(filepath))

print(f"Added Google tag to {len(modified_files)} HTML files.")
