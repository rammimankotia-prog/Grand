document.addEventListener('DOMContentLoaded', () => {
    // Tour Options Database
    const tourModes = {
        car: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$12,500 p.p.",
            shortDesc: "Witness the crown jewels of North Indian heritage in a private chauffeur-driven luxury SUV. This itinerary offers a relaxed, customizable pace with scenic highway drives and palace stopovers, allowing you to absorb India's beauty at your own leisure.",
            highlight: "🚙 Includes a dedicated Mercedes-Benz V-Class SUV with personal chauffeur, mobile Wi-Fi, refreshments, and fast-track highway toll clearances throughout your trip.",
            itinerary: [
                { day: 1, title: "Welcome to Delhi", desc: "Arrive in Delhi where a private chauffeur greets you. Transfer in a Mercedes V-Class to your luxury hotel (The Leela Palace/The Lodhi) for a welcome dinner." },
                { day: 2, title: "Imperial Delhi Curation", desc: "Explore Delhi's contrast. Discover Humayun's Tomb, Qutub Minar, and embark on a private rickshaw ride through the ancient spice markets of Chandni Chowk." },
                { day: 3, title: "Scenic Drive to Agra", desc: "Drive along the Yamuna Expressway in your luxury SUV. Check-in to the Oberoi Amarvilas, where every room features an uninterrupted view of the Taj Mahal." },
                { day: 4, title: "Agra Sunrise & Artisan Heritage", desc: "Beat the crowds with a sunrise visit to the Taj Mahal. Explore the red sandstone ramparts of Agra Fort, followed by a private workshop with direct descendants of the Taj's original marble inlay artisans." },
                { day: 5, title: " फतेहपुर सीकरी to Jaipur", desc: "Drive to Jaipur. Stop en route at the ancient Mughal capital of Fatehpur Sikri and the deep stepwells of Abhaneri. Check-in to the royal Rambagh Palace." },
                { day: 6, title: "The Royal Jaipur Experience", desc: "Ascend Amber Fort in luxury. Visit the wind-kissed screen of Hawa Mahal, and explore the City Palace, including access to the Maharaja's private chambers." },
                { day: 7, title: "Hidden Artisans of Rajasthan", desc: "Participate in a private block-printing workshop, learn Rajasthan blue pottery, and enjoy sunset champagne drinks overlooking the city at Nahargarh Fort." },
                { day: 8, title: "Chauffeur Drive Return to Delhi", desc: "Relax in your SUV as you drive back to Delhi. A private transfer takes you straight to the Delhi Airport for your departure." }
            ],
            inclusions: [
                "Dedicated Mercedes-Benz V-Class SUV throughout the tour",
                "Private English-speaking historian guides at all cities",
                "Luxury accommodation in 5-star Heritage Palaces (Oberoi/Taj)",
                "Daily gourmet breakfasts and three curated palace dinners",
                "All monument entry tickets with fast-track VIP access",
                "Bottled water, refreshments, and mobile Wi-Fi in SUV"
            ],
            exclusions: [
                "International flights and travel visas",
                "Personal expenses (spa, laundry, alcoholic drinks)",
                "Customary tipping and gratuities"
            ]
        },
        train: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$11,800 p.p.",
            shortDesc: "Experience India's iconic rail network in absolute comfort. Bypassing road traffic, you will ride on board express trains in executive coaches, enjoying priority boarding, lounge access, and a unique look at rural Indian landscapes.",
            highlight: "🚂 Includes Executive Coach reservations on the Gatimaan Express and Shatabdi Express, private VIP station porter services, and executive lounge access.",
            itinerary: [
                { day: 1, title: "Arrival in the Capital", desc: "Welcome to Delhi. Private luxury transfer to your hotel. Unwind and enjoy a bespoke briefing of your upcoming rail holiday." },
                { day: 2, title: "Delhi Heritage Tour", desc: "Tour Delhi's primary historical points. Visit the Lotus Temple, India Gate, and the Mughal-era Red Fort with your private guide." },
                { day: 3, title: "Express Rail to Agra", desc: "Board the Gatimaan Express in the Executive Lounge. Enjoy a 100-minute high-speed journey to Agra. Check-in to your resort and tour the Agra Fort." },
                { day: 4, title: "Taj Mahal & local Craft Curation", desc: "Enjoy a guided sunrise tour of the Taj Mahal. Spend the afternoon discovering Agra's traditional leather and marble carving industries." },
                { day: 5, title: "Shatabdi Express to Jaipur", desc: "Board the Shatabdi Express Executive Coach for a scenic train journey to Jaipur. Transfer to the Rambagh Palace upon arrival." },
                { day: 6, title: "Pink City Fortresses", desc: "Explore Jaipur's architectural wonders, including Amber Fort, Jantar Mantar (astronomical observatory), and the City Palace museum." },
                { day: 7, title: "Sitar & Sunset Jal Mahal", desc: "Take a private local food tasting tour and attend an exclusive private Sitar recital in a restored Rajasthani haveli." },
                { day: 8, title: "Return Train to Delhi", desc: "Board the evening Shatabdi Express back to Delhi. Transfer directly to Delhi airport for your onward flight." }
            ],
            inclusions: [
                "Executive class tickets on all express trains (Gatimaan/Shatabdi)",
                "Private local chauffeur transfers at each destination",
                "Dedicated porter service at all railway platforms",
                "Stays in premium heritage properties (Oberoi/Taj)",
                "VIP fast-track monument entries",
                "Curated private local city guides"
            ],
            exclusions: [
                "Meals not mentioned in the itinerary",
                "Gratuities and personal purchases",
                "Optional hot air balloon rides in Jaipur"
            ]
        },
        flight: {
            duration: "6 Days / 5 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$19,500 p.p.",
            shortDesc: "The ultimate luxury aviation tour. Bypassing roads and rails entirely, you will fly between Delhi, Agra, and Jaipur in private charter aircraft. Save hours of transit time and maximize your exploration of royal history.",
            highlight: "✈️ Includes private charter flights (Turbo-props/Light Jets) with VIP FBO terminal boarding, skipping commercial queues and road congestion entirely.",
            itinerary: [
                { day: 1, title: "Capital Arrival & Palace Check-in", desc: "Arrive in Delhi. Transfer via private chauffeur to the Leela Palace. Enjoy a private dinner and presentation by a heritage expert." },
                { day: 2, title: "Private Charter to Agra", desc: "Board your private charter aircraft. A short 25-minute flight takes you to Agra. Check-in to Oberoi Amarvilas. Discover Agra Fort and enjoy sunset Taj views." },
                { day: 3, title: "Sunrise Taj & Charter to Jaipur", desc: "Witness the Taj Mahal at sunrise. Late morning, fly via private charter to Jaipur. Transfer to the Rambagh Palace. Sunset drinks at the Palace gardens." },
                { day: 4, title: "Royal Jaipur Curated Tour", desc: "Take a private tour of Jaipur's heritage. Enjoy a royal lunch inside the private courtyards of the City Palace, hosted by a palace curator." },
                { day: 5, title: "Fly back to Delhi", desc: "Fly your private charter back to Delhi. Check-in to a luxury suite and enjoy a custom Indian culinary tasting dinner." },
                { day: 6, title: "Departure", desc: "Private transfer to Delhi Airport terminal for your international flight home." }
            ],
            inclusions: [
                "All flights via private luxury charter aircraft",
                "FBO airport terminal boarding (no security lines/delays)",
                "Premium Suite accommodations at Oberoi Amarvilas and Rambagh Palace",
                "All gourmet meals, including curated palace dinners and private chef menus",
                "Personal 24/7 tour curator traveling with you",
                "Skip-the-line VIP entries at all sights"
            ],
            exclusions: [
                "International commercial flights",
                "Visa processing fees",
                "Personal boutique purchases"
            ]
        },
        sameday: {
            duration: "1 Day (14 Hours)",
            cities: "Delhi - Agra - Delhi",
            price: "$4,500 p.p.",
            shortDesc: "Short on time but refuse to compromise on luxury? This high-speed 1-day express curation whisks you from Delhi to Agra in a premium chauffeur-driven Mercedes, offering private guided access to the Taj Mahal and royal dining.",
            highlight: "⚡ Yamuna Expressway speed transfers in a luxury Mercedes Sedan/SUV, private historian guide, and royal dining at Oberoi Amarvilas.",
            itinerary: [
                { day: 1, time: "06:00 AM", title: "Luxury Chauffeur Pickup", desc: "Your chauffeur collects you from your Delhi hotel or airport in a Mercedes Sedan. Travel in comfort along the Yamuna Expressway." },
                { day: 1, time: "09:30 AM", title: "Taj Mahal Private Walk", desc: "Arrive in Agra. Meet your private historian guide and skip the queues to tour the Taj Mahal, learning about its history and architectural secrets." },
                { day: 1, time: "01:00 PM", title: "Royal Lunch at Oberoi", desc: "Enjoy a multi-course Indian culinary lunch at the Bellevue restaurant in the Oberoi Amarvilas, facing views of the Taj." },
                { day: 1, time: "02:30 PM", title: "Agra Fort Exploration", desc: "Discover Agra Fort, the spectacular red sandstone walled city of the Mughal Emperors, exploring its marble palaces and chambers." },
                { day: 1, time: "05:00 PM", title: "Sunset Taj View & Return", desc: "Catch the sunset reflections of the Taj Mahal across the Yamuna River from Mehtab Bagh. Begin your comfortable return drive to Delhi." },
                { day: 1, time: "08:30 PM", title: "Delhi Drop-off", desc: "Arrive back in Delhi. Your chauffeur drops you off directly at your hotel or the international airport terminal." }
            ],
            inclusions: [
                "Yamuna Expressway return transfers in a private Mercedes vehicle",
                "Private historian guide in Agra",
                "Skip-the-line VIP entry tickets to Taj Mahal and Agra Fort",
                "Multi-course royal lunch at the Oberoi Amarvilas",
                "Cold towels, snacks, and mineral water during transit"
            ],
            exclusions: [
                "Hotel lodging (None)",
                "Dinner in Delhi",
                "Tipping and camera tickets"
            ]
        }
    };

    // UI Elements
    const tabButtons = document.querySelectorAll('.mode-tab-btn');
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

    // Function to render active tour mode
    function updateTourDisplay(modeKey) {
        const modeData = tourModes[modeKey];
        if (!modeData) return;

        // Update basic strings
        displayDuration.innerText = modeData.duration;
        displayCities.innerText = modeData.cities;
        displayPrice.innerText = `From ${modeData.price}`;
        tourShortDesc.innerText = modeData.shortDesc;
        summaryPriceDisplay.innerText = `${modeData.price}`;
        selectedModeInput.value = modeKey;

        // Highlight box
        modeHighlightBox.innerText = modeData.highlight;

        // Render Timeline
        timelineBox.innerHTML = '';
        modeData.itinerary.forEach((item) => {
            const dayBlock = document.createElement('div');
            dayBlock.className = 'timeline-day-block';

            // Check if time is defined (e.g. for same day tour)
            const timeLabel = item.time ? `<span class="day-tag">${item.time}</span>` : `<span class="day-tag">Day ${item.day}</span>`;
            const dayCircleText = item.day ? item.day : '✦';

            dayBlock.innerHTML = `
                <div class="timeline-day-number">${dayCircleText}</div>
                <div class="timeline-day-title">
                    <h4>${item.title}</h4>
                    ${timeLabel}
                </div>
                <p class="timeline-day-desc">${item.desc}</p>
            `;
            timelineBox.appendChild(dayBlock);
        });

        // Render Inclusions
        inclusionsList.innerHTML = '';
        modeData.inclusions.forEach(inc => {
            const li = document.createElement('li');
            li.innerText = inc;
            inclusionsList.appendChild(li);
        });

        // Render Exclusions
        exclusionsList.innerHTML = '';
        modeData.exclusions.forEach(exc => {
            const li = document.createElement('li');
            li.innerText = exc;
            exclusionsList.appendChild(li);
        });
    }

    // Tab Event Listeners
    tabButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Find target button
            const targetBtn = e.target.closest('.mode-tab-btn');
            if (!targetBtn) return;

            // Remove active classes
            tabButtons.forEach(b => b.classList.remove('active'));
            // Add active class
            targetBtn.classList.add('active');

            // Get selected mode
            const mode = targetBtn.getAttribute('data-mode');
            updateTourDisplay(mode);
        });
    });

    // Initialize display with default 'car' mode
    updateTourDisplay('car');

    // Sidebar Booking Form Handler
    const bookingForm = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
        const originalText = submitBtn.innerText;
        submitBtn.innerText = 'Routing to Curator...';
        submitBtn.disabled = true;

        // Simulate API post
        setTimeout(() => {
            bookingForm.style.display = 'none';
            bookingSuccess.style.display = 'flex';
        }, 1800);
    });
});
