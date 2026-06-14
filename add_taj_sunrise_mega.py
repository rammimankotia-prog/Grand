import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

new_item = (
    '                                    <a class="dropdown-item" href="taj-mahal-sunrise-tour.html">\n'
    '                                        <span class="item-icon">🌅</span>\n'
    '                                        <span class="item-text">\n'
    '                                            <span class="item-name">Taj Mahal Sunrise Tour</span>\n'
    '                                            <span class="item-sub">Express Entry · Skip the Line</span>\n'
    '                                        </span>\n'
    '                                    </a>\n'
)

menu_updated = 0
for fname in os.listdir(repo_path):
    if not fname.endswith('.html') or fname == 'taj-mahal-sunrise-tour.html':
        continue
    fpath = os.path.join(repo_path, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # check if already added
    content = ''.join(lines)
    if 'taj-mahal-sunrise-tour.html' in content:
        continue
        
    out_lines = []
    updated = False
    for line in lines:
        if '<a class="dropdown-item" href="agra-day-tour.html">' in line and not updated:
            out_lines.append(new_item)
            updated = True
        out_lines.append(line)
        
    if updated:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)
        menu_updated += 1

print(f'Updated mega menu in {menu_updated} files')
