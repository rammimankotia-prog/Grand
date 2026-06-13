import os
from bs4 import BeautifulSoup

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_files = [f for f in os.listdir(repo_path) if f.endswith('.html')]

# 1. Update Global Header Navigation
for filename in html_files:
    file_path = os.path.join(repo_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    changed = False
    # Find Tours Dropdown
    tours_dropdown = soup.find('div', class_='dropdown-menu')
    if tours_dropdown:
        # Check if it's already there
        if not tours_dropdown.find('a', href='4-days-golden-triangle-tour.html'):
            # Find the 5 days golden triangle tour link to insert before it
            five_days = tours_dropdown.find('a', href='5-days-golden-triangle-tour.html')
            if five_days:
                new_link = soup.new_tag('a', href='4-days-golden-triangle-tour.html')
                new_link.string = '4 Days Golden Triangle'
                five_days.insert_before(new_link)
                changed = True
                
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

# 2. Update Tour Cards on index.html and all-tours.html
tour_card_html = """
<div class="journey-card reveal reveal-delay-2">
    <div class="card-img-container">
        <img alt="A breathtaking view of the Taj Mahal and Jaipur's royal architecture, representing the Golden Triangle Tour" class="journey-img" src="assets/golden_triangle_hero.png"/>
        <div class="card-badge">Best Seller</div>
    </div>
    <div class="card-content">
        <div class="card-meta">
            <span class="duration">4 Days / 3 Nights</span>
            <span class="divider">|</span>
            <span class="location">Delhi, Agra, Jaipur</span>
        </div>
        <h3 class="card-title">4-Days Golden Triangle Tour</h3>
        <p class="card-text">Experience the vibrant contrasts of Old and New Delhi, witness the Taj Mahal at sunrise, and immerse yourself in the royal grandeur of Jaipur.</p>
        <ul class="card-highlights">
            <li>Delhi Sightseeing</li>
            <li>Taj Mahal Sunrise</li>
            <li>Jaipur City Tour</li>
        </ul>
        <div class="card-footer">
            <span class="price">From $190 <span class="pp">/ person</span></span>
            <a class="btn btn-outline btn-sm" href="4-days-golden-triangle-tour.html">View Tour</a>
        </div>
    </div>
</div>
"""

for fn in ['index.html', 'all-tours.html']:
    fp = os.path.join(repo_path, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    grid = soup.find('div', class_='journeys-grid')
    if grid:
        # Check if it's already there
        if not grid.find('a', href='4-days-golden-triangle-tour.html'):
            # Insert after 5-days tour card if possible
            five_days_card = None
            for a in grid.find_all('a', class_='btn'):
                if a.get('href') == '5-days-golden-triangle-tour.html':
                    five_days_card = a.find_parent('div', class_='journey-card')
                    break
            
            if five_days_card:
                new_card = BeautifulSoup(tour_card_html, 'html.parser')
                five_days_card.insert_after(new_card)
            else:
                grid.append(BeautifulSoup(tour_card_html, 'html.parser'))

            with open(fp, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                print(f'Updated Tour Card in {fn}')
