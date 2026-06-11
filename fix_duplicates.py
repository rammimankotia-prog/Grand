import re

def fix_duplicates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the tour grid section
    grid_pattern = re.compile(r'(<div class="journeys-grid".*?>)(.*?)(</div>\s*</div>\s*</section>|</div>\s*<div style="text-align: center;)', re.DOTALL)
    match = grid_pattern.search(html)
    
    if not match:
        print(f"Could not find tour grid in {filename}")
        return

    prefix = match.group(1)
    grid_content = match.group(2)
    suffix = match.group(3)

    card_starts = [m.start() for m in re.finditer(r'<div class="journey-card', grid_content)]
    card_starts.append(len(grid_content))
    
    new_grid_content = grid_content[:card_starts[0]] 
    seen_titles = set()
    
    for i in range(len(card_starts) - 1):
        start = card_starts[i]
        end = card_starts[i+1]
        
        card_chunk = grid_content[start:end]
        
        title_match = re.search(r'<h3 class="card-title">(.*?)</h3>', card_chunk)
        if title_match:
            title = title_match.group(1).strip()
            if title not in seen_titles:
                seen_titles.add(title)
                prev_text = grid_content[card_starts[i-1] if i > 0 else 0 : start]
                if i == 0:
                    prev_text = grid_content[:start]
                    
                comment = ""
                cm = re.search(r'(\s*<!-- Card:.*?-->\s*)$', prev_text)
                if cm:
                    comment = cm.group(1)
                    
                new_grid_content += comment + card_chunk
            else:
                print(f"Removed duplicate card: '{title}' from {filename}")
        else:
            new_grid_content += card_chunk

    new_html = html[:match.start()] + prefix + new_grid_content + suffix + html[match.end():]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)

fix_duplicates('index.html')
fix_duplicates('all-tours.html')
