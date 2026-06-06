document.addEventListener('DOMContentLoaded', () => {
    // Tour Options Database
    const tourModes = {
        car: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$12,500 p.p.",
            shortDesc: "Witness the crown jewels of North Indian heritage in a private chauffeur-driven car. This itinerary offers a relaxed, customizable pace with scenic highway drives and palace stopovers, allowing you to absorb India's beauty at your own leisure.",
            highlight: "🚗 Includes a dedicated private car with personal driver, mobile Wi-Fi, refreshments, and fast-track highway toll clearances throughout your trip.",
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
            price: "$8,500 p.p.",
            shortDesc: "Explore the Golden Triangle in a private air-conditioned taxi with an experienced local driver-guide. A cost-effective yet comfortable option allowing you to stop at scenic viewpoints, local markets, and heritage villages along the way.",
            highlight: "🚕 Includes a private A/C taxi with knowledgeable driver-guide, flexible pit stops, mineral water, and full itinerary coverage at your preferred pace.",
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
            duration: "7 Days / 6 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$15,800 p.p.",
            shortDesc: "The best of both worlds — private car transfers for scenic highway stretches combined with domestic flight segments to save time between key cities. Enjoy the flexibility of road travel and the speed of air for maximum comfort.",
            highlight: "🚘✈️ Includes private car transfers Delhi-Agra + domestic IndiGo/Vistara flight Agra-Jaipur, airport lounge access, and a personal travel coordinator throughout.",
            itinerary: [
                { day: 1, title: "Delhi Arrival & Private Car to Agra", desc: "Arrive in Delhi. Your private car departs for Agra via the Yamuna Expressway. Check-in to Oberoi Amarvilas with views of the Taj Mahal." },
                { day: 2, title: "Sunrise Taj Mahal & Agra Fort", desc: "Beat the crowds with a private guided sunrise visit to the Taj Mahal. Explore Agra Fort, the red sandstone Mughal citadel, in the afternoon." },
                { day: 3, title: "Domestic Flight: Agra to Jaipur", desc: "Drive to Agra Airport and board a domestic flight to Jaipur. Transfer to the Rambagh Palace upon arrival. Evening at leisure in the Pink City." },
                { day: 4, title: "Royal Jaipur Exploration", desc: "Explore Amber Fort, Hawa Mahal, and the City Palace with a private guide. Attend a sunset cultural show at Nahargarh Fort." },
                { day: 5, title: "Jaipur Artisan Heritage Day", desc: "Morning block-printing workshop and local bazaar exploration. Afternoon at leisure or optional Jal Mahal photo tour." },
                { day: 6, title: "Jaipur to Delhi by Car", desc: "Scenic drive back to Delhi via NH48. Sightseeing en route at Neemrana Fort. Check-in to your Delhi hotel for the final night." },
                { day: 7, title: "Delhi Departure", desc: "Private transfer to Delhi International Airport for your onward flight home." }
            ],
            inclusions: [
                "Private A/C car transfers (Delhi-Agra and Jaipur-Delhi)",
                "Domestic flight: Agra to Jaipur (economy or business class)",
                "Airport transfers and lounge access at Agra Airport",
                "Luxury accommodation in 5-star properties",
                "Daily breakfasts and two curated palace dinners",
                "Personal guide and VIP monument access"
            ],
            exclusions: [
                "International airfare and visa fees",
                "Meals not specified in the itinerary",
                "Personal shopping and gratuities"
            ]
        },
        sameday: {
            duration: "1 Day (14 Hours)",
            cities: "Delhi - Agra - Delhi",
            price: "$3,200 p.p.",
            shortDesc: "Short on time? This same-day car journey whisks you from Delhi to Agra and back in a private air-conditioned car. Visit the Taj Mahal, Agra Fort, and enjoy a memorable royal lunch — all in one unforgettable day.",
            highlight: "🚗 Private A/C car on the Yamuna Expressway, personal guide at Taj Mahal and Agra Fort, and a curated lunch — back in Delhi by evening.",
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
        modeData.itinerary.forEach((item, idx) => {
            const dayBlock = document.createElement('div');
            dayBlock.className = 'timeline-day-block';

            // For same-day tours use step number, for multi-day tours use Day X
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
        submitBtn.innerText = 'Routing to Curator...';
        submitBtn.disabled = true;

        const data = {
            _subject: `New Grand Holidays Booking: Golden Triangle (${document.getElementById('selected-tour-mode').value.toUpperCase()})`,
            name: document.getElementById('b-name').value,
            email: document.getElementById('b-email').value,
            preferredDate: document.getElementById('b-date').value,
            guestsCount: document.getElementById('b-travelers').value,
            message: document.getElementById('b-notes').value,
            estimatedPrice: document.getElementById('summary-price-display').innerText
        };

        fetch("https://formsubmit.co/ajax/book@godwinhotels.com", {
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
});
