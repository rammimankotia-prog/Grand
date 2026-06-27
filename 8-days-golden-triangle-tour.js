document.addEventListener('DOMContentLoaded', () => {
    // Tour Options Database
    const tourModes = {
        car: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "₹83,000 per person",
            shortDesc: "Witness the crown jewels of North Indian heritage in a private chauffeur-driven car. This itinerary offers a relaxed, customizable pace with scenic highway drives and palace stopovers, allowing you to absorb India's beauty at your own leisure.",
            highlight: "🚗 Includes a dedicated private car with personal driver, mobile Wi-Fi, refreshments, and fast-track highway toll clearances throughout your trip.",
            itinerary: [
                { day: 1, title: "Arrival & Welcome to Delhi", desc: "Arrive at New Delhi International Airport where our representative will warmly welcome you. Transfer via private luxury car to Hotel Godwin Deluxe, your premium stay in the heart of the city. Spend the evening relaxing and acclimatizing to the vibrant energy of India." },
                { day: 2, title: "Delhi Sightseeing: Old & New", desc: "After a hearty breakfast at Hotel Godwin Deluxe, dive into Delhi's rich history. Explore the grand Jama Masjid, enjoy a thrilling rickshaw ride through Chandni Chowk, and visit the serene Rajghat. Later, marvel at the towering Qutub Minar and the magnificent Humayun's Tomb, before driving past the grand India Gate and Parliament House." },
                { day: 3, title: "Delhi to Agra: The City of Love", desc: "Enjoy a morning drive to Agra via the Yamuna Expressway. Upon arrival, check-in to your luxury hotel. In the afternoon, visit the imposing Agra Fort, a UNESCO World Heritage site showcasing spectacular Mughal architecture, followed by a sunset view of the Taj Mahal from Mehtab Bagh." },
                { day: 4, title: "Sunrise at Taj Mahal & Artisan Tour", desc: "Experience the ethereal beauty of the Taj Mahal at dawn. Return for breakfast, then explore the exquisite Tomb of I'timad-ud-Daulah, often called the 'Baby Taj'. Spend the evening visiting local marble inlay artisans whose ancestors built the Taj Mahal." },
                { day: 5, title: "Agra to Jaipur via Fatehpur Sikri", desc: "Depart for Jaipur, the famed Pink City. En route, explore the abandoned red sandstone city of Fatehpur Sikri, built by Emperor Akbar, and marvel at the stunning stepwell, Chand Baori, in Abhaneri village. Arrive in Jaipur and check into your royal heritage hotel." },
                { day: 6, title: "Jaipur Sightseeing & Royal Forts", desc: "Ascend the majestic Amber Fort via a royal elephant or jeep ride. Stop to photograph the breathtaking Jal Mahal sitting in Man Sagar Lake. Later, explore the intricate Hawa Mahal (Palace of Winds), the grand City Palace, and the astronomical wonders of Jantar Mantar." },
                { day: 7, title: "Cultural Immersion in the Pink City", desc: "Spend the morning visiting the historic Nahargarh Fort, offering panoramic views of Jaipur. Later, enjoy a guided heritage walk through the vibrant local bazaars famous for block printing, blue pottery, and exquisite jewelry. Enjoy a traditional Rajasthani dinner in the evening." },
                { day: 8, title: "Jaipur to Delhi & Departure", desc: "After breakfast, enjoy a scenic drive back to New Delhi. Upon arrival, depending on your flight schedule, you can do some last-minute shopping at Connaught Place or be transferred directly to the airport for your onward journey, bringing your Golden Triangle tour to a memorable close." }
            ],
            inclusions: [
                "Dedicated Toyota Innova throughout the tour",
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
            price: "₹85,000 per person",
            shortDesc: "Explore the Golden Triangle via executive class express trains combined with private local taxis at each destination. A comfortable, seamless rail option that skips highway traffic and lets you enjoy scenic views between Delhi, Agra, and Jaipur.",
            highlight: "🚆 Includes Executive Class tickets on high-speed Gatimaan & Shatabdi trains, private taxi transfers at destinations, dedicated porters, and guided sightseeing.",
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
            price: "₹158,000 per person",
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
            var origText = submitBtn ? submitBtn.innerText : 'Submit';
        submitBtn.innerText = 'Routing to Curator...';
        submitBtn.disabled = true;

        const data = {
            _subject: `New Grand Holidays Booking: Golden Triangle (${document.getElementById('selected-tour-mode').value.toUpperCase()})`,
            name: document.getElementById('b-name').value,
            email: document.getElementById('b-email').value,
            _cc: document.getElementById('b-email').value,
                mobile: document.getElementById('b-mobile').value,
            preferredDate: document.getElementById('b-date').value,
            guestsCount: document.getElementById('b-travelers').value,
            message: document.getElementById('b-notes').value,
            estimatedPrice: document.getElementById('summary-price-display').innerText
        };

            // ── Required-field validation ────────────────────────────
            var valName = document.getElementById('b-name') ? document.getElementById('b-name').value.trim() : '';
            var valEmail = document.getElementById('b-email') ? document.getElementById('b-email').value.trim() : '';
            var valMobile = document.getElementById('b-mobile') ? document.getElementById('b-mobile').value.trim() : '';
            var valDate = document.getElementById('b-date') ? document.getElementById('b-date').value : '';

            if (!valName || !valEmail || !valMobile || !valDate) {
                var missing = [];
                if (!valName)   missing.push('Full Name');
                if (!valEmail)  missing.push('Email Address');
                if (!valMobile) missing.push('Mobile Number');
                if (!valDate)   missing.push('Preferred Date');
                alert('Please fill in the required fields:\n\u2022 ' + missing.join('\n\u2022 '));
                if (typeof submitBtn !== 'undefined' && submitBtn) { 
                    submitBtn.innerText = (typeof origText !== 'undefined' ? origText : 'Send Reservation Request'); 
                    submitBtn.disabled = false; 
                }
                return;
            }
            // ────────────────────────────────────────────────────────
        fetch("submit-booking.php", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success || data.success === "true") {

            bookingForm.style.display = 'none';
            bookingSuccess.style.display = 'flex';
        
            } else {
                alert("Server Message: " + (data.message || "Email service requires activation. Please check tours@godwinhotels.com for an activation link."));
                const submitBtn = bookingForm.querySelector('button[type="submit"]') || bookingForm.querySelector('.btn-sidebar-submit');
                if (submitBtn) {
                    submitBtn.innerText = 'Submit Reservation Request';
                    submitBtn.disabled = false;
                }
            }
        })
        .catch(err => {
            console.error(err);
            submitBtn.innerText = 'Error. Try Again.';
            submitBtn.disabled = false;
        });
    });

    // Mobile Dropdown Menu Toggle
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = toggle.closest('.nav-dropdown');
                if (parent) {
                    parent.classList.toggle('active');
                }
            }
        });
    });

    // FAQ Accordion
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const answer = btn.nextElementSibling;
            const isOpen = btn.classList.contains('open');
            // Close all others
            document.querySelectorAll('.faq-question.open').forEach(other => {
                if (other !== btn) {
                    other.classList.remove('open');
                    other.setAttribute('aria-expanded', 'false');
                    other.nextElementSibling.classList.remove('open');
                }
            });
            // Toggle current
            btn.classList.toggle('open', !isOpen);
            btn.setAttribute('aria-expanded', String(!isOpen));
            answer.classList.toggle('open', !isOpen);
        });
    });
});
