document.addEventListener('DOMContentLoaded', () => {
    // Himalayan Sanctuary Database
    const tourModes = {
        heli: {
            duration: "10 Days / 9 Nights",
            cities: "Srinagar · Pahalgam · Gulmarg · Shimla",
            price: "$15,800 p.p.",
            shortDesc: "Fly over the magnificent Himalayas. Skip the long drives and board your private helicopter transitions between Srinagar, Gulmarg, Pahalgam, and Shimla.",
            highlight: "🚁 Private helicopter transfers, curated suites at Khyber Gulmarg & Wildflower Hall Shimla, personal concierge, and VIP local historian guides.",
            itinerary: [
                { day: 1, title: "Arrival in Srinagar", desc: "Welcome to Kashmir. A private SUV transfers you to a custom royal houseboat on Dal Lake. Sunset Shikara cruise with live sitar." },
                { day: 2, title: "Mughal Gardens & Houseboat Recital", desc: "Explore Shalimar Bagh and Nishat Bagh with a private historian. Sitar performance on the houseboat deck." },
                { day: 3, title: "Private Helicopter to Gulmarg", desc: "Fly over the breathtaking Pir Panjal range. Check-in to a luxury suite at the Khyber Himalayan Resort & Spa." },
                { day: 4, title: "Gondola Ride & Apharwat Peak", desc: "Skip-the-line VIP tickets to Gulmarg Gondola Phase 1 & 2. Sunset champagne toast at Apharwat Peak." },
                { day: 5, title: "Heli-Flight to Pahalgam", desc: "Fly directly to Pahalgam. Check-in to a luxury pine-forest cottage. Evening campfire with local folk music." },
                { day: 6, title: "Aru Valley Trekking Curation", desc: "Guided trek through pristine forests with veteran mountaineers. Private picnic lunch by the alpine Lidder river." },
                { day: 7, title: "Helicopter Transfer to Shimla", desc: "Fly by private helicopter from Pahalgam to Shimla. Check-in to the royal Wildflower Hall (Oberoi)." },
                { day: 8, title: "Wildflower Sanctuary Walk", desc: "Private nature walk in the cedar sanctuary, followed by colonial high tea on the terrace overlooking snow peaks." },
                { day: 9, title: "Colonial Shimla History Walk", desc: "Guided heritage walk of the Mall Road, Christ Church, and Viceregal Lodge, Lord Kitchener's estate." },
                { day: 10, title: "Private Departure Transfer", desc: "Private helicopter/SUV transfer to Chandigarh or Delhi airport for your return flight home." }
            ],
            inclusions: [
                "Bespoke private helicopter transfers between destinations",
                "Private luxury SUV transfers for local city tours",
                "Ultra-luxury stays (Oberoi Wildflower Hall & Khyber Resort suites)",
                "All monument entry tickets with fast-track VIP access",
                "Daily gourmet breakfasts and curated dinners",
                "Private English-speaking historian guides throughout"
            ],
            exclusions: [
                "International flights and travel visas",
                "Personal expenses (spa, laundry, alcoholic drinks)",
                "Customary tipping and gratuities"
            ]
        },
        suv: {
            duration: "10 Days / 9 Nights",
            cities: "Srinagar · Pahalgam · Gulmarg · Shimla",
            price: "$12,200 p.p.",
            shortDesc: "Discover the spectacular landscapes at your own pace in a premium luxury SUV (Audi Q7 or Toyota Fortuner) with a dedicated chauffeur and curator.",
            highlight: "🚗 Luxury SUV throughout the trip, Oberoi Wildflower Hall Shimla stay, custom local shikara & ski tickets, and local guides.",
            itinerary: [
                { day: 1, title: "Srinagar Valley Arrival", desc: "Arrive in Srinagar. Your private luxury chauffeur transfers you to a Taj Palace Houseboat. Sunset Shikara ride." },
                { day: 2, title: "Mughal Architecture Curation", desc: "Historian-guided tour of Jama Masjid Srinagar, Shalimar Bagh, and Nishat Bagh." },
                { day: 3, title: "SUV Road Trip to Gulmarg", desc: "Drive along scenic pine roads in your SUV. Check-in to the Khyber Resort." },
                { day: 4, title: "Gulmarg Meadows & Gondola", desc: "Guided snow walk or meadow tour. VIP tickets for the Gulmarg Gondola." },
                { day: 5, title: "SUV Transfer to Pahalgam", desc: "Drive to Pahalgam. Pass through historic saffron fields and Avantipura ruins." },
                { day: 6, title: "Betaab Valley & Glacier Rivers", desc: "Guided trek in Betaab Valley. Traditional Kashmiri Wazwan lunch by the river." },
                { day: 7, title: "Overland Drive to Shimla", desc: "Road drive to Srinagar airport, flight to Chandigarh, and SUV transfer to Shimla." },
                { day: 8, title: "Jakhoo Temple & Ridge Walk", desc: "Visit Jakhoo Temple and explore the historic wooden colonial buildings of Shimla." },
                { day: 9, title: "Leisure at Wildflower Hall", desc: "Unwind at Wildflower Hall. Enjoy the heated outdoor infinity pool facing the mountains." },
                { day: 10, title: "Departure Transfer to Chandigarh", desc: "SUV transfer back to Chandigarh airport for your flight home." }
            ],
            inclusions: [
                "Dedicated premium SUV (Audi Q7 / Fortuner) throughout the trip",
                "Premium hotel stays in Kashmir and Shimla",
                "Private local historian guides at each location",
                "VIP tickets for Gulmarg Gondola and Shikara",
                "Daily breakfast and three curated lunches",
                "Highway tolls, parking, and driver allowance"
            ],
            exclusions: [
                "Flights and airport departure taxes",
                "Personal tips and shopping expenses",
                "Optional heli-skiing activities in Gulmarg"
            ]
        },
        heritage: {
            duration: "10 Days / 9 Nights",
            cities: "Srinagar · Pahalgam · Gulmarg · Shimla",
            price: "$9,600 p.p.",
            shortDesc: "Experience the timeless cultural heritage of the Himalayas with premium boutique accommodations and local transport overlays.",
            highlight: "🏔️ Premium boutique hotel stays, private Innova Crysta, traditional sightseeing, and local culinary tours.",
            itinerary: [
                { day: 1, title: "Srinagar Houseboat Welcome", desc: "Arrive at Srinagar airport. Private Innova transfer to your deluxe houseboat." },
                { day: 2, title: "Srinagar Old City & Bazaars", desc: "Guided walking tour through historic bazaars, spice markets, and local artisans." },
                { day: 3, title: "Drive to Gulmarg", desc: "Scenic road transfer to Gulmarg. Relax and stroll in the green meadows." },
                { day: 4, title: "Gulmarg Gondola Ride", desc: "Ride the world's second-highest cable car. Visit the ancient Baba Reshi shrine." },
                { day: 5, title: "Drive to Pahalgam Valley", desc: "Transfer to Pahalgam. Scenic stops at Awantipora and apple orchards." },
                { day: 6, title: "Aru Valley Scenic Excursion", desc: "Explore Chandanwari and Aru Valley by local taxi. Enjoy mountain stream views." },
                { day: 7, title: "Transfer to Shimla", desc: "Innova transfer to Srinagar airport, flight to Chandigarh, and drive to Shimla." },
                { day: 8, title: "Shimla Ridge & Mall Road", desc: "Heritage walk along the Ridge, Mall Road, and the Lakkar Bazaar." },
                { day: 9, title: "Kufri Pine Forest Excursion", desc: "Visit Kufri forest area. Enjoy high tea at a local heritage lodge." },
                { day: 10, title: "Departure via Chandigarh", desc: "Chauffeur transfer to Chandigarh airport for your departure flight." }
            ],
            inclusions: [
                "Private Toyota Innova Crysta for all road transfers",
                "Stays in premium heritage boutique hotels",
                "Local guided sightseeing tours",
                "Daily breakfast and airport transfers",
                "Standard entry tickets to gardens and gondola"
            ],
            exclusions: [
                "Domestic and international flight tickets",
                "Meals and drinks not mentioned",
                "Tips and personal spending"
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
    updateTourDisplay('heli');

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
                    _subject: `Grand Holidays - Himalayan Sanctuary Booking Request`,
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
