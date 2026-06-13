import os
from bs4 import BeautifulSoup
import shutil

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
source_html = os.path.join(repo_path, '5-days-golden-triangle-tour.html')
target_html = os.path.join(repo_path, '4-days-golden-triangle-tour.html')
source_css = os.path.join(repo_path, 'golden-triangle.css')
target_css = os.path.join(repo_path, '4-days-golden-triangle-tour.css')
source_js = os.path.join(repo_path, 'golden-triangle.js')
target_js = os.path.join(repo_path, '4-days-golden-triangle-tour.js')

# Copy CSS and JS
shutil.copyfile(source_css, target_css)
shutil.copyfile(source_js, target_js)

with open(source_html, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Update SEO Meta tags
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "4-Days Private Golden Triangle Tour: Delhi, Agra & Jaipur by Car | Grand Holidays"

meta_desc = soup.find('meta', attrs={'name': 'description'})
if meta_desc:
    meta_desc['content'] = "Experience the magic of India on a 4-Day Private Golden Triangle Tour. Explore Delhi's heritage, witness the Taj Mahal at sunrise, and discover the royal forts of Jaipur in luxury."

meta_kw = soup.find('meta', attrs={'name': 'keywords'})
if meta_kw:
    meta_kw['content'] = "4 days golden triangle tour, private golden triangle tour india, delhi agra jaipur tour package, taj mahal sunrise tour, jaipur city tour by car, luxury golden triangle tour"

# Update Canonical Link
canonical = soup.find('link', rel='canonical')
if canonical:
    canonical['href'] = "https://grandholidaytours.com/4-days-golden-triangle-tour.html"

# Update CSS/JS links
for link in soup.find_all('link', rel='stylesheet'):
    if 'golden-triangle.css' in link.get('href', ''):
        link['href'] = '4-days-golden-triangle-tour.css?v=1'

for script in soup.find_all('script'):
    if 'golden-triangle.js' in script.get('src', ''):
        script['src'] = '4-days-golden-triangle-tour.js?v=1'

# 2. Hero Section
hero_title = soup.find('h1', class_='hero-title')
if hero_title:
    hero_title.string = "4-Days Private Golden Triangle Tour"

hero_subtitle = soup.find('p', class_='hero-subtitle')
if hero_subtitle:
    hero_subtitle.string = "Delhi, Agra & Jaipur by Car"

# Find the main hero image and update it
for img in soup.find_all('img'):
    if img.get('alt') == 'Golden Triangle Tour India':
        img['src'] = 'assets/golden_triangle_hero.png'
        img['alt'] = "A breathtaking view of the Taj Mahal and Jaipur's royal architecture, representing the Golden Triangle Tour"
        break

# Overview Text
overview = soup.find('p', class_='overview-text')
if overview:
    overview.string = "Embark on an unforgettable 4-day private journey through India's famed Golden Triangle. Experience the vibrant contrasts of Old and New Delhi, witness the ethereal beauty of the Taj Mahal at sunrise in Agra, and immerse yourself in the royal grandeur of Jaipur's palaces and forts. Travel comfortably in a private, air-conditioned vehicle with expert local guides bringing history to life at every stop."

# Meta Info (Duration, Price, etc)
meta_duration = soup.find('span', string=lambda t: t and 'Days' in t and 'Nights' in t)
if meta_duration:
    meta_duration.string = '4 Days / 3 Nights'

# 3. Itinerary Section
timeline_box = soup.find('div', id='itinerary-timeline-box')
if timeline_box:
    timeline_box.clear()
    
    itinerary = [
        {
            'day': 'Day 1',
            'title': 'The Magic of Delhi & Journey to Agra',
            'desc': """Your adventure begins with a flexible morning pickup from anywhere in the Delhi NCR region. We dive straight into history at the towering Qutub Minar, followed by the peaceful, lotus-shaped Bahá'í House of Worship. Enjoy a scenic drive past the majestic Red Fort, India Gate, and the grand Parliament House. Uncover the mysteries of the ancient Agrasen Ki Baoli stepwell, and marvel at Humayun's Tomb, the inspiration for the Taj Mahal. After a delicious local lunch at Connaught Place, we’ll explore the vibrant chaos of Old Delhi—riding through the spice-scented lanes of Chandni Chowk, admiring the grand Jama Masjid, and visiting Asia's largest spice market, Khari Baoli. In the evening, relax on a comfortable drive to Agra, where you'll check into your hotel for the night."""
        },
        {
            'day': 'Day 2',
            'title': 'Sunrise at the Taj Mahal & The Road to the Pink City',
            'desc': """Rise early for an unforgettable sunrise visit to the Taj Mahal. Watch the marble monument change colors in the morning light as your guide shares the timeless love story behind its creation. After breakfast at your hotel, we’ll explore the sprawling courtyards of the imposing Agra Fort. Next, visit the delicate Itmad-ud-Daulah, affectionately known as the "Baby Taj." After savoring authentic Agra cuisine for lunch, you'll be driven comfortably to the vibrant "Pink City" of Jaipur to relax and spend the night."""
        },
        {
            'day': 'Day 3',
            'title': 'Royal Jaipur City Tour',
            'desc': """After a hearty breakfast, begin your exploration of Jaipur's royal heritage. Start at the formidable Jaigarh Fort, perched high on the Aravalli hills and home to the world's largest wheeled cannon. Next, wander through the opulent City Palace, a dazzling blend of Rajasthani and Mughal architecture. Take a moment to photograph the serene Jal Mahal (Water Palace) floating in Man Sagar Lake, and admire the iconic Hawa Mahal (Palace of Winds), with its intricate lattice windows designed for royal ladies. Conclude your day of sightseeing at the Jantar Mantar observatory, a fascinating collection of giant astronomical instruments."""
        },
        {
            'day': 'Day 4',
            'title': 'Farewell and Departure',
            'desc': """Enjoy your final morning in Rajasthan. Depending on your onward travel plans, your driver will either take you on a comfortable drive back to your requested drop-off point in Delhi, or provide a convenient drop-off at Jaipur Airport."""
        }
    ]
    
    for item in itinerary:
        block = soup.new_tag('div', **{'class': 'timeline-day-block'})
        
        number = soup.new_tag('div', **{'class': 'timeline-day-number'})
        number.string = item['day'].split()[-1] # Extracts '1', '2' etc.
        
        wrapper = soup.new_tag('div', **{'class': 'timeline-day-title-wrapper'})
        
        title_div = soup.new_tag('div', **{'class': 'timeline-day-title'})
        day_tag = soup.new_tag('span', **{'class': 'day-tag'})
        day_tag.string = item['day']
        h4 = soup.new_tag('h4')
        h4.string = item['title']
        title_div.append(day_tag)
        title_div.append(h4)
        
        desc = soup.new_tag('p', **{'class': 'timeline-day-desc'})
        desc.string = item['desc']
        
        wrapper.append(title_div)
        wrapper.append(desc)
        
        block.append(number)
        block.append(wrapper)
        
        timeline_box.append(block)

# 4. FAQs
faq_grid = soup.find('div', class_='faq-grid')
if faq_grid:
    faq_grid.clear()
    faqs = [
        {"q": "What is the best time to start the tour on Day 1?", "a": "We recommend starting between 7:00 AM and 11:00 AM. We offer flexible pickup times from anywhere in Delhi NCR to best suit your schedule."},
        {"q": "Are the monument entry tickets included?", "a": "To provide you with maximum flexibility, monument entry tickets are not included in the base price. However, your guide will assist you with purchasing tickets efficiently at every site."},
        {"q": "What type of vehicle will we use?", "a": "You will travel in a comfortable, private air-conditioned vehicle suited to your group size. This is typically a premium Sedan (like a Toyota Etios) for 1-2 passengers, or a spacious SUV (like an Innova Crysta) for larger families."},
        {"q": "Is there a lot of walking involved?", "a": "Yes, exploring the sprawling forts and the Taj Mahal involves a moderate amount of walking. We highly recommend wearing comfortable walking shoes and bringing a hat or sunglasses."},
        {"q": "Can we customize the drop-off location on Day 4?", "a": "Absolutely. On your final day, we can either drive you back to any location in Delhi NCR, or we can drop you off locally at the Jaipur Airport for your onward journey."}
    ]
    for faq in faqs:
        faq_item = soup.new_tag('div', **{'class': 'faq-item'})
        btn = soup.new_tag('button', **{'class': 'faq-question', 'aria-expanded': 'false'})
        q_text = soup.new_tag('span', **{'class': 'faq-q-text'})
        q_text.string = faq['q']
        icon = soup.new_tag('span', **{'class': 'faq-icon'})
        icon.append(BeautifulSoup('<svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"></line><line x1="1" y1="7" x2="13" y2="7"></line></svg>', 'html.parser').svg)
        btn.append(q_text)
        btn.append(icon)
        
        answer = soup.new_tag('div', **{'class': 'faq-answer'})
        inner = soup.new_tag('div', **{'class': 'faq-answer-inner'})
        p = soup.new_tag('p')
        p.string = faq['a']
        inner.append(p)
        answer.append(inner)
        
        faq_item.append(btn)
        faq_item.append(answer)
        faq_grid.append(faq_item)

# Map SVG
svg_map = soup.find('svg', class_='gt-svg')
if svg_map:
    new_svg = """
    <svg class="gt-svg" viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <filter id="pinShadow"><feDropShadow dx="0" dy="3" flood-color="rgba(0,0,0,0.28)" stdDeviation="5"/></filter>
            <filter id="labelShadow"><feDropShadow dx="0" dy="2" flood-color="rgba(0,0,0,0.1)" stdDeviation="3"/></filter>
            <radialGradient cx="50%" cy="50%" id="bgG" r="60%">
                <stop offset="0%" stop-color="#fdf8f1"/>
                <stop offset="100%" stop-color="#ede4d5"/>
            </radialGradient>
            <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b0a090"/>
                <stop offset="50%" stop-color="#A67C31"/>
                <stop offset="100%" stop-color="#b0a090"/>
            </linearGradient>
        </defs>
        
        <rect fill="url(#bgG)" height="100%" rx="16" width="100%"/>
        
        <!-- Map Title -->
        <text fill="#b0a090" font-family="Outfit,sans-serif" font-size="14" font-weight="600" letter-spacing="3" text-anchor="middle" x="340" y="60">GOLDEN TRIANGLE CIRCUIT</text>

        <!-- Route Path -->
        <path id="route-path" d="M 180 140 Q 280 200 450 200 Q 500 280 450 360 Q 280 340 160 300 Q 140 200 180 140" fill="none" stroke="url(#lineGrad)" stroke-dasharray="8 6" stroke-linecap="round" stroke-width="3">
            <animate attributeName="stroke-dashoffset" dur="6s" from="0" repeatCount="indefinite" to="-200"></animate>
        </path>

        <!-- Moving Taxi -->
        <g>
            <animateMotion dur="15s" repeatCount="indefinite" rotate="auto">
                <mpath href="#route-path"></mpath>
            </animateMotion>
            <g transform="translate(-10, -5)">
                <!-- Wheels -->
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="3" y="-1.2"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="13" y="-1.2"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="3" y="10"></rect>
                <rect fill="#111" height="1.2" rx="0.5" width="4" x="13" y="10"></rect>
                <!-- Car body -->
                <rect fill="#f59e0b" height="10" rx="3" stroke="#78350f" stroke-width="1.2" width="20" x="0" y="0"></rect>
                <!-- Front Grill -->
                <rect fill="#1e293b" height="3" rx="0.2" width="0.7" x="19.5" y="3.5"></rect>
                <!-- TAXI text -->
                <rect fill="#fff" height="3" rx="0.5" width="8" x="6" y="3.5"></rect>
                <text fill="#000" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" letter-spacing="0.1" text-anchor="middle" x="10" y="5.7">TAXI</text>
            </g>
        </g>

        <!-- Points -->
        <!-- Delhi -->
        <g transform="translate(180, 140)">
            <circle cx="0" cy="0" r="10" fill="#fff" stroke="#4a90e2" stroke-width="3" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="4" fill="#4a90e2"/>
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="80" x="-40" y="-35"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="-18">New Delhi</text>
        </g>
        
        <!-- Agra -->
        <g transform="translate(450, 200)">
            <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="3" fill="#A67C31"/>
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="60" x="-30" y="-35"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="-18">Agra</text>
        </g>

        <!-- Jaipur -->
        <g transform="translate(160, 300)">
            <circle cx="0" cy="0" r="8" fill="#fff" stroke="#A67C31" stroke-width="4" filter="url(#pinShadow)"/>
            <circle cx="0" cy="0" r="3" fill="#A67C31"/>
            <rect fill="#fff" filter="url(#labelShadow)" height="26" rx="4" width="70" x="-35" y="15"/>
            <text fill="#1a1208" font-family="Cinzel,serif" font-size="12" font-weight="700" text-anchor="middle" x="0" y="32">Jaipur</text>
        </g>
    </svg>
    """
    svg_map.replace_with(BeautifulSoup(new_svg, 'html.parser').svg)

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print('Successfully created 4-days-golden-triangle-tour.html')
