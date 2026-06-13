import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
js_file = os.path.join(repo_path, '4-days-golden-triangle-tour.js')
html_file = os.path.join(repo_path, '4-days-golden-triangle-tour.html')

# 1. Update HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('5 Days Golden Triangle Route', '4 Days Golden Triangle Route')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update JS
js_content = """document.addEventListener('DOMContentLoaded', () => {
    const tourData = {
        duration: "4 Days / 3 Nights",
        cities: "Delhi - Agra - Jaipur",
        price: "$190 p.p.",
        shortDesc: "Embark on an unforgettable 4-day private journey through India's famed Golden Triangle. Travel comfortably in a private, air-conditioned vehicle with expert local guides bringing history to life at every stop.",
        highlight: "✨ Includes a dedicated private car with personal driver, hotel pickups, and scenic highway drives between the major cities.",
        itinerary: [
            { day: 1, title: "The Magic of Delhi & Journey to Agra", desc: "Your adventure begins with a flexible morning pickup from anywhere in the Delhi NCR region. We dive straight into history at the towering Qutub Minar, followed by the peaceful, lotus-shaped Bahá'í House of Worship. Enjoy a scenic drive past the majestic Red Fort, India Gate, and the grand Parliament House. Uncover the mysteries of the ancient Agrasen Ki Baoli stepwell, and marvel at Humayun's Tomb, the inspiration for the Taj Mahal. After a delicious local lunch at Connaught Place, we’ll explore the vibrant chaos of Old Delhi—riding through the spice-scented lanes of Chandni Chowk, admiring the grand Jama Masjid, and visiting Asia's largest spice market, Khari Baoli. In the evening, relax on a comfortable drive to Agra, where you'll check into your hotel for the night." },
            { day: 2, title: "Sunrise at the Taj Mahal & The Road to the Pink City", desc: "Rise early for an unforgettable sunrise visit to the Taj Mahal. Watch the marble monument change colors in the morning light as your guide shares the timeless love story behind its creation. After breakfast at your hotel, we’ll explore the sprawling courtyards of the imposing Agra Fort. Next, visit the delicate Itmad-ud-Daulah, affectionately known as the \\"Baby Taj.\\" After savoring authentic Agra cuisine for lunch, you'll be driven comfortably to the vibrant \\"Pink City\\" of Jaipur to relax and spend the night." },
            { day: 3, title: "Royal Jaipur City Tour", desc: "After a hearty breakfast, begin your exploration of Jaipur's royal heritage. Start at the formidable Jaigarh Fort, perched high on the Aravalli hills and home to the world's largest wheeled cannon. Next, wander through the opulent City Palace, a dazzling blend of Rajasthani and Mughal architecture. Take a moment to photograph the serene Jal Mahal (Water Palace) floating in Man Sagar Lake, and admire the iconic Hawa Mahal (Palace of Winds), with its intricate lattice windows designed for royal ladies. Conclude your day of sightseeing at the Jantar Mantar observatory, a fascinating collection of giant astronomical instruments." },
            { day: 4, title: "Farewell and Departure", desc: "Enjoy your final morning in Rajasthan. Depending on your onward travel plans, your driver will either take you on a comfortable drive back to your requested drop-off point in Delhi, or provide a convenient drop-off at Jaipur Airport." }
        ],
        inclusions: [
            "Private air-conditioned vehicle",
            "Hotel pickup and drop-off",
            "English-speaking local guides",
            "3 nights accommodation (with breakfast)",
            "Bottled water"
        ],
        exclusions: [
            "Monument admission tickets (unless specifically requested)",
            "Meals (lunch/dinner)",
            "Gratuities"
        ]
    };

    // DOM Elements
    const els = {
        duration: document.getElementById('display-duration'),
        cities: document.getElementById('display-cities'),
        price: document.getElementById('display-price'),
        shortDesc: document.getElementById('tour-short-desc'),
        highlight: document.getElementById('mode-highlight-box'),
        itinerary: document.getElementById('itinerary-timeline-box'),
        inclusions: document.getElementById('inclusions-list'),
        exclusions: document.getElementById('exclusions-list')
    };

    function renderTour() {
        if(els.duration) els.duration.textContent = tourData.duration;
        if(els.cities) els.cities.textContent = tourData.cities;
        if(els.price) els.price.textContent = tourData.price;
        if(els.shortDesc) els.shortDesc.textContent = tourData.shortDesc;
        if(els.highlight) els.highlight.innerHTML = `<p>${tourData.highlight}</p>`;

        // Render Itinerary
        if(els.itinerary) {
            els.itinerary.innerHTML = tourData.itinerary.map(item => `
                <div class="timeline-day-block">
                    <div class="timeline-day-number">${item.day}</div>
                    <div class="timeline-day-title-wrapper">
                        <div class="timeline-day-title">
                            <span class="day-tag">Day ${item.day}</span>
                            <h4>${item.title}</h4>
                        </div>
                        <p class="timeline-day-desc">${item.desc}</p>
                    </div>
                </div>
            `).join('');
        }

        // Render Inclusions
        if(els.inclusions) {
            els.inclusions.innerHTML = tourData.inclusions.map(inc => `<li>✓ ${inc}</li>`).join('');
        }

        // Render Exclusions
        if(els.exclusions) {
            els.exclusions.innerHTML = tourData.exclusions.map(exc => `<li>✗ ${exc}</li>`).join('');
        }
    }

    renderTour();
});
"""

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Fixed HTML and JS IDs.")
