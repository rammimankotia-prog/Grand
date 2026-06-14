import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# The inline <style> block in each page sets min-width: 230px for dropdown-menu.
# We need to override that so the mega-menu can be wide.
# Also ensure the inline mobile override doesn't set display:none on .mega-menu
# We'll inject a small patch right after the existing inline style tag closes.

patch_css = """<style>
/* Mega-menu override patch */
@media (min-width: 769px) {
    .mega-menu { min-width: 860px !important; opacity: 0; visibility: hidden; display: block; }
    .nav-dropdown:hover .mega-menu { opacity: 1; visibility: visible; }
}
@media (max-width: 768px) {
    .mega-menu { display: none; opacity: 1 !important; visibility: visible !important; }
    .nav-dropdown.active .mega-menu { display: block !important; }
}
</style>
"""

updated = 0
for filename in os.listdir(repo_path):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(repo_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Mega-menu override patch' in content:
        print(f"Already patched: {filename}")
        continue

    # Insert the patch just before </head>
    if '</head>' in content:
        content = content.replace('</head>', patch_css + '</head>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"Patched {filename}")

print(f"\nPatched {updated} files.")
