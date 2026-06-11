import re
import shutil
import glob
import os

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\himachal_exotic_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\himachal_exotic.png")

with open('rajasthan-desert-adventure.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Hotel table we added previously
hotel_table_pattern = r'<!-- Accommodation & Vehicle Info -->.*?</div>\s*</div>'
html = re.sub(hotel_table_pattern, '', html, flags=re.DOTALL)

# Replace HTML specific fields
html = html.replace('Rajasthan Desert Adventure Tour (04 Nights 05 Days)', 'Himachal Exotic Tour (05 Nights 06 Days)')
html = html.replace('Rajasthan Desert Adventure Tour exploring Jodhpur and Jaisalmer', 'Himachal Exotic Tour exploring the breathtaking hill stations of Shimla and Manali')
html = html.replace('rajasthan-desert-adventure.html', 'himachal-exotic-tour.html')
html = html.replace('rajasthan-desert-adventure.js', 'himachal-exotic-tour.js')
html = html.replace('Rajasthan Desert Adventure Banner', 'Himachal Exotic Tour Banner')
html = html.replace('Rajasthan Desert Adventure', 'Himachal Exotic Tour')
html = html.replace('assets/desert_adventure.png', 'assets/himachal_exotic.png')
html = html.replace('Jodhpur - Jaisalmer', 'Delhi - Shimla - Manali')
html = html.replace('New Grand Holidays Booking: Rajasthan Desert Adventure Tour', 'New Grand Holidays Booking: Himachal Exotic Tour')

# Map specific replacements
html = html.replace('Rajasthan Desert Adventure Route', 'Himachal Exotic Route')
html = html.replace('An unforgettable desert odyssey connecting the majestic Blue City with the Golden Sands of Jaisalmer.', 'A mesmerizing journey from the historic capital of Delhi up into the majestic, snow-capped peaks of the Himalayas.')

# Replace map SVG entirely
new_svg = """                    <svg viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg" class="gt-svg">
                        <defs>
                            <filter id="pinShadow"><feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="rgba(0,0,0,0.28)"/></filter>
                            <filter id="labelShadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.1)"/></filter>
                            <radialGradient id="bgG" cx="50%" cy="50%" r="60%">
                                <stop offset="0%" stop-color="#fdf8f1"/>
                                <stop offset="100%" stop-color="#ede4d5"/>
                            </radialGradient>
                        </defs>
                        <rect x="0" y="0" width="680" height="480" rx="20" fill="url(#bgG)"/>
                        
                        <!-- Route Line Paths Connecting Sights -->
                        <path id="route-path" d="M450,380 L350,180 L250,60 L450,380" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">
                             <animate attributeName="stroke-dashoffset" from="0" to="-200" dur="5s" repeatCount="indefinite"/>
                        </path>

                        <!-- Moving Taxi Sedan along route -->
                        <g>
                            <animateMotion dur="16s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#route-path"/>
                            </animateMotion>
                            <g transform="translate(-10, -5)">
                                <!-- Wheels -->
                                <rect x="3" y="-1.2" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="13" y="-1.2" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="3" y="10" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <rect x="13" y="10" width="4" height="1.2" fill="#111" rx="0.5"/>
                                <!-- Car body -->
                                <rect x="0" y="0" width="20" height="10" rx="3" fill="#f59e0b" stroke="#78350f" stroke-width="1.2"/>
                                <!-- Front Grill -->
                                <rect x="19.5" y="3.5" width="0.7" height="3" fill="#1e293b" rx="0.2"/>
                                <!-- Headlights -->
                                <rect x="18.5" y="0.8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <rect x="18.5" y="8" width="1.2" height="1.2" rx="0.3" fill="#fef08a" stroke="#ca8a04" stroke-width="0.4"/>
                                <!-- Taillights -->
                                <rect x="-0.3" y="0.8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <rect x="-0.3" y="8" width="0.8" height="1.2" rx="0.3" fill="#ef4444"/>
                                <!-- Windshield -->
                                <path d="M12,1.5 L15,3 L15,7 L12,8.5 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Rear Window -->
                                <path d="M5,1.8 L3.5,3 L3.5,7 L5,8.2 Z" fill="#e0f2fe" stroke="#0369a1" stroke-width="0.5"/>
                                <!-- Side windows -->
                                <rect x="5.5" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="0.8" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="5.5" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <rect x="8.8" y="8.4" width="2.8" height="0.8" fill="#e0f2fe"/>
                                <!-- Bumpers -->
                                <rect x="-0.8" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <rect x="20" y="2" width="0.8" height="6" fill="#1e293b" rx="0.3"/>
                                <!-- Taxi Light -->
                                <rect x="7.5" y="3.5" width="5" height="3" rx="0.6" fill="#fff" stroke="#b45309" stroke-width="0.8"/>
                                <text x="10" y="5.7" font-family="Outfit, sans-serif" font-size="2.2" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="0.1">TAXI</text>
                            </g>
                        </g>

                        <!-- Distance Badges -->
                        <g transform="translate(400,280)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">340 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~8 hrs drive</text>
                        </g>

                        <g transform="translate(300,120)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">250 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~7 hrs drive</text>
                        </g>

                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(450, 380)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 6</text>
                        </g>

                        <!-- Delhi (450, 380) -->
                        <g>
                            <circle cx="450" cy="380" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="450" y="405" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">DELHI</text>
                        </g>

                        <!-- Shimla (350, 180) -->
                        <g>
                            <circle cx="350" cy="180" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="350" y="160" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">SHIMLA</text>
                        </g>
                        
                        <!-- Manali (250, 60) -->
                        <g>
                            <circle cx="250" cy="60" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="250" y="40" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">MANALI</text>
                        </g>

                    </svg>"""

old_svg_pattern = r'<svg viewBox="0 0 680 480".*?</svg>'
html = re.sub(old_svg_pattern, new_svg, html, flags=re.DOTALL)

# Update the City Cards under the map
old_city_cards = r'<div class="gt-city-cards">.*?<div class="gt-city-card">.*?02</div>.*?</div>\s*</div>'

new_city_cards = """<div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127960;</div>
                        <h3 class="city-card-name">Delhi</h3>
                        <p class="city-card-desc">The historic capital. A blend of ancient monuments, vibrant markets, and wide, leafy boulevards.</p>
                        <div class="city-card-tags"><span>India Gate</span><span>Qutub Minar</span><span>Lotus Temple</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#127956;</div>
                        <h3 class="city-card-name">Shimla</h3>
                        <p class="city-card-desc">The 'Queen of Hills'. Famous for its colonial architecture, the bustling Mall Road, and scenic snow peaks at Kufri.</p>
                        <div class="city-card-tags"><span>Mall Road</span><span>Kufri</span><span>Jhakoo Temple</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">03</div>
                        <div class="city-card-icon">&#9978;</div>
                        <h3 class="city-card-name">Manali</h3>
                        <p class="city-card-desc">A paradise for nature lovers and adventurers. Beautiful pine forests, ancient temples, and thrilling valleys.</p>
                        <div class="city-card-tags"><span>Solang Valley</span><span>Hadimba Temple</span><span>Rohtang</span></div>
                    </div>
                </div>"""
html = re.sub(old_city_cards, new_city_cards, html, flags=re.DOTALL)

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now generate JS file with simplified human-readable itinerary
js_content = """document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "6 Days / 5 Nights",
            cities: "Delhi - Shimla - Manali",
            price: "On Request",
            shortDesc: "Escape to the magnificent Himalayas! This refreshing 6-day journey takes you through the beautiful pine forests and snow-capped peaks of Shimla and Manali, starting and ending in Delhi.",
            highlight: "🚗 Includes private premium A/C transport, daily delicious breakfast, and complete assistance.",
            itinerary: [
                { day: 1, title: "Welcome to Delhi & The Drive to Shimla", desc: "Your adventure begins! We will warmly welcome you at the Delhi airport or railway station. You'll then hop into your private luxury car for a scenic drive up into the mountains to Shimla. Known as the 'Queen of Hills', Shimla boasts a wonderful, laid-back atmosphere. Check into your hotel and enjoy a relaxing evening at your own pace." },
                { day: 2, title: "Shimla Sightseeing & Exploring Kufri", desc: "After a delicious breakfast, we head to Kufri, a stunning nature retreat famous for its snow slopes, winter sports, and the Himalayan Nature Park (home to over 180 animal species!). Later, we'll visit the famous Jhakoo Temple and give you plenty of time to shop and stroll along Shimla's iconic Mall Road before enjoying a mouth-watering dinner back at the resort." },
                { day: 3, title: "The Journey to Manali", desc: "Today, enjoy breakfast and check out, as we hit the road for the beautiful drive from Shimla to Manali. You'll watch the scenery transform as we travel deeper into the Himalayas. After checking into your hotel in Manali, you can spend the evening relaxing or exploring the local markets." },
                { day: 4, title: "Manali Adventure & Sightseeing", desc: "Get ready for a fun-filled day! First, we visit the breathtaking Solang Valley where you can try thrilling activities like paragliding and zorbing. In the afternoon, we'll explore Manali's cultural gems: the peaceful Tibetan Monastery, the natural hot springs at Vashist Village, and the ancient, forest-surrounded Hadimba Devi Temple. Enjoy your evening back at the hotel or taking a walk down Mall Road." },
                { day: 5, title: "Return to Delhi & City Tour", desc: "After breakfast, we take the long, scenic drive back down the mountains to Delhi. Once we arrive in the capital, you'll stretch your legs with a wonderful sightseeing tour of New Delhi! You'll visit the majestic India Gate, the President's House, the historic Qutub Minar, the beautiful Lotus Temple, and Raj Ghat. Check into your Delhi hotel for a restful night." },
                { day: 6, title: "Departure from Delhi", desc: "Enjoy your final breakfast at the hotel. We'll assist you with checking out and provide a comfortable transfer to the Delhi Airport or Railway Station for your journey home, carrying wonderful memories of the Himalayas!" }
            ],
            inclusions: [
                "Assistance on Arrival.",
                "A 24 – hour helpline.",
                "Daily Breakfast",
                "Hotel Accommodation",
                "Travelling in an AC car."
            ],
            exclusions: [
                "Air fare / train fare.",
                "Guide & Monuments fees",
                "Camera & safari Charges",
                "Insurance",
                "Any other item not specified."
            ]
        }
    };

    const displayDuration = document.getElementById('display-duration');
    const displayCities = document.getElementById('display-cities');
    const displayPrice = document.getElementById('display-price');
    const tourShortDesc = document.getElementById('tour-short-desc');
    const modeHighlightBox = document.getElementById('mode-highlight-box');
    const timelineBox = document.getElementById('itinerary-timeline-box');
    const inclusionsList = document.getElementById('inclusions-list');
    const exclusionsList = document.getElementById('exclusions-list');
    const summaryPriceDisplay = document.getElementById('summary-price-display');
    const selectedModeInput = document.getElementById('selected-tour-mode');

    function updateTourDisplay(modeKey) {
        const modeData = tourModes[modeKey];
        if (!modeData) return;

        if (displayDuration) displayDuration.innerText = modeData.duration;
        if (displayCities) displayCities.innerText = modeData.cities;
        if (displayPrice) displayPrice.innerText = `${modeData.price}`;
        if (tourShortDesc) tourShortDesc.innerText = modeData.shortDesc;
        if (summaryPriceDisplay) summaryPriceDisplay.innerText = `${modeData.price}`;
        if (selectedModeInput) selectedModeInput.value = modeKey;

        if (modeHighlightBox) modeHighlightBox.innerText = modeData.highlight;

        if (timelineBox) {
            timelineBox.innerHTML = '';
            modeData.itinerary.forEach((item, idx) => {
                const dayBlock = document.createElement('div');
                dayBlock.className = 'timeline-day-block';

                const stepNum = idx + 1;
                const circleLabel = item.time ? stepNum : item.day;
                const tagLabel = item.time
                    ? `<span class="day-tag time-tag">${item.time}</span>`
                    : `<span class="day-tag">Day ${item.day}</span>`;

                dayBlock.innerHTML = `
                    <div class="tl-circle">${circleLabel}</div>
                    <div class="tl-body">
                        <div class="tl-head">
                            <h4 class="tl-title">${item.title}</h4>
                            ${tagLabel}
                        </div>
                        <p class="tl-desc">${item.desc.replace(/\\n/g, '<br>')}</p>
                    </div>
                `;
                timelineBox.appendChild(dayBlock);
            });
        }

        if (inclusionsList) {
            inclusionsList.innerHTML = '';
            modeData.inclusions.forEach(inc => {
                const li = document.createElement('li');
                li.innerText = inc;
                inclusionsList.appendChild(li);
            });
        }

        if (exclusionsList) {
            exclusionsList.innerHTML = '';
            modeData.exclusions.forEach(exc => {
                const li = document.createElement('li');
                li.innerText = exc;
                exclusionsList.appendChild(li);
            });
        }
    }

    updateTourDisplay('car');

    const bookingForm = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
            submitBtn.innerText = 'Routing to Curator...';
            submitBtn.disabled = true;

            const data = {
                _subject: `New Grand Holidays Booking: Himachal Exotic Tour`,
                name: document.getElementById('b-name').value,
                email: document.getElementById('b-email').value,
                mobile: document.getElementById('b-mobile').value,
                preferredDate: document.getElementById('b-date').value,
                guestsCount: document.getElementById('b-travelers').value,
                message: document.getElementById('b-notes').value,
                estimatedPrice: document.getElementById('summary-price-display').innerText
            };

            fetch("https://formsubmit.co/ajax/mail@godwinhotels.com", {
                method: "POST",
                headers: { 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(() => {
                bookingForm.style.display = 'none';
                bookingSuccess.style.display = 'flex';
            })
            .catch(err => {
                console.error(err);
                submitBtn.innerText = 'Error. Try Again.';
                submitBtn.disabled = false;
            });
        });
    }
});"""

with open('himachal-exotic-tour.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update index.html and all-tours.html to include the new card
dropdown_link = '                          <a href="himachal-exotic-tour.html" class="dropdown-item">Himachal Exotic Tour</a>\n'
new_card = """
                <!-- Card: Himachal Exotic Tour -->
                <div class="journey-card reveal reveal-delay-2">
                    <div class="card-img-container">
                        <img src="assets/himachal_exotic.png" alt="Himachal Exotic Tour" class="journey-img">
                        <div class="card-badge">Himalayan Escape</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">6 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Delhi · Shimla · Manali</span>
                        </div>
                        <h3 class="card-title">Himachal Exotic Tour</h3>
                        <p class="card-text">Escape to the magnificent Himalayas! Explore the beautiful pine forests and snow-capped peaks of Shimla and Manali.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Explore Kufri & Solang Valley</li>
                            <li>Delhi City Tour included</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="himachal-exotic-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

def add_card_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_html = f.read()
    
    # Add to dropdown (after Rajasthan Desert Adventure)
    file_html = re.sub(r'(<a href="rajasthan-desert-adventure.html" class="dropdown-item">Rajasthan Desert Adventure</a>)', r'\1\n' + dropdown_link, file_html)
    
    # Add card (after Rajasthan Desert Adventure card)
    desert_card_end = r'(<h3 class="card-title">Rajasthan Desert Adventure</h3>.*?<a href="rajasthan-desert-adventure.html" class="btn btn-outline btn-sm">View.*?\n.*?</div>\s*</div>\s*</div>)'
    file_html = re.sub(desert_card_end, r'\1' + '\n' + new_card, file_html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_html)

add_card_to_file('index.html')
add_card_to_file('all-tours.html')
