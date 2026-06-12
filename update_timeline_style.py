from bs4 import BeautifulSoup

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/delhi-museum-tour.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

timeline_box = soup.find('div', id='itinerary-timeline-box')
if timeline_box:
    timeline_box.clear()
    
    itinerary = [
        {'time': '10:00 AM', 'title': 'National Museum', 'desc': "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras."},
        {'time': '11:30 AM', 'title': 'National Rail Museum', 'desc': "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time."},
        {'time': '01:00 PM', 'title': 'International Dolls Museum', 'desc': "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes."}
    ]
    
    clock_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
    
    for item in itinerary:
        block = soup.new_tag('div', **{'class': 'timeline-day-block'})
        
        number = soup.new_tag('div', **{'class': 'timeline-day-number'})
        number.append(BeautifulSoup(clock_svg, 'html.parser'))
        
        wrapper = soup.new_tag('div', **{'class': 'timeline-day-title-wrapper'})
        
        title_div = soup.new_tag('div', **{'class': 'timeline-day-title'})
        time_tag = soup.new_tag('span', **{'class': 'day-tag time-tag'})
        time_tag.string = item['time']
        h4 = soup.new_tag('h4')
        h4.string = item['title']
        title_div.append(time_tag)
        title_div.append(h4)
        
        desc = soup.new_tag('p', **{'class': 'timeline-day-desc'})
        desc.string = item['desc']
        
        wrapper.append(title_div)
        wrapper.append(desc)
        
        block.append(number)
        block.append(wrapper)
        
        timeline_box.append(block)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Timeline replaced successfully.')
