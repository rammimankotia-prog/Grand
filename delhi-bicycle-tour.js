document.addEventListener('DOMContentLoaded', () => {
    // Delhi Bicycle Tour Database
    const tourModes = {
        standard: {
            duration: "4 Hours",
            cities: "New Delhi",
            price: "₹3,700 p.p.",
            shortDesc: "Experience the magic of New Delhi at sunrise. Cycle through historic streets and grand avenues on a comfortable city bike, culminating with a hearty breakfast at Hotel Godwin Deluxe.",
            highlight: "🚲 High-quality city bike, helmet, English-speaking cycling guide, and complimentary breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "06:15 AM", title: "Meet at Hotel Godwin Deluxe", desc: "Gather at the hotel lobby. Meet your cycling guide, get fitted for your bicycle and helmet, and receive a short safety briefing." },
                { day: "06:30 AM", title: "Start Cycling", desc: "Set off into the quiet, cool morning air, experiencing Delhi before the traffic begins." },
                { day: "07:00 AM", title: "India Gate & Rajpath", desc: "Cycle down the majestic Rajpath (Kartavya Path) towards India Gate. Enjoy the spectacular sunrise views over this iconic war memorial." },
                { day: "08:00 AM", title: "Lutyens' Delhi & Parliament House", desc: "Pedal through the wide, tree-lined avenues of Lutyens' Delhi. Pass by the grand Parliament House and Rashtrapati Bhavan (President's Estate)." },
                { day: "08:45 AM", title: "Lodhi Gardens", desc: "Take a peaceful ride through Lodhi Gardens, a beautiful park dotted with 15th-century architectural monuments and lush greenery." },
                { day: "09:30 AM", title: "Return to Godwin Deluxe", desc: "Cycle back to Hotel Godwin Deluxe, returning your equipment." },
                { day: "09:45 AM", title: "Breakfast", desc: "Celebrate a great morning ride with a delicious, complimentary breakfast at the Indian Grill Restaurant inside the hotel." }
            ],
            inclusions: [
                "Start and end at Hotel Godwin Deluxe",
                "High-quality 21-speed city bicycle and safety helmet",
                "Professional English-speaking cycling guide",
                "Bottled water during the ride",
                "Complimentary post-ride Breakfast at Indian Grill Restaurant"
            ],
            exclusions: [
                "Gratuities and tips",
                "Personal expenses"
            ]
        },
        ebike: {
            duration: "4 Hours",
            cities: "New Delhi",
            price: "₹5,400 p.p.",
            shortDesc: "Experience the magic of New Delhi at sunrise effortlessly. Glide through historic streets on a premium E-Bike, culminating with a hearty breakfast at Hotel Godwin Deluxe.",
            highlight: "⚡ Premium Electric Bike, helmet, English-speaking cycling guide, and complimentary breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "06:15 AM", title: "Meet at Hotel Godwin Deluxe", desc: "Gather at the hotel lobby. Meet your cycling guide, get fitted for your E-Bike and helmet, and receive a short safety briefing." },
                { day: "06:30 AM", title: "Start Cycling", desc: "Set off into the quiet, cool morning air, experiencing Delhi before the traffic begins." },
                { day: "07:00 AM", title: "India Gate & Rajpath", desc: "Glide down the majestic Rajpath (Kartavya Path) towards India Gate. Enjoy the spectacular sunrise views over this iconic war memorial." },
                { day: "08:00 AM", title: "Lutyens' Delhi & Parliament House", desc: "Pedal effortlessly through the wide, tree-lined avenues of Lutyens' Delhi. Pass by the grand Parliament House and Rashtrapati Bhavan (President's Estate)." },
                { day: "08:45 AM", title: "Lodhi Gardens", desc: "Take a peaceful ride through Lodhi Gardens, a beautiful park dotted with 15th-century architectural monuments and lush greenery." },
                { day: "09:30 AM", title: "Return to Godwin Deluxe", desc: "Cycle back to Hotel Godwin Deluxe, returning your equipment." },
                { day: "09:45 AM", title: "Breakfast", desc: "Celebrate a great morning ride with a delicious, complimentary breakfast at the Indian Grill Restaurant inside the hotel." }
            ],
            inclusions: [
                "Start and end at Hotel Godwin Deluxe",
                "Premium Electric Bicycle (E-Bike) and safety helmet",
                "Professional English-speaking cycling guide",
                "Bottled water during the ride",
                "Complimentary post-ride Breakfast at Indian Grill Restaurant"
            ],
            exclusions: [
                "Gratuities and tips",
                "Personal expenses"
            ]
        },
        group: {
            duration: "4 Hours",
            cities: "New Delhi",
            price: "₹2,900 p.p.",
            shortDesc: "Join a fun, private group cycling tour (min 4 people) through New Delhi at sunrise, culminating with a hearty breakfast at Hotel Godwin Deluxe.",
            highlight: "👨‍👩‍👧‍👦 Private Group Tour (Min 4), high-quality bikes, English-speaking guide, and complimentary breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "06:15 AM", title: "Meet at Hotel Godwin Deluxe", desc: "Gather your group at the hotel lobby. Meet your cycling guide, get fitted for bicycles and helmets, and receive a safety briefing." },
                { day: "06:30 AM", title: "Start Cycling", desc: "Set off into the quiet, cool morning air, experiencing Delhi before the traffic begins." },
                { day: "07:00 AM", title: "India Gate & Rajpath", desc: "Cycle down the majestic Rajpath (Kartavya Path) towards India Gate. Enjoy the spectacular sunrise views over this iconic war memorial." },
                { day: "08:00 AM", title: "Lutyens' Delhi & Parliament House", desc: "Pedal through the wide, tree-lined avenues of Lutyens' Delhi. Pass by the grand Parliament House and Rashtrapati Bhavan (President's Estate)." },
                { day: "08:45 AM", title: "Lodhi Gardens", desc: "Take a peaceful ride through Lodhi Gardens, a beautiful park dotted with 15th-century architectural monuments and lush greenery." },
                { day: "09:30 AM", title: "Return to Godwin Deluxe", desc: "Cycle back to Hotel Godwin Deluxe, returning your equipment." },
                { day: "09:45 AM", title: "Breakfast", desc: "Celebrate a great morning ride with a delicious, complimentary breakfast at the Indian Grill Restaurant inside the hotel." }
            ],
            inclusions: [
                "Start and end at Hotel Godwin Deluxe",
                "High-quality 21-speed city bicycles and safety helmets",
                "Professional English-speaking cycling guide dedicated to your group",
                "Bottled water during the ride",
                "Complimentary post-ride Breakfast at Indian Grill Restaurant"
            ],
            exclusions: [
                "Gratuities and tips",
                "Personal expenses"
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
        if(displayDuration) displayDuration.innerText = modeData.duration;
        if(displayCities) displayCities.innerText = modeData.cities;
        if(displayPrice) displayPrice.innerText = `From ${modeData.price}`;
        if(tourShortDesc) tourShortDesc.innerText = modeData.shortDesc;
        if(summaryPriceDisplay) summaryPriceDisplay.innerText = `${modeData.price}`;
        if(selectedModeInput) selectedModeInput.value = modeKey;

        // Highlight box
        if(modeHighlightBox) modeHighlightBox.innerText = modeData.highlight;

        // Render Timeline
        if(timelineBox) {
            timelineBox.innerHTML = '';
            modeData.itinerary.forEach(item => {
                const row = document.createElement('div');
                row.className = 'tl-row';
                row.innerHTML = `
                    <div class="tl-circle">🕒</div>
                    <div class="tl-body">
                        <div class="tl-head">
                            <span class="day-tag">${item.day}</span>
                            <h4 class="tl-title">${item.title}</h4>
                        </div>
                        <p class="tl-desc">${item.desc}</p>
                    </div>
                `;
                timelineBox.appendChild(row);
            });
        }

        // Render Inclusions
        if(inclusionsList) {
            inclusionsList.innerHTML = '';
            modeData.inclusions.forEach(inc => {
                const li = document.createElement('li');
                li.innerText = inc;
                inclusionsList.appendChild(li);
            });
        }

        // Render Exclusions
        if(exclusionsList) {
            exclusionsList.innerHTML = '';
            modeData.exclusions.forEach(exc => {
                const li = document.createElement('li');
                li.innerText = exc;
                exclusionsList.appendChild(li);
            });
        }
    }

    // Set Initial Load
    updateTourDisplay('standard');

    // Tab Event Listeners
    if(tabButtons) {
        tabButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                tabButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                updateTourDisplay(btn.getAttribute('data-mode'));
            });
        });
    }

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
            const mobile = document.getElementById('b-mobile').value;
            const date = document.getElementById('b-date').value;
            const guests = document.getElementById('b-travelers').value;
                        const notes = document.getElementById('b-notes').value;
            const mode = selectedModeInput.value;

            const submitUrl = "submit-booking.php";

            fetch(submitUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    _subject: `Grand Holidays - Delhi Bicycle Tour Request`,
                    Name: name,
                    Email: email,
                    Mobile: mobile,
                    Preferred_Date: date,
                    Guests: guests,
                    Start_Point: hotel,
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
                bookingForm.style.display = 'none';
                successMessage.innerHTML = `<h3>Request Submitted</h3><p>Your details were routed to our curator team. We will connect with you shortly.</p>`;
                successMessage.style.display = 'flex';
            });
        });
    }

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
