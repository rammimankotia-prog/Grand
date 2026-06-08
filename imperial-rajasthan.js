document.addEventListener('DOMContentLoaded', () => {
    // Rajasthan Retold Database
    const tourModes = {
        suv: {
            duration: "9 Days / 8 Nights",
            cities: "Jodhpur · Jaisalmer · Udaipur",
            price: "$14,200 (For 2 Adults)",
            shortDesc: "Explore the royal forts and glistening lakes of Rajasthan in a private luxury SUV (Toyota Innova Crysta or Fortuner) with a dedicated chauffeur-guide.",
            highlight: "🚗 Private luxury chauffeur SUV throughout, stays at Umaid Bhawan Palace & Taj Lake Palace, lake cruises, and historic city guides.",
            itinerary: [
                { day: 1, title: "Arrival in Jodhpur", desc: "Welcome to the Blue City. Your private chauffeur transfers you in a luxury SUV to the majestic Umaid Bhawan Palace." },
                { day: 2, title: "Mehrangarh Fort & Bazaars", desc: "Curator-led private tour of Mehrangarh Fort. Ziplining over the desert ramparts and a guided walk through the old city bazaars." },
                { day: 3, title: "Overland SUV Drive to Jaisalmer", desc: "Drive across the Thar Desert in your premium SUV. Check-in to the luxury desert camp at Sujan The Serai." },
                { day: 4, title: "Dune Safari & Desert Stargazing", desc: "Camel safari in Sam Sand Dunes, sunset champagne, folk music around the bonfire, and premium desert stargazing." },
                { day: 5, title: "Jaisalmer Living Fort", desc: "Guided walk of the golden sandstone Jaisalmer Fort and the ornate Patwon ki Haveli, capturing ancient architecture." },
                { day: 6, title: "Scenic Road Trip to Udaipur", desc: "Chauffeur drive to Udaipur. Check-in to the legendary Taj Lake Palace, floating on the calm waters of Lake Pichola." },
                { day: 7, title: "City Palace & Yacht Cruise", desc: "Guided tour of Udaipur City Palace and crystal gallery. Sunset private yacht cruise on Lake Pichola." },
                { day: 8, title: "Monsoon Palace & Vintage Cars", desc: "Visit Sajjangarh Monsoon Palace at sunset. Explore the Maharana's royal vintage car collection." },
                { day: 9, title: "Udaipur Departure", desc: "Private SUV transfer to Udaipur Airport for your departure flight." }
            ],
            inclusions: [
                "Dedicated premium SUV (Fortuner / Innova) throughout the itinerary",
                "Private local historian guides at all cities",
                "Heritage palace hotel stays (Umaid Bhawan & Taj Lake Palace)",
                "Daily gourmet breakfasts and three curated palace dinners",
                "VIP fast-track monument entries",
                "Private yacht cruise on Lake Pichola"
            ],
            exclusions: [
                "International flights and travel visas",
                "Personal expenses (spa, laundry, alcoholic drinks)",
                "Customary tipping and gratuities"
            ]
        },
        charter: {
            duration: "9 Days / 8 Nights",
            cities: "Jodhpur · Jaisalmer · Udaipur",
            price: "$19,500 (For 2 Adults)",
            shortDesc: "Unrivaled heritage style. Drive between heritage palace destinations in a private luxury SUV (Audi Q7 or Mercedes GLE) and stay in historical grand suites.",
            highlight: "🚗 Premium luxury SUV (Audi Q7 / Mercedes GLE) throughout, stay in historical Grand Palace Suites, vintage car transfers, and private curator guides.",
            itinerary: [
                { day: 1, title: "Arrival in Jodhpur", desc: "Welcome to Jodhpur. Your private chauffeur transfers you in a luxury Audi Q7 or Mercedes SUV to the grand Umaid Bhawan Palace royal suite." },
                { day: 2, title: "Royal Early-Access Fort Tour", desc: "Private early-access tour of Mehrangarh Fort with the personal curator. Evening polo grounds dining." },
                { day: 3, title: "Scenic Road Journey to Jaisalmer", desc: "Road trip across the desert dunes in your premium luxury SUV. Check-in to Sujan The Serai camp." },
                { day: 4, title: "Thar Dunes & Astronomer Stargazing", desc: "Desert dunes safari, champagne sunset, private astronomer-guided stargazing using high-end telescopes." },
                { day: 5, title: "Living Fort Royal Chambers", desc: "Exclusive inside tour of Jaisalmer Fort's private royal chambers and local sandstone art workshops." },
                { day: 6, title: "SUV Road Transfer to Udaipur", desc: "Scenic road transfer in your luxury SUV to Udaipur. Royal welcome and check-in to Taj Lake Palace grand suite." },
                { day: 7, title: "Private City Palace & Royal Barge", desc: "Curator-guided tour of Udaipur City Palace. Sunset cruise on a royal historical barge with live classical music." },
                { day: 8, title: "Sajjangarh High Tea", desc: "Private champagne high tea at Sajjangarh Monsoon Palace overlooking the Aravali Hills." },
                { day: 9, title: "Udaipur Departure", desc: "Private luxury SUV transfer to Udaipur Airport for your departure flight." }
            ],
            inclusions: [
                "Private luxury SUV (Audi Q7 / Mercedes GLE) for all road transfers",
                "Stays in Grand Royal Suites at premium palace properties",
                "Private historian/curator guides at all locations",
                "All monument entry tickets with fast-track VIP access",
                "All meals and premium beverages included",
                "Sunset barge cruise on Lake Pichola"
            ],
            exclusions: [
                "Flights and airport departure taxes",
                "Personal shopping expenses",
                "Customary tipping"
            ]
        },
        express: {
            duration: "9 Days / 8 Nights",
            cities: "Jodhpur · Jaisalmer · Udaipur",
            price: "$11,500 (For 2 Adults)",
            shortDesc: "Experience the timeless cultural heritage of Rajasthan with stays in handpicked boutique Havelis and private Sedan transport.",
            highlight: "🏠 Stays in boutique heritage Havelis, private Sedan transport (Toyota Etios/Dzire), guided sightseeing, and local cultural tours.",
            itinerary: [
                { day: 1, title: "Jodhpur Arrival", desc: "Welcome to Jodhpur. Chauffeur Sedan transfer to Taj Hari Mahal hotel. Rest and unpack." },
                { day: 2, title: "Forts & Jaswant Thada", desc: "Guided tour of Mehrangarh Fort, Jaswant Thada cenotaph, and local spice markets." },
                { day: 3, title: "Road Drive to Jaisalmer", desc: "Scenic road transfer in your private Sedan to Jaisalmer. Check-in to a boutique desert haveli." },
                { day: 4, title: "Camel Safari & Bonfire", desc: "Dune safari, sunset cultural dance, traditional desert dinner under the open sky." },
                { day: 5, title: "Havelis of Jaisalmer", desc: "Walking tour of Jaisalmer Fort and the historic architectural havelis." },
                { day: 6, title: "Drive to Udaipur", desc: "Road transfer in your Sedan to Udaipur. Check-in to Raas Devigarh or boutique haveli." },
                { day: 7, title: "City Palace & Lake Boat Tour", desc: "City Palace museum tour, Jagdish Temple, and group boat ride on Lake Pichola." },
                { day: 8, title: "Eklingji & Nagda Temples", desc: "Excursion to the 10th-century Eklingji and Nagda temples with a private guide." },
                { day: 9, title: "Departure from Udaipur", desc: "Chauffeur transfer to Udaipur Airport for your departure flight." }
            ],
            inclusions: [
                "Private Sedan (Toyota Etios / Maruti Dzire) for all road transfers",
                "Stays in premium boutique heritage Havelis",
                "Local guided sightseeing and entrance tickets",
                "Daily breakfast and airport transfers",
                "Shared boat cruise on Lake Pichola"
            ],
            exclusions: [
                "Flights and airport departure taxes",
                "Personal tips and shopping expenses",
                "Optional custom excursions"
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
        modeData.itinerary.forEach(item => {
            const row = document.createElement('div');
            row.className = 'tl-row';
            row.innerHTML = `
                <div class="tl-circle">${item.day}</div>
                <div class="tl-body">
                    <div class="tl-head">
                        <span class="day-tag">Day ${item.day}</span>
                        <h4 class="tl-title">${item.title}</h4>
                    </div>
                    <p class="tl-desc">${item.desc}</p>
                </div>
            `;
            timelineBox.appendChild(row);
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

    // Set Initial Load
    updateTourDisplay('suv');

    // Tab Event Listeners
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            updateTourDisplay(btn.getAttribute('data-mode'));
        });
    });

    // Mobile Navigation Toggle
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.querySelector('.nav-menu');
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // Dropdown toggle for mobile viewports
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const navDropdown = document.querySelector('.nav-dropdown');
    if (dropdownToggle && navDropdown) {
        dropdownToggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                navDropdown.classList.toggle('active');
            }
        });
    }

    // Handle Form Booking Request
    const bookingForm = document.getElementById('tourBookingForm');
    const successMessage = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const name = document.getElementById('b-name').value;
            const email = document.getElementById('b-email').value;
            const date = document.getElementById('b-date').value;
            const guests = document.getElementById('b-travelers').value;
            const notes = document.getElementById('b-notes').value;
            const mode = selectedModeInput.value;

            const submitUrl = "https://formsubmit.co/ajax/mail@godwinhotels.com";

            fetch(submitUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    _subject: `Grand Holidays - Imperial Rajasthan Booking Request`,
                    Name: name,
                    Email: email,
                    Preferred_Date: date,
                    Guests: guests,
                    Selected_Mode: mode,
                    Additional_Notes: notes
                })
            })
            .then(response => response.json())
            .then(data => {
                bookingForm.style.display = 'none';
                successMessage.style.display = 'flex';
            })
            .catch(error => {
                console.error("Booking submit error: ", error);
                // Graceful fallback display
                bookingForm.style.display = 'none';
                successMessage.innerHTML = `<h3>Request Submitted</h3><p>Your details were routed to our curator team. We will connect with you shortly.</p>`;
                successMessage.style.display = 'flex';
            });
        });
    }
});
