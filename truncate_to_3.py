import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the journeys-grid content
match = re.search(r'(<div class="journeys-grid">)(.*?)(<!-- End of Journeys Grid -->|</section>)', index_html, flags=re.DOTALL)
if match:
    grid_start = match.group(1)
    grid_content = match.group(2)
    
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
    
    new_grid_content = grid_start + "\n" + kept_cards + more_tours_btn + "\n            </div>\n        </div>\n    </section>"
    
    section_match = re.search(r'(<section id="tours" class="journeys-section">.*?</section>)', index_html, flags=re.DOTALL)
    if section_match:
        old_section = section_match.group(1)
        new_section = re.sub(r'<div class="journeys-grid">.*</div>\s*</div>\s*</section>', new_grid_content, old_section, flags=re.DOTALL)
        index_html = index_html.replace(old_section, new_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
