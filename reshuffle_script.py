import os
import re

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

grid_start = html.find('<div class="journeys-grid">')
if grid_start == -1:
    print('journeys-grid not found')
    exit()

grid_content_start = grid_start + len('<div class="journeys-grid">')

parts = re.split(r'(?=<!-- Card )', html[grid_content_start:])

pre_grid = html[:grid_content_start] + parts[0]
cards_and_after = parts[1:]

parsed_cards = []
after_grid = ''

for part in cards_and_after:
    split_token = '        </div>\n        <div class="all-tours-btn-wrapper">'
    if split_token in part:
        card_content, rest = part.split(split_token, 1)
        parsed_cards.append(card_content)
        after_grid = split_token + rest
    else:
        parsed_cards.append(part)

print(f'Found {len(parsed_cards)} cards.')

delhi_cards = []
agra_cards = []
other_cards = []

for card in parsed_cards:
    lower_card = card.lower()
    is_delhi = any(x in lower_card for x in ['delhi-sightseeing.html', 'delhi-food-tour.html', 'delhi-spiritual-tour.html', 'delhi-bicycle-tour.html', 'delhi-tuk-tuk-tour.html'])
    is_agra = any(x in lower_card for x in ['agra-day-tour.html', 'delhi-agra-2-day-tour.html'])
    
    if is_delhi:
        delhi_cards.append(card)
    elif is_agra:
        agra_cards.append(card)
    else:
        other_cards.append(card)

print(f'Delhi: {len(delhi_cards)}, Agra: {len(agra_cards)}, Other: {len(other_cards)}')

new_html = pre_grid + "".join(delhi_cards) + "".join(agra_cards) + "".join(other_cards) + after_grid

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Updated index.html')
