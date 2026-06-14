import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

for fname in ['index.html', 'all-tours.html']:
    fpath = os.path.join(repo_path, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Taj Mahal Sunrise Tour card and replace its price
    card_marker = '<!-- Card: Taj Mahal Sunrise Tour -->'
    if card_marker in content:
        # Split by marker, there's only one such card
        parts = content.split(card_marker)
        if len(parts) > 1:
            # We want to replace the FIRST 'On Request' in the card html (parts[1])
            # The structure in card is <span class="price">On Request</span>
            new_price = '₹12,000 <span class="pp">/ person <small style="font-size:0.7em;opacity:0.75;">(min. 2 pax)</small></span>'
            parts[1] = parts[1].replace('<span class="price">On Request</span>', f'<span class="price">{new_price}</span>', 1)
            content = card_marker.join(parts)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated price in {fname}')
        
print("Done!")
