document.addEventListener('DOMContentLoaded', () => {
    // Delhi Museum Tour Database
    const tourModes = {
        pax2: {
            duration: "Half Day (10:00 AM - 2:00 PM)",
            cities: "Museum District, Delhi",
            price: "₹15,000 Total",
            shortDesc: "Explore Delhi's premier archives at a relaxed, customized pace. Perfect for couples or solo travelers who desire a tailored private tour of the National Museum, Rail Museum, and Dolls Museum in a private AC Sedan.",
            highlight: "🏛️ Includes private Sedan transfers (Dzire / Etios), professional local guide, entry tickets to all three museums, and bottled mineral water.",
            itinerary: [
                { time: "10:00 AM", title: "National Museum", desc: "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras." },
                { time: "11:30 AM", title: "National Rail Museum", desc: "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time." },
                { time: "01:00 PM", title: "International Dolls Museum", desc: "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes." },
                { time: "02:00 PM", title: "Return Transfer & Drop-off", desc: "After an enriching cultural journey, enjoy a comfortable private transfer back to Hotel Godwin Deluxe or your preferred location in Delhi." }
            ],
            inclusions: [
                "Pickup and drop-off from Hotel Godwin Deluxe or Delhi NCR",
                "Private air-conditioned Sedan (Toyota Etios / Maruti Dzire or similar)",
                "Services of a professional local English-speaking guide",
                "All museum and monument admission tickets",
                "Bottled mineral water and refreshments",
                "All toll taxes, parking, and driver allowances"
            ],
            exclusions: [
                "Lunches and dining expenses",
                "Camera or photography fees inside museums (where applicable)",
                "Personal expenses and tips",
                "Customary tipping and gratuities"
            ]
        },
        pax4: {
            duration: "Half Day (10:00 AM - 2:00 PM)",
            cities: "Museum District, Delhi",
            price: "₹23,000 Total",
            shortDesc: "Perfect for families or small groups. Travel together in a private AC SUV (Innova Crysta) to explore Delhi's premier museum circuit with your dedicated guide.",
            highlight: "🚙 Includes private SUV transfers (Toyota Innova Crysta), professional local guide, entry tickets to all three museums, and bottled mineral water.",
            itinerary: [
                { time: "10:00 AM", title: "National Museum", desc: "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras." },
                { time: "11:30 AM", title: "National Rail Museum", desc: "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time." },
                { time: "01:00 PM", title: "International Dolls Museum", desc: "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes." },
                { time: "02:00 PM", title: "Return Transfer & Drop-off", desc: "After an enriching cultural journey, enjoy a comfortable private transfer back to Hotel Godwin Deluxe or your preferred location in Delhi." }
            ],
            inclusions: [
                "Pickup and drop-off from Hotel Godwin Deluxe or Delhi NCR",
                "Private air-conditioned SUV (Toyota Innova Crysta)",
                "Services of a professional local English-speaking guide",
                "All museum and monument admission tickets",
                "Bottled mineral water and refreshments",
                "All toll taxes, parking, and driver allowances"
            ],
            exclusions: [
                "Lunches and dining expenses",
                "Camera or photography fees inside museums (where applicable)",
                "Personal expenses and tips",
                "Customary tipping and gratuities"
            ]
        },
        pax6: {
            duration: "Half Day (10:00 AM - 2:00 PM)",
            cities: "Museum District, Delhi",
            price: "₹32,000 Total",
            shortDesc: "Spacious and comfortable. Travel in a private AC Tempo Traveller to tour the National Museum, Rail Museum, and Dolls Museum with your family and dedicated guide.",
            highlight: "🚐 Includes private AC Minivan (Tempo Traveller), professional local guide, entry tickets to all three museums, and bottled mineral water.",
            itinerary: [
                { time: "10:00 AM", title: "National Museum", desc: "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras." },
                { time: "11:30 AM", title: "National Rail Museum", desc: "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time." },
                { time: "01:00 PM", title: "International Dolls Museum", desc: "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes." },
                { time: "02:00 PM", title: "Return Transfer & Drop-off", desc: "After an enriching cultural journey, enjoy a comfortable private transfer back to Hotel Godwin Deluxe or your preferred location in Delhi." }
            ],
            inclusions: [
                "Pickup and drop-off from Hotel Godwin Deluxe or Delhi NCR",
                "Private air-conditioned Minivan (Tempo Traveller)",
                "Services of a professional local English-speaking guide",
                "All museum and monument admission tickets",
                "Bottled mineral water and refreshments",
                "All toll taxes, parking, and driver allowances"
            ],
            exclusions: [
                "Lunches and dining expenses",
                "Camera or photography fees inside museums (where applicable)",
                "Personal expenses and tips",
                "Customary tipping and gratuities"
            ]
        },
        pax10: {
            duration: "Half Day (10:00 AM - 2:00 PM)",
            cities: "Museum District, Delhi",
            price: "₹45,000 Total",
            shortDesc: "Our signature group curation. Travel in a private AC Minibus with a dedicated guide and tour coordinator ensuring a seamless, premium educational experience.",
            highlight: "🚌 Includes private luxury AC Coach, tour coordinator + professional guide, entry tickets to all three museums, and onboard refreshments.",
            itinerary: [
                { time: "10:00 AM", title: "National Museum", desc: "Step into the cultural gateway of India. House to a staggering collection of antiquities, you will witness 5,000-year-old relics of the Indus Valley Civilization, exquisite Buddhist murals from Central Asia, and royal jewelry. It is a veritable treasure house of India's golden eras." },
                { time: "11:30 AM", title: "National Rail Museum", desc: "Sprawling across 10 lush acres, this fascinating archive chronicles 150 years of India's railway heritage. Marvel at majestic royal saloons, vintage steam locomotives, and the legendary Fairy Queen built in 1855—the best-preserved locomotive of its time." },
                { time: "01:00 PM", title: "International Dolls Museum", desc: "A delightful conclusion to your journey, this uniquely captivating collection features over 6,000 intricately crafted dolls from 85 countries, each resplendently dressed in authentic regional costumes." },
                { time: "02:00 PM", title: "Return Transfer & Drop-off", desc: "After an enriching cultural journey, enjoy a comfortable private transfer back to Hotel Godwin Deluxe or your preferred location in Delhi." }
            ],
            inclusions: [
                "Pickup and drop-off from Hotel Godwin Deluxe or Delhi NCR",
                "Private air-conditioned luxury Mini-Coach (15-Seater)",
                "Services of a professional local English-speaking guide",
                "Dedicated tour coordinator to manage group flow",
                "All museum and monument admission tickets",
                "Bottled mineral water, soft drinks, and light snacks",
                "All toll taxes, priority monument parking, and driver fees"
            ],
            exclusions: [
                "Lunches and dining expenses",
                "Camera or photography fees inside museums (where applicable)",
                "Personal expenses and tips",
                "Customary tipping and gratuities"
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
            var origText = submitBtn ? submitBtn.innerText : 'Submit';
        submitBtn.innerText = 'Routing to Curator...';
        submitBtn.disabled = true;

        const data = {
            _subject: `New Grand Holidays Booking: Delhi Museum Tour (${document.getElementById('selected-tour-mode').value.toUpperCase()})`,
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
