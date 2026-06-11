import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# The grid starts with <div class="journeys-grid">
match = re.search(r'(<div class="journeys-grid">)(.*?)(<div style="text-align: center; margin-top: 4rem; grid-column: 1 / -1; width: 100%;">\s*<a href="all-tours.html")', index_html, flags=re.DOTALL)

if not match:
    # Maybe we didn't match the button. Let's just find the grid end.
    match = re.search(r'(<div class="journeys-grid">)(.*?)(</div>\s*</div>\s*</section>)', index_html, flags=re.DOTALL)

if match:
    grid_start = match.group(1)
    grid_content = match.group(2)
    grid_end = match.group(3)
    
    # Split the grid content into individual cards
    cards = re.split(r'(<!-- Card [0-9a-zA-Z\s]+:.*?-->)', grid_content)
    
    # We want to keep only the first 3 cards
    kept_cards = ""
    card_count = 0
    i = 1
    while i < len(cards) and card_count < 3:
        kept_cards += cards[i] # the comment
        kept_cards += cards[i+1] # the html
        card_count += 1
        i += 2
        
    more_tours_btn = """
                <div style="text-align: center; margin-top: 4rem; grid-column: 1 / -1; width: 100%;">
                    <a href="all-tours.html" class="btn btn-primary" style="padding: 1rem 3rem; font-size: 1.1rem; border-radius: 50px;">View All Tours</a>
                </div>
"""
    
    # Replace the old grid content with the kept cards
    new_index = index_html[:match.start(2)] + "\n" + kept_cards + "\n" + more_tours_btn + "\n            " + index_html[match.start(3):]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_index)
    print("Successfully updated index.html")
else:
    print("Failed to match grid section")
