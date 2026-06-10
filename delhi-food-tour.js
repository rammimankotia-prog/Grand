document.addEventListener('DOMContentLoaded', () => {
    // Delhi Food & Spice Tour Database
    const tourModes = {
        sedan: {
            duration: "8 Hours",
            cities: "Old & New Delhi",
            price: "$65 (For 2 Adults)",
            shortDesc: "Experience the vibrant culinary heritage of Delhi. Travel in a comfortable private Sedan with pick-up, drop-off, and breakfast at Hotel Godwin Deluxe.",
            highlight: "🚗 Private Sedan, English-speaking guide, comprehensive street food & spice market tour, starting with breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "09:00 AM", title: "Breakfast at Godwin Deluxe", desc: "Begin your day with a complimentary, hearty breakfast at the Indian Grill Restaurant within Hotel Godwin Deluxe." },
                { day: "10:00 AM", title: "Pick-up from Godwin Deluxe", desc: "Meet your English-speaking driver and guide at the hotel lobby. Board your neat and clean private Sedan." },
                { day: "10:30 AM", title: "Khari Baoli Spice Market", desc: "Walk through Asia's largest wholesale spice market. Let the aromas of rich Indian spices and herbs captivate your senses." },
                { day: "12:00 PM", title: "Chandni Chowk Street Food", desc: "Dive into the heart of Old Delhi. Taste world-famous local delicacies like Chole Bhature, Aloo Tikki, and Jalebis from heritage vendors." },
                { day: "02:00 PM", title: "Paranthe Wali Gali", desc: "Enjoy a traditional lunch experience tasting a variety of stuffed deep-fried bread at historic eateries." },
                { day: "03:30 PM", title: "Jama Masjid Environs", desc: "Explore the bustling lanes around Jama Masjid, sampling Mughal-style kebabs, rich curries, and traditional Shahi Tukda." },
                { day: "05:00 PM", title: "Drop-off at Godwin Deluxe", desc: "Return to Hotel Godwin Deluxe in the comfort of your private vehicle." }
            ],
            inclusions: [
                "Pick-up and Drop-off at Hotel Godwin Deluxe",
                "Complimentary Breakfast at Indian Grill Restaurant, Hotel Godwin Deluxe",
                "Private, neat, and clean Sedan",
                "Professional English-speaking Driver and Tour Guide",
                "Toll taxes, parking, and driver allowance"
            ],
            exclusions: [
                "Cost of food and beverages consumed during the tour (pay as you go)",
                "Personal expenses and tips",
                "Monument entry fees (if any)"
            ]
        },
        suv: {
            duration: "8 Hours",
            cities: "Old & New Delhi",
            price: "$85 (For 2 Adults)",
            shortDesc: "Experience the vibrant culinary heritage of Delhi. Travel in a spacious private SUV with pick-up, drop-off, and breakfast at Hotel Godwin Deluxe.",
            highlight: "🚙 Private spacious SUV, English-speaking guide, comprehensive street food & spice market tour, starting with breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "09:00 AM", title: "Breakfast at Godwin Deluxe", desc: "Begin your day with a complimentary, hearty breakfast at the Indian Grill Restaurant within Hotel Godwin Deluxe." },
                { day: "10:00 AM", title: "Pick-up from Godwin Deluxe", desc: "Meet your English-speaking driver and guide at the hotel lobby. Board your neat and clean private SUV." },
                { day: "10:30 AM", title: "Khari Baoli Spice Market", desc: "Walk through Asia's largest wholesale spice market. Let the aromas of rich Indian spices and herbs captivate your senses." },
                { day: "12:00 PM", title: "Chandni Chowk Street Food", desc: "Dive into the heart of Old Delhi. Taste world-famous local delicacies like Chole Bhature, Aloo Tikki, and Jalebis from heritage vendors." },
                { day: "02:00 PM", title: "Paranthe Wali Gali", desc: "Enjoy a traditional lunch experience tasting a variety of stuffed deep-fried bread at historic eateries." },
                { day: "03:30 PM", title: "Jama Masjid Environs", desc: "Explore the bustling lanes around Jama Masjid, sampling Mughal-style kebabs, rich curries, and traditional Shahi Tukda." },
                { day: "05:00 PM", title: "Drop-off at Godwin Deluxe", desc: "Return to Hotel Godwin Deluxe in the comfort of your private vehicle." }
            ],
            inclusions: [
                "Pick-up and Drop-off at Hotel Godwin Deluxe",
                "Complimentary Breakfast at Indian Grill Restaurant, Hotel Godwin Deluxe",
                "Private, neat, and clean SUV",
                "Professional English-speaking Driver and Tour Guide",
                "Toll taxes, parking, and driver allowance"
            ],
            exclusions: [
                "Cost of food and beverages consumed during the tour (pay as you go)",
                "Personal expenses and tips",
                "Monument entry fees (if any)"
            ]
        },
        minivan: {
            duration: "8 Hours",
            cities: "Old & New Delhi",
            price: "$110 (For 2 Adults)",
            shortDesc: "Experience the vibrant culinary heritage of Delhi. Travel in a premium private Minivan with pick-up, drop-off, and breakfast at Hotel Godwin Deluxe.",
            highlight: "🚐 Private premium Minivan, English-speaking guide, comprehensive street food & spice market tour, starting with breakfast at Hotel Godwin Deluxe.",
            itinerary: [
                { day: "09:00 AM", title: "Breakfast at Godwin Deluxe", desc: "Begin your day with a complimentary, hearty breakfast at the Indian Grill Restaurant within Hotel Godwin Deluxe." },
                { day: "10:00 AM", title: "Pick-up from Godwin Deluxe", desc: "Meet your English-speaking driver and guide at the hotel lobby. Board your neat and clean private Minivan." },
                { day: "10:30 AM", title: "Khari Baoli Spice Market", desc: "Walk through Asia's largest wholesale spice market. Let the aromas of rich Indian spices and herbs captivate your senses." },
                { day: "12:00 PM", title: "Chandni Chowk Street Food", desc: "Dive into the heart of Old Delhi. Taste world-famous local delicacies like Chole Bhature, Aloo Tikki, and Jalebis from heritage vendors." },
                { day: "02:00 PM", title: "Paranthe Wali Gali", desc: "Enjoy a traditional lunch experience tasting a variety of stuffed deep-fried bread at historic eateries." },
                { day: "03:30 PM", title: "Jama Masjid Environs", desc: "Explore the bustling lanes around Jama Masjid, sampling Mughal-style kebabs, rich curries, and traditional Shahi Tukda." },
                { day: "05:00 PM", title: "Drop-off at Godwin Deluxe", desc: "Return to Hotel Godwin Deluxe in the comfort of your private vehicle." }
            ],
            inclusions: [
                "Pick-up and Drop-off at Hotel Godwin Deluxe",
                "Complimentary Breakfast at Indian Grill Restaurant, Hotel Godwin Deluxe",
                "Private, neat, and clean Minivan",
                "Professional English-speaking Driver and Tour Guide",
                "Toll taxes, parking, and driver allowance"
            ],
            exclusions: [
                "Cost of food and beverages consumed during the tour (pay as you go)",
                "Personal expenses and tips",
                "Monument entry fees (if any)"
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
    updateTourDisplay('sedan');

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

            const submitUrl = "https://formsubmit.co/ajax/mail@godwinhotels.com";

            fetch(submitUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    _subject: `Grand Holidays - Delhi Food & Spice Tour Request`,
                    Name: name,
                    Email: email,
                    Mobile: mobile,
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
