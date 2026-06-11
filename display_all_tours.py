with open('all-tours.html', 'r', encoding='utf-8') as f:
    all_tours = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract everything between <div class="journeys-grid"> and the end of the section in all_tours.html
start_marker = '<div class="journeys-grid">'
end_marker = '            </div>\n        </div>\n    </section>'

start_idx = all_tours.find(start_marker)
end_idx = all_tours.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    full_grid = all_tours[start_idx:end_idx]
    
    # We want ALL cards. Let's parse them by <!-- Card
    parts = full_grid.split('<!-- Card')
    
    # parts[0] is the <div class="journeys-grid">\n
    # parts[1] is the first card, parts[2] is the second...
    # Keep ALL cards
    kept_grid = parts[0]
    for i in range(1, len(parts)):
        kept_grid += '<!-- Card' + parts[i]
        
    # Since all tours are displayed, we don't need the View All Tours button anymore.
    
    # Now replace the grid in index_html
    idx_start = index_html.find(start_marker)
    idx_end = index_html.find(end_marker, idx_start)
    
    if idx_start != -1 and idx_end != -1:
        new_index = index_html[:idx_start] + kept_grid + index_html[idx_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_index)
        print(f"Success! Restored all {len(parts)-1} tours to the homepage.")
    else:
        print("Failed to find boundaries in index.html")
else:
    print("Failed to find boundaries in all-tours.html")
