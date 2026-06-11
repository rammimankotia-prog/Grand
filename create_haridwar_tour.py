import os
import re

# --- Generate HTML ---
with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Title & Meta
html = html.replace('<title>Himachal Exotic Tour (05 Nights 06 Days) | Grand Holidays</title>', '<title>Haridwar Rishikesh Tour Package From Delhi | Grand Holidays</title>')
html = html.replace('content="Himachal Exotic Tour exploring the breathtaking hill stations of Shimla and Manali in a private Swift Dzire."', 'content="Haridwar Rishikesh Tour Package from Delhi. Experience divine Ganga Aarti, sacred temples, and spiritual vibes in a 3 Days 2 Nights journey."')
html = html.replace('href="https://grandholidaytours.com/himachal-exotic-tour.html"', 'href="https://grandholidaytours.com/haridwar-rishikesh-tour.html"')

# Hero Section
html = html.replace('assets/himachal_exotic.png', 'assets/haridwar_rishikesh_hero.png')
html = html.replace('alt="Himachal Exotic Tour Banner"', 'alt="Haridwar Rishikesh Tour Banner"')
html = html.replace('<h1 class="tour-main-title">Himachal Exotic Tour</h1>', '<h1 class="tour-main-title">Haridwar & Rishikesh Spiritual Tour</h1>')
html = html.replace('<span id="display-duration">5 Days / 4 Nights</span>', '<span id="display-duration">3 Days / 2 Nights</span>')
html = html.replace('<span id="display-cities">Delhi - Shimla - Manali</span>', '<span id="display-cities">Delhi - Haridwar - Rishikesh</span>')
html = html.replace('<span id="display-price">From $12,500 p.p.</span>', '<span id="display-price">On Request</span>')

# Price Summary Box
html = html.replace('<span class="summary-value" id="summary-price-display">$12,500 p.p.</span>', '<span class="summary-value" id="summary-price-display">On Request</span>')

# Tour Description
desc = """Haridwar literally means "Gateway of God". Haridwar is one of the most famous holy cities in India. Surrounded by the majestic Shivalik Hills on one side and the mighty Ganges River on the other, Haridwar exudes a mysterious charm that goes further than its reputation as a renowned pilgrimage center. The holy city attracts millions of tourists and pilgrims every year. The chaotic streets and the crowded banks of the river, with throngs of people taking a dip to wash away their sins, radiate a certain energy that is hard to miss. For Hindus, Haridwar is one of the most sacred cities. This 3-day spiritual journey takes you through the divine aura of Haridwar and the serene tranquility of Rishikesh, offering a perfect blend of devotion and peace."""

html = re.sub(r'<p id="tour-short-desc".*?</p>', f'<p id="tour-short-desc" class="block-text">{desc}</p>', html, flags=re.DOTALL)

# Map SVG (Replace entirely)
map_svg = """<svg viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg" class="gt-svg">
                        <defs>
                            <filter id="pinShadow"><feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="rgba(0,0,0,0.28)"/></filter>
                            <filter id="labelShadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.1)"/></filter>
                            <radialGradient id="bgG" cx="50%" cy="50%" r="60%">
                                <stop offset="0%" stop-color="#fdf8f1"/>
                                <stop offset="100%" stop-color="#ede4d5"/>
                            </radialGradient>
                        </defs>
                        <rect x="0" y="0" width="680" height="480" rx="20" fill="url(#bgG)"/>
                        
                        <path id="route-path" d="M340,400 L340,150 L380,80 L340,400" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">
                             <animate attributeName="stroke-dashoffset" from="0" to="-200" dur="5s" repeatCount="indefinite"/>
                        </path>

                        <!-- Distance Badges -->
                        <g transform="translate(260,280)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">220 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>

                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(340, 400)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 3</text>
                        </g>

                        <!-- Delhi (340, 400) -->
                        <g>
                            <circle cx="340" cy="400" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="340" y="425" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">DELHI</text>
                        </g>

                        <!-- Haridwar (340, 150) -->
                        <g>
                            <circle cx="340" cy="150" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="340" y="130" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">HARIDWAR</text>
                        </g>
                        
                        <!-- Rishikesh (380, 80) -->
                        <g>
                            <circle cx="380" cy="80" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="420" y="85" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">RISHIKESH</text>
                        </g>
                    </svg>"""

html = re.sub(r'<svg viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg" class="gt-svg">.*?</svg>', map_svg, html, flags=re.DOTALL)

# Map section title & desc
html = html.replace('<h2 class="gt-map-title">Himachal Exotic Tour Route</h2>', '<h2 class="gt-map-title">Haridwar & Rishikesh Tour Route</h2>')
html = html.replace('<p class="gt-map-subtitle">A mesmerizing journey from the historic capital of Delhi up into the majestic, snow-capped peaks of the Himalayas.</p>', '<p class="gt-map-subtitle">A divine journey from the bustling capital of Delhi to the spiritual havens of Haridwar and Rishikesh along the holy Ganges.</p>')

# Map City Cards
city_cards = """<div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">🏛️</div>
                        <h3 class="city-card-name">Delhi</h3>
                        <p class="city-card-desc">The starting point of your spiritual journey.</p>
                        <div class="city-card-tags"><span>Capital City</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">🛕</div>
                        <h3 class="city-card-name">Haridwar</h3>
                        <p class="city-card-desc">The Gateway of God. Witness the divine Ganga Aarti at Har Ki Pauri and seek blessings at sacred temples.</p>
                        <div class="city-card-tags"><span>Har Ki Pauri</span><span>Mansa Devi</span><span>Chandi Devi</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">03</div>
                        <div class="city-card-icon">🧘‍♂️</div>
                        <h3 class="city-card-name">Rishikesh</h3>
                        <p class="city-card-desc">The Yoga Capital of the World. Walk across the iconic suspension bridges and feel the peaceful vibes.</p>
                        <div class="city-card-tags"><span>Ram Jhula</span><span>Laxman Jhula</span><span>Ashrams</span></div>
                    </div>"""

