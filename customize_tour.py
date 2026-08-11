import os
import re

# Update HTML
html_path = '8-hours-sightseeing-tour.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements_html = {
    '5 Days Golden Triangle Tour | Grand Holidays': '8 Hours 80km Day Sightseeing Tour by Tempo Traveller | Grand Holidays',
    '5 Days Golden Triangle tour covering Delhi, Jaipur, and Agra in a private Swift Dzire.': '8 Hours 80km Day Sightseeing tour in Delhi by spacious Tempo Traveller for up to 8-16 guests.',
    'luxury golden triangle tour, Delhi Agra Jaipur tour, premium golden triangle package, Taj Mahal luxury tour': 'delhi sightseeing, tempo traveller rental delhi, 8 hours 80 km tour, delhi day tour, group tour delhi',
    'https://grandholidaytours.com/5-days-golden-triangle-tour.html': 'https://grandholidaytours.com/8-hours-sightseeing-tour.html',
    '5-days-golden-triangle-tour.css': '8-hours-sightseeing-tour.css',
    '5-days-golden-triangle-tour.js': '8-hours-sightseeing-tour.js',
    '5 Days Golden Triangle Tour': '8 Hours Day Sightseeing by Tempo Traveller',
    '<span class="tour-badge">HERITAGE CLASSIC</span>': '<span class="tour-badge">DAY SIGHTSEEING</span>',
    'assets/taj_mahal.png': 'assets/delhi_banner.png', # Assuming a generic banner exists, or just keep it
    'Hotel Grand Godwin': 'Anywhere in Delhi',
    'Indian Grill Restaurant': 'At Leisure',
    'Private Transfer': 'Tempo Traveller',
    'Pickup &amp; Drop-off': '8 Hours / 80 KM',
    '5 Days Golden Triangle Route': 'Delhi Sightseeing Route',
    'Three iconic cities. One legendary journey across heritage, royalty and wonder.': 'Experience the best of Delhi at your own pace in a comfortable Tempo Traveller.',
    'Estimated Package Price': 'Estimated Rental Price',
    '₹38,000 (For 2 Adults)': 'From ₹4,500',
    'Deposit Required:</strong> 25%': 'Deposit Required:</strong> 20%',
    'Number of Guests': 'Number of Passengers (Up to 16)',
}

for old, new in replacements_html.items():
    html = html.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update JS
js_path = '8-hours-sightseeing-tour.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# I will just replace the entire tourModes object in the JS file using regex
new_tourModes = """const tourModes = {
        car: {
            duration: "8 Hours / 80 Kilometers",
            cities: "Delhi Local Sightseeing",
            price: "₹4,500 - ₹6,000 (Based on seating capacity)",
            shortDesc: "Experience the vibrant city of Delhi at your own pace with our 8 Hours / 80 Kilometers day sightseeing tour in a spacious and comfortable Tempo Traveller. Perfect for families and groups, this package offers the flexibility to explore the capital's iconic monuments, bustling markets, and historical landmarks together.",
            highlight: "🚐 Includes a dedicated fully air-conditioned Tempo Traveller with a professional local driver for 8 Hours and 80 Kilometers within Delhi.",
            itinerary: [
                { day: 1, time: "09:00 AM", title: "Pick-up & Old Delhi Exploration", desc: "Your chauffeur will pick you up from your hotel or residence in Delhi NCR. Start your day by visiting the historical Red Fort and Jama Masjid in Old Delhi, followed by a drive past the bustling lanes of Chandni Chowk." },
                { day: 1, time: "12:00 PM", title: "New Delhi Monuments", desc: "Head towards New Delhi to visit the iconic India Gate, Parliament House, and Rashtrapati Bhavan (President's Estate). Perfect spots for photography." },
                { day: 1, time: "02:00 PM", title: "Lunch & South Delhi Highlights", desc: "After lunch, visit the serene Lotus Temple and the towering Qutub Minar, a UNESCO World Heritage site showcasing brilliant Indo-Islamic architecture." },
                { day: 1, time: "05:00 PM", title: "Evening Drop-off", desc: "Conclude your 8-hour sightseeing tour with a convenient drop-off at your hotel or any desired location within the city limits." }
            ],
            inclusions: [
                "Air-conditioned Tempo Traveller for 8 Hours / 80 KM",
                "Professional English-speaking driver",
                "Fuel, state taxes, and toll charges within Delhi",
                "Pick-up and drop-off within Delhi NCR"
            ],
            exclusions: [
                "Monument entry fees and camera charges",
                "Meals and beverages",
                "Guide services (can be arranged on request)",
                "Extra kilometers/hours charges beyond 80KM/8Hrs",
                "Parking charges"
            ]
        }
    };"""

js = re.sub(r'const tourModes = \{.*?\n    \};', new_tourModes, js, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
