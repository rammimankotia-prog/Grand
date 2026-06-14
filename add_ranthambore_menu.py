import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# New Ranthambore item to inject into the Rajasthan col of the mega menu
old_rajasthan_end = '''<a class="dropdown-item" href="tiger-tour-jaipur.html">
                                        <span class="item-icon">🐯</span>
                                        <span class="item-text">
                                            <span class="item-name">Tiger Tour With Jaipur</span>
                                            <span class="item-sub">Ranthambore Safari · Jaipur</span>
                                        </span>
                                    </a>'''

new_rajasthan_end = old_rajasthan_end + '''
                                    <a class="dropdown-item" href="ranthambore-tiger-safari.html">
                                        <span class="item-icon">🌿</span>
                                        <span class="item-text">
                                            <span class="item-name">Ranthambore Tiger Safari</span>
                                            <span class="item-sub">3 Days · Delhi to Ranthambore</span>
                                        </span>
                                    </a>'''

updated = 0
for filename in os.listdir(repo_path):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(repo_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_rajasthan_end in content and 'ranthambore-tiger-safari.html' not in content:
        content = content.replace(old_rajasthan_end, new_rajasthan_end, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1

print(f"Added Ranthambore to mega menu in {updated} files.")