html = re.sub(r'<div class="gt-city-cards">.*?</div>\s*</div>\s*</div>\s*</div>', f'<div class="gt-city-cards">{city_cards}</div></div></div></div>', html, flags=re.DOTALL)

# FAQ text replace "Himachal Exotic Tour"
html = html.replace('about the Himachal Exotic Tour', 'about the Haridwar & Rishikesh Tour')

# JS File reference
html = html.replace('<script src="himachal-exotic-tour.js"></script>', '<script src="haridwar-rishikesh-tour.js"></script>')

with open('haridwar-rishikesh-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated HTML")

# --- Generate JS ---
js_content = """document.addEventListener('DOMContentLoaded', () => {

    const tourData = {
        highlights: [
            "Witness divine Ganga Aarti at Har Ki Pauri in Haridwar.",
            "Visit Mansa Devi & Chandi Devi temples for spiritual blessings.",
            "Explore sacred sites like Daksh Prajapati Temple & Ashrams.",
            "Short trip to Rishikesh covering Ram Jhula & Laxman Jhula.",
            "Enjoy peaceful ghats, spiritual vibes & holy river views."
        ],
        itinerary: [
            {
                day: "Day 1",
                location: "Haridwar",
                title: "Arrive Delhi \u2013 Haridwar",
                stay: "1 Night",
                desc: "Upon arrival at Delhi airport/ Railway station our executive will receive you with warm welcome. Our representative will take you to Haridwar. Reach in Haridwar check into the hotel and have some rest. By evening you can attend a heart-touching aarti in Har-Ki-Pauri which is believed to be the place where elixir of immortality Nector (Amrit) fell during Samundra Manthan. Later back to the hotel, have some delicious food and stay overnight.",
                meta: "Accommodation & Dinner Only"
            },
            {
                day: "Day 2",
                location: "Haridwar",
                title: "Haridwar Local + Rishikesh Day Trip",
                stay: "1 Night",
                desc: "After having breakfast, proceed to Haridwar Local Sightseeing. Places to visit will be Daksh Prajapati temple, Ananandamai Ashram, Mata Chanda Devi Temples, Mansa Devi, and Parmarth. Later take a short drive from Haridwar to Rishikesh (20 Kms) while enroute covering Bhuma Niketan and Bharat Mata Mandir. In Rishikesh major attraction to cover will be Ram Jhula & Laxman Jhula. Later it is time to return to Haridwar for an overnight stay. Note: Adventure activities at your own cost.",
                meta: "Accommodation, Breakfast & Lunch or Dinner"
            },
            {
                day: "Day 3",
                location: "Haridwar",
                title: "Haridwar \u2013 Delhi Departure",
                stay: "Departure",
                desc: "After a healthy breakfast check out from the hotel of Haridwar. Our representative will take you back to Delhi's Airport/ Railway station for dropping. Take with you good memories with blessings.",
                meta: "Breakfast Only"
            }
        ],
        inclusions: [
            "Pick-up and drop from Delhi Airport/railway station/Bus Stop.",
            "Stay for 2 adults in 1 double room (base category).",
            "2 Breakfasts & 2 Dinners (MAP Plan).",
            "All sightseeing and transfers by private Non-AC Sedan car.",
            "(AC not used in hilly areas. Extra charge if needed in hills \u2013 paid to driver).",
            "Parking, fuel, toll tax & driver charges \u2013 included.",
            "All taxes included (except GST)."
        ],
        exclusions: [
            "Flights, Trains, Ferries etc.",
            "Monument Entrance Fees & Camera Fees.",
            "Parking Inside Monuments / Parks / Temples Etc.",
            "Personal Expenses - Laundry, Shopping, Telephone bills, tips etc.",
            "Adventure Activities - Safari, Rides, Surfing, Paragliding etc.",
            "Any Extra services - Permits, Volvo Luggage Charges, Heater, Meals etc.",
            "Anything else not listed in above details."
        ]
    };

    const highlightsBox = document.getElementById('mode-highlight-box');
    if(highlightsBox) {
        highlightsBox.innerHTML = `
            <ul class="highlight-list">
                ${tourData.highlights.map(h => `<li><span class="hl-dot"></span>${h}</li>`).join('')}
            </ul>
        `;
    }

    const timelineBox = document.getElementById('itinerary-timeline-box');
    if(timelineBox) {
        timelineBox.innerHTML = tourData.itinerary.map(day => `
            <div class="timeline-item">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <span class="day-badge">${day.day} / (${day.location})</span>
                    <h3 class="day-title">${day.title} <span class="stay-tag">${day.stay}</span></h3>
                    <p class="day-desc">${day.desc}</p>
                    <div class="day-meta">
                        <span>🍲 ${day.meta}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    const incList = document.getElementById('inclusions-list');
    if(incList) {
        incList.innerHTML = tourData.inclusions.map(inc => `<li>${inc}</li>`).join('');
    }

    const excList = document.getElementById('exclusions-list');
    if(excList) {
        excList.innerHTML = tourData.exclusions.map(exc => `<li>${exc}</li>`).join('');
    }

    const form = document.getElementById('tourBookingForm');
    const successMsg = document.getElementById('bookingSuccessMessage');
    
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            form.style.display = 'none';
            if (successMsg) successMsg.style.display = 'block';
        });
    }
});
"""

with open('haridwar-rishikesh-tour.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
    
print("Generated JS")
