import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
css_link = '<link href="mega-menu.css?v=1" rel="stylesheet"/>'

updated = 0
for filename in os.listdir(repo_path):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(repo_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already linked
    if 'mega-menu.css' in content:
        print(f"Already has mega-menu.css: {filename}")
        continue

    # Insert just before </head>
    if '</head>' in content:
        content = content.replace('</head>', css_link + '\n</head>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"Linked mega-menu.css in {filename}")
    else:
        print(f"No </head> found in {filename}")

print(f"\nLinked CSS in {updated} files.")
