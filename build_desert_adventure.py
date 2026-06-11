import re
import shutil
import os
import glob

# Copy the generated image
image_files = glob.glob(r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9\desert_adventure_*.png")
if image_files:
    shutil.copy2(image_files[0], r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets\desert_adventure.png")

with open('marvellous-marwar-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace HTML specific fields
html = html.replace('Marvellous Marwar Tour (04 Nights 05 Days)', 'Rajasthan Desert Adventure Tour (04 Nights 05 Days)')
html = html.replace('Marvellous Marwar Tour covering Jodhpur, Bikaner, and Jaisalmer', 'Rajasthan Desert Adventure Tour exploring Jodhpur and Jaisalmer')
html = html.replace('marvellous-marwar-tour.html', 'rajasthan-desert-adventure.html')
html = html.replace('marvellous-marwar-tour.js', 'rajasthan-desert-adventure.js')
html = html.replace('Marvellous Marwar Tour Banner', 'Rajasthan Desert Adventure Banner')
html = html.replace('Marvellous Marwar Tour', 'Rajasthan Desert Adventure')
html = html.replace('assets/mehrangarh_fort.png', 'assets/desert_adventure.png')
html = html.replace('Jodhpur - Bikaner - Jaisalmer', 'Jodhpur - Jaisalmer')
html = html.replace('New Grand Holidays Booking: Marvellous Marwar Tour', 'New Grand Holidays Booking: Rajasthan Desert Adventure Tour')

# Map specific replacements
html = html.replace('Marvellous Marwar Route', 'Rajasthan Desert Adventure Route')
html = html.replace('A magnificent loop traversing through the Blue City, the royal dunes of Bikaner, and the Golden Sands of Jaisalmer.', 'An unforgettable desert odyssey connecting the majestic Blue City with the Golden Sands of Jaisalmer.')

# Replace map path (Jodhpur 500,350 to Jaisalmer 120,280 and back)
old_path = r'<path id="route-path" d="M500,350 L340,100 L120,280 L500,350" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">'
new_path = r'<path id="route-path" d="M500,350 L120,280 L500,350" fill="none" stroke="#a67c31" stroke-width="3" stroke-dasharray="10,8" stroke-linecap="round" opacity="0.9">'
html = html.replace(old_path, new_path)

# Remove Bikaner from SVG
bikaner_svg = r'<!-- Bikaner \(340, 100\) -->\s*<g>\s*<circle cx="340" cy="100" r="12" fill="#a67c31" stroke="#fff" stroke-width="3" filter="url\(#pinShadow\)"\/>\s*<text x="340" y="80" text-anchor="middle" font-family="Outfit,sans-serif" font-size="11" font-weight="800" fill="#6b4c12" letter-spacing="1">BIKANER<\/text>\s*<\/g>'
html = re.sub(bikaner_svg, '', html, flags=re.DOTALL)

# Replace map distance badges (Only Jodhpur <-> Jaisalmer)
old_badges = r'<!-- Distance Badges -->.*?<!-- TOUR STARTS / ENDS -->'

new_badges = """<!-- Distance Badges -->
                        <!-- Jodhpur to Jaisalmer -->
                        <g transform="translate(310,315)">
                            <rect x="-44" y="-16" width="88" height="32" rx="16" fill="#1a1208" opacity="0.88"/>
                            <text x="0" y="-2" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10" font-weight="700" fill="#f0c060">285 km</text>
                            <text x="0" y="11" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" fill="rgba(255,220,120,0.75)">~5 hrs drive</text>
                        </g>

                        <!-- TOUR STARTS / ENDS -->"""
html = re.sub(old_badges, new_badges, html, flags=re.DOTALL)

# Update the City Cards under the map
old_city_cards = r'<div class="gt-city-cards">.*?<div class="gt-city-card">.*?03</div>.*?</div>\s*</div>'

new_city_cards = """<div class="gt-city-cards">
                    <div class="gt-city-card">
                        <div class="city-card-num">01</div>
                        <div class="city-card-icon">&#127984;</div>
                        <h3 class="city-card-name">Jodhpur</h3>
                        <p class="city-card-desc">The Blue City &mdash; guarded by the majestic Mehrangarh Fort. A mesmerizing sea of blue houses in the Thar.</p>
                        <div class="city-card-tags"><span>Mehrangarh Fort</span><span>Jaswant Thada</span><span>Umaid Bhawan</span></div>
                    </div>
                    <div class="gt-city-card">
                        <div class="city-card-num">02</div>
                        <div class="city-card-icon">&#127964;</div>
                        <h3 class="city-card-name">Jaisalmer</h3>
                        <p class="city-card-desc">The Golden City &mdash; rising from the desert sands. Famous for its living fort, intricate havelis and Sam Sand Dunes.</p>
                        <div class="city-card-tags"><span>Golden Fort</span><span>Patwon ki Haveli</span><span>Sand Dunes</span></div>
                    </div>
                </div>"""
html = re.sub(old_city_cards, new_city_cards, html, flags=re.DOTALL)

# Add Hotel Table and Vehicle Information below Inclusions/Exclusions
hotel_table_html = """
                    <!-- Accommodation & Vehicle Info -->
                    <div class="detail-block glass-card" style="margin-top: 2rem;">
                        <h2 class="block-title">Accommodation Options</h2>
                        <div style="overflow-x:auto;">
                            <table style="width:100%; border-collapse: collapse; margin-top: 1rem; font-family: 'Outfit', sans-serif; font-size: 0.9rem; text-align: left; background: #FFFEFB; border: 1px solid rgba(166,124,49,0.2);">
                                <thead>
                                    <tr style="background: rgba(166,124,49,0.08); color: #A67C31;">
                                        <th style="padding: 1rem; border-bottom: 2px solid rgba(166,124,49,0.2);">Destinations</th>
                                        <th style="padding: 1rem; border-bottom: 2px solid rgba(166,124,49,0.2);">3 Star Option</th>
                                        <th style="padding: 1rem; border-bottom: 2px solid rgba(166,124,49,0.2);">4 Star Option</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom: 1px solid rgba(0,0,0,0.05);">
                                        <td style="padding: 1rem; font-weight: 600; color: #6B5F54;">Jaisalmer Hotel (1N)</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Dewki Niwas / Chandragan / Jaisalmer Resort / Similar</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Desert Tulip / Sairafort / Similar</td>
                                    </tr>
                                    <tr style="border-bottom: 1px solid rgba(0,0,0,0.05);">
                                        <td style="padding: 1rem; font-weight: 600; color: #6B5F54;">Jaisalmer Camp (1N)</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Desert Adventure Camp / Similar</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Wind Desert Camp / Similar</td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 1rem; font-weight: 600; color: #6B5F54;">Jodhpur (2N)</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Kuchaman Haveli / Similar</td>
                                        <td style="padding: 1rem; color: #6B5F54;">Sri Ram Empire / Zone By The Park / Similar</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        
                        <h2 class="block-title" style="margin-top: 2rem;">Vehicle Configurations</h2>
                        <ul class="ie-list" style="margin-top: 1rem;">
                            <li><strong>2 – 3 person + 1 child:</strong> Swift Dzire or similar (as per itinerary and timing only).</li>
                            <li><strong>4 – 6 person:</strong> Xylo / Innova / Scorpio or similar (as per itinerary and timing only).</li>
                        </ul>
                    </div>
"""

# Insert the new table just before the right column closing tag
html = html.replace('</div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->', hotel_table_html + '\n                </div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->')


with open('rajasthan-desert-adventure.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now generate JS file
js_content = """document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Jodhpur - Jaisalmer",
            price: "On Request",
            shortDesc: "The Rajasthan Desert Adventure Tour is an experience that lets you explore the vibrant cities of Jodhpur and Jaisalmer, featuring heritage forts and an overnight luxury camp in the Sam Sand Dunes.",
            highlight: "🚗 Includes dedicated premium A/C transport, daily breakfast, and complete assistance throughout the tour.",
            itinerary: [
                { day: 1, title: "Jodhpur Station / Airport – Jaisalmer (285 Km / 5 hrs)", desc: "Meet & Greet on arrival at Jodhpur Railway Station / Airport & transfer to Jaisalmer. Enroute visit Jaisalmer War Museum – The Jaisalmer War Museum is located 10 km short of Jaisalmer on the Jaisalmer – Jodhpur Highway. The unique museum has been designed with the view of honouring the contributions and sacrifices of war heroes, and to highlight their bravery. It also traces the evolution of the Indian Army. On arrival Check-in to hotel. Overnight stay at Jaisalmer." },
                { day: 2, title: "Jaisalmer Sightseeing & Sand Dunes", desc: "After breakfast visit the Jaisalmer Fort which is made by unique Golden Lime stone, that’s why its known as Golden Fort or Sonar Kella. After that visit Patwon-ki-haveli, Nathmal-ki-haveli, Salim singh-ki-Haveli. People still live in these ancient buildings dating from 12th to 15th century. After that also visit Gadishar Lake. In evening proceed for camel ride on Sam Sand Dunes & you can experience the spectacular view of Sun set in Thar desert.\\n\\nPackage Includes:\\n• Traditional welcome with Aarti Tikka\\n• Welcome Drink (Non-Alcoholic) On Arrival\\n• One Camel Safari in the evening (Two pax each camel)\\n• Evening Bonfire with cultural program & veg. snacks\\n• Buffet Dinner & Buffet Breakfast (Fixed Menu)\\n\\nOvernight stay at Camp." },
                { day: 3, title: "Jaisalmer – Jodhpur (285 Km / 5 hrs)", desc: "After breakfast transfer to Jodhpur. On arrival check-in to your hotel. Overnight stay at Jodhpur." },
                { day: 4, title: "Jodhpur Local Sightseeing", desc: "After breakfast start for Jodhpur city tour. Covering Umaid Bhawan Palace Museum, Mehrangarh Fort- situated on a low sandstone hill. Within the fort visit Moti Mahal and Phool Mahal. Also visit Jaswant Thada – an imposing marble cenotaph built in memory of Maharaja Jaswant Singh II around 1899, Kaylana Lake and Mandore Garden. Evening free for leisure. Overnight stay at Jodhpur." },
                { day: 5, title: "Hotel – Jodhpur Railway Station / Airport", desc: "After breakfast check out from hotel and transfer to Jodhpur Railway Station / Airport for your onward journey." }
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
                _subject: `New Grand Holidays Booking: Rajasthan Desert Adventure Tour`,
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

with open('rajasthan-desert-adventure.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# 1. Add to dropdown
dropdown_link = '                          <a href="rajasthan-desert-adventure.html" class="dropdown-item">Rajasthan Desert Adventure</a>\n'
index_html = re.sub(r'(<a href="marvellous-marwar-tour.html" class="dropdown-item">Marvellous Marwar Tour</a>)', r'\1\n' + dropdown_link, index_html)

# 2. Add card after Marvellous Marwar Tour
new_card = """
                <!-- Card X: Rajasthan Desert Adventure -->
                <div class="journey-card reveal reveal-delay-2">
                    <div class="card-img-container">
                        <img src="assets/desert_adventure.png" alt="Rajasthan Desert Adventure" class="journey-img">
                        <div class="card-badge">Desert Safari</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">5 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Jodhpur · Jaisalmer</span>
                        </div>
                        <h3 class="card-title">Rajasthan Desert Adventure</h3>
                        <p class="card-text">Explore the vibrant Blue City of Jodhpur and enjoy an overnight luxury camp and camel safari in the Sam Sand Dunes of Jaisalmer.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Luxury Camp Stay</li>
                            <li>Sunset Camel Safari</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="rajasthan-desert-adventure.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

marwar_card_end = r'(<h3 class="card-title">Marvellous Marwar Tour</h3>.*?<a href="marvellous-marwar-tour.html" class="btn btn-outline btn-sm">View.*?\n.*?</div>\s*</div>\s*</div>)'
index_html = re.sub(marwar_card_end, r'\1' + '\n' + new_card, index_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
