document.addEventListener('DOMContentLoaded', () => {
    // Delhi Sightseeing Curation Database
    const tourModes = {
        pax2: {
            duration: "8 Hours / 80 Km",
            cities: "Old & New Delhi",
            price: "₹15,000 Total",
            shortDesc: "Immerse yourself in Delhi's historical heritage at a relaxed, customized pace. Perfect for couples or solo travelers who desire a tailored private tour of Delhi staying at Hotel Godwin Deluxe, with a premium AC Sedan, a dedicated guide, and flexible itinerary pacing.",
            highlight: "🚗 Includes 1 night stay at Hotel Godwin Deluxe, gourmet breakfast in the Indian Grill Restaurant, private pickup & drop-off at Hotel Godwin Deluxe, private AC Sedan (Maruti Dzire or Toyota Etios), dedicated licensed English-speaking historian guide, traditional rickshaw ride in Chandni Chowk, mineral water, and all toll/parking fees.",
            itinerary: [
                { time: "08:00 AM", title: "Breakfast at Indian Grill Restaurant", desc: "Enjoy a delicious complimentary breakfast at the Indian Grill Restaurant inside Hotel Godwin Deluxe before embarking on your tour." },
                { time: "09:00 AM", title: "Pickup from Hotel Godwin Deluxe", desc: "Your private chauffeur and expert guide greet you at the lobby of Hotel Godwin Deluxe to begin your sightseeing circuit in a premium AC Sedan." },
                { time: "09:30 AM", title: "Jama Masjid Exploration", desc: "Visit India's largest mosque, built by Emperor Shah Jahan. Gaze at the grand sandstone courtyard and white marble domes with your guide." },
                { time: "10:30 AM", title: "Chandni Chowk Rickshaw Ride", desc: "Embark on an interactive rickshaw ride through the vibrant, narrow streets of the ancient Mughal market, soaking in the heritage sights." },
                { time: "11:30 AM", title: "Spice Market (Khari Baoli)", desc: "Walk through Asia's largest wholesale spice market. Smell the rich aromas and view local spice merchants trading heritage spices." },
                { time: "12:30 PM", title: "Red Fort (Lal Qila) photo-stop", desc: "Stop at the outer ramparts of the spectacular Red Fort for professional photos and a brief historical overview from your guide." },
                { time: "01:15 PM", title: "Curated Boutique Lunch", desc: "Enjoy a traditional multi-course lunch at a premium, handpicked boutique restaurant in Delhi (lunch not included in pricing)." },
                { time: "02:30 PM", title: "Raj Ghat & India Gate", desc: "Pay respects at Raj Ghat, the memorial of Mahatma Gandhi. Then, drive past Rashtrapati Bhavan (Presidential Palace) and stop at India Gate." },
                { time: "03:45 PM", title: "Humayun's Tomb", desc: "Tour the breathtaking red sandstone garden tomb of Emperor Humayun, a UNESCO World Heritage site and design precursor to the Taj Mahal." },
                { time: "04:45 PM", title: "Lotus Temple & Qutub Minar", desc: "View the modern lotus-shaped Baha'i temple, then explore the Qutub Minar complex, featuring the historic 12th-century brick minaret." },
                { time: "05:30 PM", title: "Drop-off at Hotel Godwin Deluxe", desc: "Your chauffeur transfers you back to Hotel Godwin Deluxe, concluding your curated sightseeing tour." }
            ],
            inclusions: [
                "1 Night luxury stay at Hotel Godwin Deluxe, Delhi",
                "Gourmet breakfast at the Indian Grill Restaurant (Hotel Godwin Deluxe)",
                "Private pickup and drop-off from/to Hotel Godwin Deluxe",
                "Private AC Sedan (Dzire / Etios) for 8 Hours / 80 Km",
                "Licensed English-speaking professional guide",
                "Bespoke rickshaw ride in Chandni Chowk",
                "Onboard mineral water and refreshments",
                "All city toll taxes, fuel, and parking fees"
            ],
            exclusions: [
                "Monument entry tickets and camera fees",
                "Lunch and personal dining expenses",
                "Customary tipping and gratuities"
            ]
        },
        pax4: {
            duration: "8 Hours / 80 Km",
            cities: "Old & New Delhi",
            price: "₹23,000 Total",
            shortDesc: "Tailored for families or small groups of friends seeking spacious comfort. Stay at Hotel Godwin Deluxe, enjoy a gourmet breakfast in the Indian Grill Restaurant, and travel together in a premium SUV (Toyota Innova Crysta) with your personal guide.",
            highlight: "🚘 Includes 1 night stay at Hotel Godwin Deluxe, gourmet breakfast in the Indian Grill Restaurant, private pickup & drop-off at Hotel Godwin Deluxe, premium Toyota Innova Crysta SUV, dedicated licensed guide, rickshaw ride, and all toll/parking fees.",
            itinerary: [
                { time: "08:00 AM", title: "Breakfast at Indian Grill Restaurant", desc: "Gather at the Indian Grill Restaurant in Hotel Godwin Deluxe for a complimentary gourmet breakfast spread to start your day." },
                { time: "09:00 AM", title: "Pickup from Hotel Godwin Deluxe", desc: "Your chauffeur collects your group from the lobby of Hotel Godwin Deluxe in a spacious Toyota Innova SUV." },
                { time: "09:30 AM", title: "Jama Masjid & Old Delhi", desc: "Explore the historic mosque of Shah Jahan, learning about its architectural marvels and Islamic heritage from your private guide." },
                { time: "10:30 AM", title: "Rickshaw Ride & Bazaars", desc: "Board private rickshaws to traverse the historic lanes of Chandni Chowk, exploring silver markets and textile bazaars." },
                { time: "11:30 AM", title: "Khari Baoli Spice Market", desc: "Climb to a vantage point overlooking the spice market to watch the hustle-bustle of the century-old dry fruit and spice trade." },
                { time: "12:30 PM", title: "Red Fort Heritage Stop", desc: "Marvel at the majestic Lahori Gate of Red Fort. Take group photos and hear stories of the Mughal court and British Raj." },
                { time: "01:15 PM", title: "Premium Family Dining", desc: "Pause for lunch at a high-end restaurant serving Mughlai or global cuisine in central Delhi (dining cost separate)." },
                { time: "02:30 PM", title: "Imperial Capital & India Gate", desc: "Explore the solemn Raj Ghat memorial, followed by a drive along Rajpath to view the Parliament House and a photo stop at India Gate." },
                { time: "03:45 PM", title: "Humayun's Garden Tomb", desc: "Explore the symmetrical Mughal gardens and Persian-influenced tomb architecture of Emperor Humayun with your guide." },
                { time: "04:45 PM", title: "Qutub Minar Heritage Complex", desc: "Marvel at the towering Qutub Minar, the iron pillar of Chandragupta II, and the ruins of ancient Delhi's first mosques." },
                { time: "05:30 PM", title: "Drop-off at Hotel Godwin Deluxe", desc: "Relax in your SUV as your driver drops you off back at Hotel Godwin Deluxe." }
            ],
            inclusions: [
                "1 Night luxury stay at Hotel Godwin Deluxe, Delhi",
                "Gourmet breakfast at the Indian Grill Restaurant (Hotel Godwin Deluxe)",
                "Private pickup and drop-off from/to Hotel Godwin Deluxe",
                "Premium Toyota Innova Crysta SUV for 8 Hours / 80 Km",
                "Licensed English-speaking professional guide",
                "Private rickshaw rides in Chandni Chowk",
                "Onboard mineral water and soft beverages",
                "All toll taxes, parking fees, and driver charges"
            ],
            exclusions: [
                "Monument entrance fees",
                "Lunch and dining charges",
                "Customary tipping and gratuities"
            ]
        },
        pax6: {
            duration: "8 Hours / 80 Km",
            cities: "Old & New Delhi",
            price: "₹32,000 Total",
            shortDesc: "Ideal for medium-sized families or corporate groups wishing to explore Delhi together in luxury. Includes hotel lodging, breakfast, private hotel pickup and drop-off, and a premium AC Minivan (Tempo Traveller).",
            highlight: "🚐 Includes 1 night stay at Hotel Godwin Deluxe, gourmet breakfast in the Indian Grill Restaurant, private pickup & drop-off at Hotel Godwin Deluxe, luxury AC Minivan, dedicated licensed guide, rickshaw ride, and all toll/parking fees.",
            itinerary: [
                { time: "08:00 AM", title: "Breakfast at Indian Grill Restaurant", desc: "Enjoy a multi-cuisine complimentary breakfast at the Indian Grill Restaurant inside Hotel Godwin Deluxe." },
                { time: "09:00 AM", title: "Pickup from Hotel Godwin Deluxe", desc: "Your group is picked up in a luxury AC Tempo Traveller from the lobby of Hotel Godwin Deluxe." },
                { time: "09:30 AM", title: "Mughal Heritage: Jama Masjid", desc: "Begin your tour at the historical mosque. Your guide leads your group through the massive gates and explains the structure." },
                { time: "10:30 AM", title: "Group Rickshaw Safari", desc: "Travel in a caravan of private rickshaws through Chandni Chowk's chaotic and fascinating historical avenues." },
                { time: "11:30 AM", title: "Spice Market Senses", desc: "Tour the spice market. Smell cardamom, chilies, and saffron, and learn about Delhi's ancient trade connections." },
                { time: "12:30 PM", title: "Red Fort Outer Courtyard", desc: "Gather for group photos in front of the Red Fort's iconic ramparts, learning about the Mughal emperors who ruled from here." },
                { time: "01:15 PM", title: "Bespoke Group Lunch", desc: "Enjoy lunch at a selected premium restaurant, offering group-style seating and curated menus (meals not included)." },
                { time: "02:30 PM", title: "Imperial Delhi Drive", desc: "Visit Raj Ghat. Enjoy a slow drive past the Parliament House, Secretariat, and Rashtrapati Bhavan, ending with a stop at India Gate." },
                { time: "03:45 PM", title: "Humayun's Garden Tomb", desc: "Tour the manicured gardens and water channels surrounding the tomb, learning about the transition of Mughal design." },
                { time: "04:45 PM", title: "Lotus Temple & Qutub Minar", desc: "Admire the Lotus Temple's architecture, then head to Qutub Minar, tracing the earliest Islamic rulers of India." },
                { time: "05:30 PM", title: "Drop-off at Hotel Godwin Deluxe", desc: "Enjoy a comfortable transfer back to Hotel Godwin Deluxe, concluding your memorable day." }
            ],
            inclusions: [
                "1 Night luxury stay at Hotel Godwin Deluxe, Delhi",
                "Gourmet breakfast at the Indian Grill Restaurant (Hotel Godwin Deluxe)",
                "Private pickup and drop-off from/to Hotel Godwin Deluxe",
                "Luxury 9/12-Seater AC Tempo Traveller for 8 Hours / 80 Km",
                "Licensed English-speaking professional guide",
                "Private rickshaw rides in Chandni Chowk",
                "Onboard bottled mineral water, juices, and light snacks",
                "All city toll taxes, driver charges, and parking fees"
            ],
            exclusions: [
                "Monument entry tickets",
                "Lunch and personal purchases",
                "Tipping and gratuities for guide/driver"
            ]
        },
        pax10: {
            duration: "8 Hours / 80 Km",
            cities: "Old & New Delhi",
            price: "₹45,000 Total",
            shortDesc: "Our signature package for larger groups or corporate delegations. Includes lodging at Hotel Godwin Deluxe, breakfast at the Indian Grill Restaurant, private pickup and drop-off, a premium AC Mini-Coach, and dedicated coordinators.",
            highlight: "🚌 Includes 1 night stay at Hotel Godwin Deluxe, gourmet breakfast in the Indian Grill Restaurant, private pickup & drop-off at Hotel Godwin Deluxe, luxury AC Mini-Coach, licensed guide, and tour coordinator.",
            itinerary: [
                { time: "08:00 AM", title: "Breakfast at Indian Grill Restaurant", desc: "Enjoy a premium breakfast spread at the Indian Grill Restaurant in Hotel Godwin Deluxe before boarding." },
                { time: "09:00 AM", title: "Pickup from Hotel Godwin Deluxe", desc: "Board your luxury 15-seater AC Mini-Coach directly at the entrance of Hotel Godwin Deluxe, greeted by your tour coordinator." },
                { time: "09:30 AM", title: "Old Delhi Heritage Tour", desc: "Arrive at Jama Masjid. Your coordinator manages priority entry while your guide leads the group through the historical mosque." },
                { time: "10:30 AM", title: "Group Rickshaw Caravan", desc: "Embark on a coordinated rickshaw ride through Chandni Chowk, taking in the antique lanes and heritage structures." },
                { time: "11:30 AM", title: "Spice Market Group Walk", desc: "Visit Khari Baoli spice market, exploring the historical trade lanes with your guide and coordinator ensuring group comfort." },
                { time: "12:30 PM", title: "Red Fort Photo Curation", desc: "Stop at the Red Fort. Enjoy a structured group photo session with the historic fort walls in the background." },
                { time: "01:15 PM", title: "Curated Group Lunch", desc: "Dine at a premium boutique restaurant with pre-arranged group seating and a curated culinary experience (meals separate)." },
                { time: "02:30 PM", title: "Imperial Vistas & India Gate", desc: "Visit Raj Ghat. Enjoy a scenic drive past Rashtrapati Bhavan and the Parliament House, with a scheduled stop at India Gate." },
                { time: "03:45 PM", title: "Humayun's Garden Tomb", desc: "Tour the garden mausoleum. Your guide explains the geometric symmetry of the gardens while the coordinator handles group access." },
                { time: "04:45 PM", title: "Qutub Minar & Lotus Temple", desc: "Photograph the Lotus Temple. Tour the Qutub Minar complex, witnessing the historical iron pillar and towering brick minaret." },
                { time: "05:30 PM", title: "Drop-off at Hotel Godwin Deluxe", desc: "Return in your private Mini-Coach for a coordinated drop-off back at Hotel Godwin Deluxe, completing a seamless journey." }
            ],
            inclusions: [
                "1 Night luxury stay at Hotel Godwin Deluxe, Delhi",
                "Gourmet breakfast at the Indian Grill Restaurant (Hotel Godwin Deluxe)",
                "Private pickup and drop-off from/to Hotel Godwin Deluxe",
                "Luxury AC Mini-Coach (15-Seater) for 8 Hours / 80 Km",
                "Licensed English-speaking professional guide",
                "Dedicated tour coordinator to manage group flow",
                "Coordinated rickshaw rides in Chandni Chowk",
                "Onboard mineral water, soft drinks, juices, and premium snacks",
                "All toll taxes, priority monument parking, and driver fees"
            ],
            exclusions: [
                "Monument entry tickets",
                "Lunch and dining expenses",
                "Tipping and gratuities"
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
    const travelersSelect = document.getElementById('b-travelers');

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
            const stepBlock = document.createElement('div');
            stepBlock.className = 'timeline-day-block';

            const stepNum = idx + 1;
            const circleLabel = stepNum;
            const tagLabel = `<span class="day-tag time-tag">${item.time}</span>`;

            stepBlock.innerHTML = `
                <div class="tl-circle">${circleLabel}</div>
                <div class="tl-body">
                    <div class="tl-head">
                        <h4 class="tl-title">${item.title}</h4>
                        ${tagLabel}
                    </div>
                    <p class="tl-desc">${item.desc}</p>
                </div>
            `;
            timelineBox.appendChild(stepBlock);
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

        // Sync booking form dropdown with tab
        const selectMap = {
            pax2: '2',
            pax4: '4',
            pax6: '6',
            pax10: '10'
        };
        if (travelersSelect.value !== selectMap[modeKey]) {
            travelersSelect.value = selectMap[modeKey];
        }
    }

    // Tab Event Listeners
    tabButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
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

    // Form Select Dropdown Event Listener (Sync Back to Tabs)
    travelersSelect.addEventListener('change', (e) => {
        const val = e.target.value;
        const modeMap = {
            '2': 'pax2',
            '4': 'pax4',
            '6': 'pax6',
            '10': 'pax10'
        };
        const targetMode = modeMap[val];
        if (targetMode) {
            // Click the corresponding tab button
            const targetBtn = document.querySelector(`.mode-tab-btn[data-mode="${targetMode}"]`);
            if (targetBtn) {
                targetBtn.click();
            }
        }
    });

    // Initialize display with default 'pax2' mode
    updateTourDisplay('pax2');

    // Sidebar Booking Form Handler
    
    

const bookingForm = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
        submitBtn.innerText = 'Routing to Curator...';
        submitBtn.disabled = true;

        const data = {
            _subject: `New Grand Holidays Booking: Delhi Local Sightseeing (${document.getElementById('selected-tour-mode').value.toUpperCase()})`,
            name: document.getElementById('b-name').value,
            email: document.getElementById('b-email').value,
            _cc: document.getElementById('b-email').value,
                mobile: document.getElementById('b-mobile').value,
            preferredDate: document.getElementById('b-date').value,
            guestsCount: document.getElementById('b-travelers').value,
                        message: document.getElementById('b-notes').value,
            estimatedPrice: document.getElementById('summary-price-display').innerText
        };

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
            document.querySelectorAll('.faq-question.open').forEach(other => {
                if (other !== btn) {
                    other.classList.remove('open');
                    other.setAttribute('aria-expanded', 'false');
                    other.nextElementSibling.classList.remove('open');
                }
            });
            btn.classList.toggle('open', !isOpen);
            btn.setAttribute('aria-expanded', String(!isOpen));
            answer.classList.toggle('open', !isOpen);
        });
    });
});
