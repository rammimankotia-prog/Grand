import re

with open('rajasthan-heritage-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace HTML specific fields
html = html.replace('Rajasthan Heritage Tour (07 Nights 08 Days)', 'Marvellous Marwar Tour (04 Nights 05 Days)')
html = html.replace('Rajasthan Heritage Tour covering Jaipur, Jodhpur, Jaisalmer, and Udaipur', 'Marvellous Marwar Tour covering Jodhpur, Bikaner, and Jaisalmer')
html = html.replace('rajasthan-heritage-tour.html', 'marvellous-marwar-tour.html')
html = html.replace('rajasthan-heritage-tour.js', 'marvellous-marwar-tour.js')
html = html.replace('Rajasthan Heritage Tour Banner', 'Marvellous Marwar Tour Banner')
html = html.replace('Rajasthan Heritage Tour', 'Marvellous Marwar Tour')
html = html.replace('8 Days / 7 Nights', '5 Days / 4 Nights')
html = html.replace('Jaipur - Jodhpur - Jaisalmer - Udaipur', 'Jodhpur - Bikaner - Jaisalmer')
html = html.replace('New Grand Holidays Booking: Rajasthan Heritage Tour', 'New Grand Holidays Booking: Marvellous Marwar Tour')

# Map specific replacements
# Replace Route title
html = html.replace('Rajasthan Heritage Route', 'Marvellous Marwar Route')
html = html.replace('A heritage loop traversing through the Pink City, the Blue City, the Golden Sands of Thar, and the romantic Lake Palace.', 'A magnificent loop traversing through the Blue City, the royal dunes of Bikaner, and the Golden Sands of Jaisalmer.')

# Replace map path
old_path = r'<path id="route-path" d="M480,160 Q400,190 320,220 Q240,200 160,180 Q240,200 320,220 Q380,290 440,360" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">'
new_path = r'<path id="route-path" d="M320,220 Q310,150 300,80 Q230,130 160,180 Q240,200 320,220" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">'
html = html.replace(old_path, new_path)

# Replace city nodes in SVG
old_cities_svg = r'<!-- Jaipur \(480, 160\) -->.*?<!-- Udaipur \(440, 360\) -->\s*<g>\s*<circle cx="440" cy="360" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url\(#pinShadow\)"/>\s*<text x="440" y="385" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">UDAIPUR</text>\s*</g>'

new_cities_svg = """<!-- Jodhpur (320, 220) -->
                        <g>
                            <circle cx="320" cy="220" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="320" y="245" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JODHPUR</text>
                        </g>

                        <!-- Bikaner (300, 80) -->
                        <g>
                            <circle cx="300" cy="80" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="300" y="60" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">BIKANER</text>
                        </g>

                        <!-- Jaisalmer (160, 180) -->
                        <g>
                            <circle cx="160" cy="180" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url(#pinShadow)"/>
                            <text x="160" y="160" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">JAISALMER</text>
                        </g>"""
html = re.sub(old_cities_svg, new_cities_svg, html, flags=re.DOTALL)

# Replace map distance badges
old_badges = r'<!-- Distance Badges -->.*?<!-- Jodhpur to Udaipur -->.*?~5 hrs drive</text>\s*</g>'

new_badges = """<!-- Distance Badges -->
                        <!-- Jodhpur to Bikaner -->
                        <g transform="translate(310,150)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">250 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~4.5 hrs drive</text>
                        </g>

                        <!-- Bikaner to Jaisalmer -->
                        <g transform="translate(230,130)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">330 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>

                        <!-- Jaisalmer to Jodhpur -->
                        <g transform="translate(240,200)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">285 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~4.5 hrs drive</text>
                        </g>"""
html = re.sub(old_badges, new_badges, html, flags=re.DOTALL)

# Update the City Cards under the map
old_city_cards = r'<div class="gt-city-cards">.*?<div class="gt-city-card">.*?04</div>.*?</div>\s*</div>'

new_city_cards = """<div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127984;</div>
                        <h3 class="city-card-name">Jodhpur</h3>
                        <p class="city-card-desc">The Blue City &mdash; guarded by the majestic Mehrangarh Fort. A mesmerizing sea of blue houses in the Thar.</p>
                        <div class="city-card-tags"><span>Mehrangarh Fort</span><span>Jaswant Thada</span><span>Mandore</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#128043;</div>
                        <h3 class="city-card-name">Bikaner</h3>
                        <p class="city-card-desc">The Camel Country &mdash; famous for its spectacular Junagarh Fort, red sandstone palaces and exotic camel farms.</p>
                        <div class="city-card-tags"><span>Junagarh Fort</span><span>Camel Farm</span><span>Lallgarh Palace</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">03</div>
                        <div class="city-card-icon">&#127964;</div>
                        <h3 class="city-card-name">Jaisalmer</h3>
                        <p class="city-card-desc">The Golden City &mdash; rising from the desert sands. Famous for its living fort, intricate havelis and Sam Sand Dunes.</p>
                        <div class="city-card-tags"><span>Jaisalmer Fort</span><span>Patwon ki Haveli</span><span>Sand Dunes</span></div>
                    </div>
                </div>"""
html = re.sub(old_city_cards, new_city_cards, html, flags=re.DOTALL)

with open('marvellous-marwar-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now generate JS file
js_content = """document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Jodhpur - Bikaner - Jaisalmer",
            price: "On Request",
            shortDesc: "Experience the Marvellous Marwar Tour. This journey takes you through the Blue City of Jodhpur, the royal dunes of Bikaner, and the Golden Sands of Jaisalmer.",
            highlight: "🚗 Includes dedicated premium A/C transport, daily breakfast, and complete assistance throughout the tour.",
            itinerary: [
                { day: 1, title: "Arrival Jodhpur - Bikaner ( 250 Kms )", desc: "Arrival at Jodhpur and drive to Bikaner. Upon arrival check in at hotel .Bikaner city of the best breed camels in the world. Visit the Camel Breeding farms, Junagarh Fort, Lallgarh Palace and Fort Museum. The magnificent palace is fabricated in red sandstone and marble is embellished with mirror work, exquisite carvings and paintings, definitely a worth visiting sight. Overnight at hotel." },
                { day: 2, title: "Bikaner - Sam ( 330 Kms )", desc: "After breakfast at your hotel check out and leave for Jaisalmer Golden City of Rajasthan the biggest state of India which is very close to Indo / Pak International border and proceed to Sam Dunes. Overnight stay at tent." },
                { day: 3, title: "Sam - Jaisalmer", desc: "After break fast check out and continue drive to Jaisalmer and check in at hotel and visit Fort, Palace museum, Jain temple, Patwon ki Haveli, Salim Singh ki Haveli, Nathmal ki haveli and Tazia tower and enjoy local market. Overnight at hotel." },
                { day: 4, title: "Jaisalmer - Jodhpur ( 285 Kms )", desc: "After breakfast check out and departure for onward journey to jodhpur upon arrival check in to hotel and proceed for city tour of jodhpur to Climb up the majestic Mehrangarh fort and explore the various sections within. Also visit the marble cenotaph at Jaswant Thada and visit Mandore Garden overnight at Hotel." },
                { day: 5, title: "Jodhpur Departure", desc: "After breakfast check out and drop at Airport to catch the flight for onwards destination. TOUR END with Sweet Memories." }
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
                        <p class="tl-desc">${item.desc}</p>
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
                _subject: `New Grand Holidays Booking: Marvellous Marwar Tour`,
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

with open('marvellous-marwar-tour.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
