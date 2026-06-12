from bs4 import BeautifulSoup
import re

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/delhi-museum-tour.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Update title and meta
if soup.title:
    soup.title.string = "Delhi Museum Tour | Private Curated Experience"

# Update Hero text
hero_title = soup.find('h1', class_='hero-title')
if hero_title:
    hero_title.string = "Delhi Museum Tour"

hero_subtitle = soup.find('p', class_='hero-subtitle')
if hero_subtitle:
    hero_subtitle.string = "Delhi holds the keys to India's vast and magnificent heritage. Our curated Delhi Museum Tour is an intellectual and visual feast designed for history connoisseurs and art enthusiasts."

# Update overview text (which is under <h2 class="block-title">Tour Description</h2>)
# Look for id="tour-short-desc"
desc = soup.find(id='tour-short-desc')
if desc:
    desc.string = "Experience the evolution of Indian civilization as we guide you through the city's most prestigious archives. With private transport and expert narration, this half-day journey offers an unhurried, deeply informative exploration of India's glorious past and vibrant present."

# Update pricing box
# The price is in <div class="price-amount">$85</div>
price = soup.find('div', class_='price-amount')
if price:
    price.string = "$65"

# Update duration and timings
# Find span with class "detail-text" inside "tour-details-grid"
# e.g. <span>Duration:</span> <span class="detail-text">8 Hours</span>
for dt in soup.find_all('div', class_='detail-item'):
    label = dt.find('span')
    if label and 'Duration' in label.text:
        val = dt.find('span', class_='detail-text')
        if val:
            val.string = "Half Day (10:00 AM - 2:00 PM)"

# Update Itinerary
# Find <div class="timeline">
timeline = soup.find('div', class_='timeline')
if timeline:
    # Clear existing items
    timeline.clear()
    
    # Add National Museum
    item1 = soup.new_tag('div', **{'class': 'timeline-item'})
    dot1 = soup.new_tag('div', **{'class': 'timeline-dot'})
    content1 = soup.new_tag('div', **{'class': 'timeline-content'})
    h4_1 = soup.new_tag('h4')
    h4_1.string = "National Museum"
    p_1 = soup.new_tag('p')
    p_1.string = "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras."
    content1.append(h4_1)
    content1.append(p_1)
    item1.append(dot1)
    item1.append(content1)
    timeline.append(item1)
    
    # Add Rail Museum
    item2 = soup.new_tag('div', **{'class': 'timeline-item'})
    dot2 = soup.new_tag('div', **{'class': 'timeline-dot'})
    content2 = soup.new_tag('div', **{'class': 'timeline-content'})
    h4_2 = soup.new_tag('h4')
    h4_2.string = "National Rail Museum"
    p_2 = soup.new_tag('p')
    p_2.string = "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time."
    content2.append(h4_2)
    content2.append(p_2)
    item2.append(dot2)
    item2.append(content2)
    timeline.append(item2)
    
    # Add Doll Museum
    item3 = soup.new_tag('div', **{'class': 'timeline-item'})
    dot3 = soup.new_tag('div', **{'class': 'timeline-dot'})
    content3 = soup.new_tag('div', **{'class': 'timeline-content'})
    h4_3 = soup.new_tag('h4')
    h4_3.string = "International Dolls Museum"
    p_3 = soup.new_tag('p')
    p_3.string = "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes."
    content3.append(h4_3)
    content3.append(p_3)
    item3.append(dot3)
    item3.append(content3)
    timeline.append(item3)

# Update Inclusions
inc_list = soup.find(id='inclusions-list')
if inc_list:
    inc_list.clear()
    for text in [
        "Sightseeing by private air-conditioned vehicle",
        "Services of local English-Speaking Guide",
        "Monument and museum entry fees",
        "Presently Applicable Taxes",
        "1 bottled water per person"
    ]:
        li = soup.new_tag('li')
        li.string = text
        inc_list.append(li)

# Update Exclusions
exc_list = soup.find(id='exclusions-list')
if exc_list:
    exc_list.clear()
    for text in [
        "Personal expenses (drinks, telephone calls, tips)",
        "Additional expenses due to weather or unforeseen disturbances",
        "Insurance against injury, accidents, or loss of goods",
        "Specific camera or photography fees inside museums"
    ]:
        li = soup.new_tag('li')
        li.string = text
        exc_list.append(li)

# Update Route Map section
map_title = soup.find('h2', class_='gt-map-title')
if map_title:
    map_title.string = "Delhi Museum Circuit"
    
map_subtitle = soup.find('p', class_='gt-map-subtitle')
if map_subtitle:
    map_subtitle.string = "A chronological journey through India's rich arts, heritage, and industrial wonders."

# Replace the map SVG and cards
# For simplicity, we can remove the complex SVG route map and just show the cards, or keep a simpler structure.
# Let's find the cards container
city_cards = soup.find_all('div', class_='gt-city-card')
if len(city_cards) >= 3:
    city_cards[0].find('h3', class_='city-card-name').string = "National Museum"
    city_cards[0].find('p', class_='city-card-desc').string = "Explore 5,000 years of civilization and art."
    
    city_cards[1].find('h3', class_='city-card-name').string = "National Rail Museum"
    city_cards[1].find('p', class_='city-card-desc').string = "Discover majestic vintage locomotives."
    
    city_cards[2].find('h3', class_='city-card-name').string = "Dolls Museum"
    city_cards[2].find('p', class_='city-card-desc').string = "View 6,000 intricately crafted dolls globally."

# Update FAQs
faq_container = soup.find('div', class_='faq-container')
if faq_container:
    faq_container.clear()
    faqs = [
        ("What are the operating hours?", "Most museums operate from 10:00 AM to 5:00 PM and remain closed on Mondays."),
        ("Are cameras allowed inside the museums?", "Photography rules vary strictly by museum. While some prohibit it entirely, others permit it in specific areas or upon payment of an additional camera fee. Your guide will assist you with the specific policies."),
        ("Is this tour suitable for children?", "Absolutely. The National Rail Museum, with its vintage trains and toy train ride, along with the International Dolls Museum, are exceptionally popular and engaging for younger travelers.")
    ]
    for q, a in faqs:
        item = soup.new_tag('div', **{'class': 'faq-item glass-card'})
        question_div = soup.new_tag('div', **{'class': 'faq-question'})
        q_span = soup.new_tag('span')
        q_span.string = q
        icon_span = soup.new_tag('span', **{'class': 'faq-icon'})
        icon_span.string = "➕"
        question_div.append(q_span)
        question_div.append(icon_span)
        
        answer_div = soup.new_tag('div', **{'class': 'faq-answer'})
        p_ans = soup.new_tag('p')
        p_ans.string = a
        answer_div.append(p_ans)
        
        item.append(question_div)
        item.append(answer_div)
        faq_container.append(item)

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
