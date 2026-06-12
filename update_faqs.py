from bs4 import BeautifulSoup

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/delhi-museum-tour.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

faq_grid = soup.find('div', class_='faq-grid')
if faq_grid:
    faq_grid.clear()
    
    faqs = [
        {
            "q": "Which museums are covered in this tour?",
            "a": "Our curated museum circuit focuses on three of Delhi's most fascinating repositories: The National Museum for 5,000 years of cultural antiquities, the National Rail Museum for majestic vintage locomotives, and the International Dolls Museum showcasing over 6,000 dolls from 85 countries."
        },
        {
            "q": "Are museum entry tickets included in the price?",
            "a": "Yes! Your $65 per person package covers all museum entry fees, as well as private transportation in an air-conditioned vehicle, bottled water, and the services of an English-speaking guide."
        },
        {
            "q": "How long does the tour take?",
            "a": "This is a Half-Day tour taking approximately 4 hours to complete. We typically begin at 10:00 AM to align with museum opening hours, and conclude by 2:00 PM."
        },
        {
            "q": "Is this tour suitable for children and families?",
            "a": "Absolutely! In fact, this is one of our most family-friendly itineraries. The National Rail Museum (with its vintage toy train rides) and the International Dolls Museum are especially captivating for children of all ages."
        },
        {
            "q": "What days are the museums open?",
            "a": "The museums on this tour operate from Tuesday to Sunday, generally between 10:00 AM and 5:00 PM. Please note that all three museums are closed on Mondays."
        },
        {
            "q": "Are we allowed to take photographs inside?",
            "a": "Photography policies vary by institution. The National Museum and Rail Museum generally permit photography (though professional video equipment may require special permission or a nominal fee), whereas the International Dolls Museum typically restricts indoor photography to preserve the exhibits."
        }
    ]
    
    for faq in faqs:
        faq_item = soup.new_tag('div', **{'class': 'faq-item'})
        
        btn = soup.new_tag('button', **{'class': 'faq-question', 'aria-expanded': 'false'})
        q_text = soup.new_tag('span', **{'class': 'faq-q-text'})
        q_text.string = faq['q']
        icon = soup.new_tag('span', **{'class': 'faq-icon'})
        # Insert SVG directly
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

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('FAQs updated successfully.')
