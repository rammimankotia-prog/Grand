import re
import shutil
import glob
import os

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\tiger_tour_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\tiger_tour.png")

with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace HTML specific fields
html = html.replace('Himachal Exotic Tour (05 Nights 06 Days)', 'Tiger Tour With Jaipur (04 Nights 05 Days)')
html = html.replace('Himachal Exotic Tour exploring the breathtaking hill stations of Shimla and Manali', 'Tiger Tour With Jaipur - Explore the remarkable Pink City and the Royal Bengal Tigers of Ranthambore.')
html = html.replace('himachal-exotic-tour.html', 'tiger-tour-jaipur.html')
html = html.replace('himachal-exotic-tour.js', 'tiger-tour-jaipur.js')
html = html.replace('Himachal Exotic Tour Banner', 'Tiger Tour Banner')
html = html.replace('Himachal Exotic Tour', 'Tiger Tour With Jaipur')
html = html.replace('assets/himachal_exotic.png', 'assets/tiger_tour.png')
html = html.replace('Delhi - Shimla - Manali', 'Jaipur - Ranthambore')
html = html.replace('New Grand Holidays Booking: Himachal Exotic Tour', 'New Grand Holidays Booking: Tiger Tour With Jaipur')

# Map specific replacements
html = html.replace('Himachal Exotic Route', 'Tiger Tour Route')
html = html.replace('A mesmerizing journey from the historic capital of Delhi up into the majestic, snow-capped peaks of the Himalayas.', 'A spectacular journey combining the rich grandeur of the Pink City with the diverse wildlife of Ranthambore.')

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
                        <path id="route-path" d="M250,180 L400,320 L250,180" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">
                             <animate attributeName="stroke-dashoffset" from="0" to="-200" dur="5s" repeatCount="indefinite"/>
                        </path>

                        <!-- Moving Taxi Sedan along route -->
                        <g>
                            <animateMotion dur="10s" repeatCount="indefinite" rotate="auto">
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
                        <g transform="translate(350,220)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">280 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~6 hrs drive</text>
                        </g>

                        <!-- TOUR STARTS / ENDS -->
                        <g transform="translate(250, 180)">
                            <rect x="-70" y="-60" width="140" height="20" rx="10" fill="#c59b3f" stroke="#fff" stroke-width="1.5" filter="url(#labelShadow)"/>
                            <text x="0" y="-47" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS / ENDS</text>
                            
                            <rect x="-40" y="-37" width="80" height="14" rx="4" fill="#1a1208"/>
                            <text x="0" y="-27" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">Day 1 &amp; Day 5</text>
                        </g>

                        <!-- Jaipur (250, 180) -->
                        <g>
                            <circle cx="250" cy="180" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="250" y="205" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JAIPUR</text>
                        </g>

                        <!-- Ranthambore (400, 320) -->
                        <g>
                            <circle cx="400" cy="320" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="400" y="345" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">RANTHAMBORE</text>
                        </g>
                    </svg>"""

old_svg_pattern = r'<svg viewBox="0 0 680 480".*?</svg>'
html = re.sub(old_svg_pattern, new_svg, html, flags=re.DOTALL)

# Update the City Cards under the map
old_city_cards = r'<div class="gt-city-cards">.*?<div class="gt-city-card">.*?02</div>.*?</div>\s*</div>'

new_city_cards = """<div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127984;</div>
                        <h3 class="city-card-name">Jaipur</h3>
                        <p class="city-card-desc">The magnificent Pink City, famous for its royal palaces, the stunning Hawa Mahal, and the majestic hilltop Amber Fort.</p>
                        <div class="city-card-tags"><span>Amber Fort</span><span>Hawa Mahal</span><span>City Palace</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#128005;</div>
                        <h3 class="city-card-name">Ranthambore</h3>
                        <p class="city-card-desc">One of the largest and most renowned national parks in Northern India, famously known for its thriving Royal Bengal Tiger population.</p>
                        <div class="city-card-tags"><span>Tiger Safari</span><span>Wildlife</span><span>Nature Trails</span></div>
                    </div>
                </div>"""
html = re.sub(old_city_cards, new_city_cards, html, flags=re.DOTALL)

# Update FAQs
new_faq = """<div class="faq-grid" id="faq-grid-gt">
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">What is the best time to visit Ranthambore for tiger sightings?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Ranthambore National Park is open from October to June. The best time for tiger sightings is during the warmer months (April to June) when tigers frequent the watering holes, though November to March offers much more pleasant weather for the overall trip.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Are the safari tickets guaranteed?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Safari tickets are subject to availability and the forest department's quotas. However, our curators handle all advanced bookings to secure your spots on the shared coach/jeep safaris. We recommend booking well in advance.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Is this tour suitable for children?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Absolutely! The blend of exploring magnificent forts in Jaipur and the thrilling wildlife safari in Ranthambore makes this an incredibly engaging and educational trip for families and children.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">What is included in the package?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>The package includes premium AC car transportation, hotel accommodations with daily breakfast, airport/railway station assistance, and a 24-hour helpline. Guide fees, monument entrances, and safari charges are excluded to give you flexibility.</p></div></div>
                </div>
            </div>"""

html = re.sub(r'<div class="faq-grid" id="faq-grid-gt">.*?</section>', new_faq + '\n        </section>', html, flags=re.DOTALL)

with open('tiger-tour-jaipur.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now generate JS file with simplified human-readable itinerary
js_content = """document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Jaipur - Ranthambore",
            price: "On Request",
            shortDesc: "Experience the ultimate contrast of Rajasthan: the royal grandeur of Jaipur's palaces and the thrilling wilderness of Ranthambore, home to the magnificent Royal Bengal Tiger.",
            highlight: "🐅 Includes private premium A/C transport, comfortable hotel stays, and daily breakfast.",
            itinerary: [
                { day: 1, title: "Welcome to the Pink City!", desc: "Your royal adventure begins today! Upon arriving at the Jaipur airport or railway station, our friendly representative will greet you and drive you to your hotel in a private luxury car. After checking in, the rest of the evening is entirely yours to relax and settle in." },
                { day: 2, title: "Exploring the Royal Wonders of Jaipur", desc: "After a delicious breakfast, get ready for a full day of sightseeing in the beautiful Pink City. We will visit the majestic Amber Fort perched on a hill, stop by the iconic honeycomb-patterned Hawa Mahal (Palace of Winds) for some amazing photos, and explore the ancient Jantar Mantar observatory and the grand City Palace. In the evening, you can relax or shop for vibrant local handicrafts." },
                { day: 3, title: "Journey to the Tiger's Domain", desc: "We start early today with breakfast before hitting the road for Ranthambore (approx. 280 kms, a scenic 6-hour drive). Ranthambore is world-famous for its incredible tiger population! Upon arrival, you'll check into your comfortable hotel and spend the evening relaxing and preparing for tomorrow's big adventure." },
                { day: 4, title: "Thrilling Ranthambore Wildlife Safari", desc: "Wake up early for an unforgettable morning! You'll embark on an exciting wildlife safari deep into the Ranthambore National Park in a shared coach. Keep your eyes peeled for the majestic Royal Bengal Tigers, leopards, and a rich variety of birds and wildlife. After the thrilling safari, the rest of the day is yours to relax at the hotel and soak in the natural surroundings." },
                { day: 5, title: "Farewell & Departure", desc: "Enjoy your final breakfast of the trip. We will then provide a comfortable transfer back to the Jaipur Airport or Railway Station for your onward journey. Your holiday concludes here, leaving you with incredible memories of palaces and tigers. See you again soon!" }
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
                _subject: `New Grand Holidays Booking: Tiger Tour With Jaipur`,
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

with open('tiger-tour-jaipur.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update index.html and all-tours.html to include the new card
dropdown_link = '                          <a href="tiger-tour-jaipur.html" class="dropdown-item">Tiger Tour With Jaipur</a>\n'
new_card = """
                <!-- Card: Tiger Tour With Jaipur -->
                <div class="journey-card reveal reveal-delay-3">
                    <div class="card-img-container">
                        <img src="assets/tiger_tour.png" alt="Tiger Tour With Jaipur" class="journey-img">
                        <div class="card-badge">Wildlife & Heritage</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">5 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Jaipur · Ranthambore</span>
                        </div>
                        <h3 class="card-title">Tiger Tour With Jaipur</h3>
                        <p class="card-text">Explore the magnificent palaces of the Pink City and discover the diverse wildlife of the royal Bengal tigers in Ranthambore.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Early Morning Jungle Safari</li>
                            <li>Jaipur City Tour included</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="tiger-tour-jaipur.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

def add_card_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_html = f.read()
    
    # Add to dropdown (after Himachal Exotic Tour)
    file_html = re.sub(r'(<a href="himachal-exotic-tour.html" class="dropdown-item">Himachal Exotic Tour</a>)', r'\1\n' + dropdown_link, file_html)
    
    # Add card (after Himachal Exotic Tour card)
    card_end = r'(<h3 class="card-title">Himachal Exotic Tour</h3>.*?<a href="himachal-exotic-tour.html" class="btn btn-outline btn-sm">View.*?\n.*?</div>\s*</div>\s*</div>)'
    file_html = re.sub(card_end, r'\1' + '\n' + new_card, file_html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_html)

add_card_to_file('index.html')
add_card_to_file('all-tours.html')
