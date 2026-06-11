import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Create all-tours.html by copying index.html
all_tours_html = index_html

# Update title and hero text for all-tours.html
all_tours_html = all_tours_html.replace('<title>Grand Holidays | Luxury Tour Company</title>', '<title>All Tours | Grand Holidays</title>')
all_tours_html = all_tours_html.replace('<h1 class="hero-title">Experience the Soul of India</h1>', '<h1 class="hero-title">Discover All Our Tours</h1>')
all_tours_html = all_tours_html.replace('<p class="hero-subtitle">Bespoke luxury journeys through royal palaces, golden sands, and spiritual sanctuaries. Unforgettable private tours with Grand Holidays.</p>', '<p class="hero-subtitle">Browse our complete collection of bespoke luxury journeys across India.</p>')

# Remove some sections from all-tours.html that aren't needed (like About)
# Actually, keeping it as a full page is fine, but we can remove the "About Us" section if we want.
# Let's just keep the full structure, it's fine.

with open('all-tours.html', 'w', encoding='utf-8') as f:
    f.write(all_tours_html)

# Now update index.html to only show 6 cards and add the "More Tours" button.
# Let's extract the journeys-grid content
match = re.search(r'(<div class="journeys-grid">)(.*?)(<!-- End of Journeys Grid -->|</section>)', index_html, flags=re.DOTALL)
if match:
    grid_start = match.group(1)
    grid_content = match.group(2)
    
    # Split the grid content into individual cards
    cards = re.split(r'(<!-- Card [0-9a-zA-Z\s]+:.*?-->)', grid_content)
    
    # cards list will have [whitespace, comment, card_html, comment, card_html...]
    # We want to keep only the first 6 cards
    kept_cards = ""
    card_count = 0
    i = 1
    while i < len(cards) and card_count < 6:
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
    
    # Replace the old section with the new one
    # Note: we need to replace exactly what we matched.
    # The end marker could be a lot of things. Let's do a more robust replacement.
    
    # Actually, replacing the whole section:
    # <section id="tours" class="journeys-section"> ... </section>
    section_match = re.search(r'(<section id="tours" class="journeys-section">.*?</section>)', index_html, flags=re.DOTALL)
    if section_match:
        old_section = section_match.group(1)
        
        # We need to construct the new section
        # Replace the inner grid
        new_section = re.sub(r'<div class="journeys-grid">.*</div>\s*</div>\s*</section>', new_grid_content, old_section, flags=re.DOTALL)
        
        # Update index_html
        index_html = index_html.replace(old_section, new_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
