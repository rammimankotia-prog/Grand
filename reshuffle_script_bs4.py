from bs4 import BeautifulSoup, Comment
import re

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

grid = soup.find('div', class_='journeys-grid')

if not grid:
    print('Grid not found')
    exit()

# We want to extract cards and their preceding comments
cards_data = []

# Children can be tags or NavigableStrings
current_comment = None
for child in list(grid.children):
    if isinstance(child, Comment):
        # We assume comments like <!-- Card 1: ... --> belong to the next tag
        current_comment = child
    elif child.name == 'div' and 'journey-card' in child.get('class', []):
        cards_data.append({
            'comment': current_comment,
            'tag': child
        })
        # Reset comment
        current_comment = None

print(f'Found {len(cards_data)} cards.')

delhi_cards = []
agra_cards = []
other_cards = []

for item in cards_data:
    # Use the links and text to determine type
    tag_str = str(item['tag']).lower()
    
    is_delhi = any(x in tag_str for x in [
        'delhi-sightseeing.html', 
        'delhi-food-tour.html', 
        'delhi-spiritual-tour.html', 
        'delhi-bicycle-tour.html', 
        'delhi-tuk-tuk-tour.html'
    ])
    
    is_agra = any(x in tag_str for x in [
        'agra-day-tour.html', 
        'delhi-agra-2-day-tour.html'
    ])
    
    if is_delhi:
        delhi_cards.append(item)
    elif is_agra:
        agra_cards.append(item)
    else:
        other_cards.append(item)

print(f'Delhi: {len(delhi_cards)}, Agra: {len(agra_cards)}, Other: {len(other_cards)}')

# Clear the grid contents
grid.clear()

# Add them back in order
# Also fix the reveal-delay classes so they stagger properly 1,2,3,4, 1,2,3,4
def append_cards(cards, start_idx):
    for i, item in enumerate(cards):
        delay = (start_idx + i) % 4 + 1
        
        # update reveal-delay
        tag = item['tag']
        classes = tag.get('class', [])
        new_classes = [c for c in classes if not c.startswith('reveal-delay-')]
        new_classes.append(f'reveal-delay-{delay}')
        tag['class'] = new_classes
        
        # Append comment
        if item['comment']:
            grid.append('\n                ')
            grid.append(item['comment'])
            
        grid.append('\n                ')
        grid.append(tag)
        grid.append('\n\n')

# Append
grid.append('\n')
append_cards(delhi_cards, 0)
append_cards(agra_cards, len(delhi_cards))
append_cards(other_cards, len(delhi_cards) + len(agra_cards))

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Updated index.html successfully using BS4.')
