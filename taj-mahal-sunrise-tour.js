document.addEventListener('DOMContentLoaded', () => {

    const tourModes = {
        sunrise: {
            duration: '~2.5 Hours',
            cities: 'Agra · Taj Mahal',
            price: '₹7,500 per person (Min. 2 Pax)',
            shortDesc: 'A short, guided sunrise experience at the Taj Mahal with express skip-the-line entry. Includes private hotel pickup and drop-off from Agra (or Delhi pickup available).',
            highlight: 'Skip the line at sunrise — the Taj Mahal at its most magical, with an expert local guide and private transfers.',
            itinerary: [
                {
                    time: 'Pickup',
                    title: 'Hotel Pickup',
                    desc: 'Your private, air-conditioned vehicle and expert guide arrive at your hotel. For Agra hotel pickups, this is typically around 5:00–5:30 AM. For Delhi hotel pickups, departure is around 2:00–3:00 AM to arrive at Agra by sunrise.'
                },
                {
                    time: 'Arrival',
                    title: 'Arrival at the Taj Mahal',
                    desc: 'You are driven directly to the Taj Mahal entrance. Your guide presents your pre-collected express entry tickets, allowing you to bypass the standard queues and walk straight in as the gates open.'
                },
                {
                    time: '2.5 Hours',
                    title: 'The Sunrise Experience',
                    desc: 'Spend approximately 2.5 breathtaking hours inside the Taj Mahal complex. Your expert local guide will share the remarkable history of Emperor Shah Jahan and Mumtaz Mahal, point out the finest architectural details, and help you find the best photography spots — including the iconic reflection pool shot. Watch the white marble transform from silver to deep gold as the sun rises.'
                },
                {
                    time: 'Drop-off',
                    title: 'Hotel Drop-off',
                    desc: 'After the tour, your private vehicle drives you back to your hotel in Agra (or Delhi, if applicable). You will arrive back well before mid-morning, leaving your day completely free for further exploration or onward travel.'
                }
            ],
            inclusions: [
                'Private air-conditioned vehicle with professional driver',
                'Expert local English-speaking guide (for the full experience)',
                'Pre-collected express entry tickets (skip the standard queue)',
                'Hotel pickup and drop-off (Agra hotel)',
                'Fuel, tolls, and driver allowances'
            ],
            exclusions: [
                'Camera / tripod fees inside the complex',
                'Meals and beverages',
                'Personal expenses (tips, laundry, phone calls)',
                'Travel insurance',
                'Delhi pickup surcharge (if applicable)',
                'Any extra activities not listed in the itinerary'
            ]
        }
    };

    const displayDuration = document.getElementById('display-duration');
    const displayCities   = document.getElementById('display-cities');
    const displayPrice    = document.getElementById('display-price');
    const tourShortDesc   = document.getElementById('tour-short-desc');
    const modeHighlightBox = document.getElementById('mode-highlight-box');
    const timelineBox     = document.getElementById('itinerary-timeline-box');
    const inclusionsList  = document.getElementById('inclusions-list');
    const exclusionsList  = document.getElementById('exclusions-list');
    const summaryPriceDisplay = document.getElementById('summary-price-display');
    const selectedModeInput   = document.getElementById('selected-tour-mode');

    function updateTourDisplay(modeKey) {
        const modeData = tourModes[modeKey];
        if (!modeData) return;

        if (displayDuration) displayDuration.innerText = modeData.duration;
        if (displayCities)   displayCities.innerText   = modeData.cities;
        if (displayPrice)    displayPrice.innerText     = modeData.price;
        if (tourShortDesc)   tourShortDesc.innerText    = modeData.shortDesc;
        if (summaryPriceDisplay) summaryPriceDisplay.innerText = modeData.price;
        if (selectedModeInput)   selectedModeInput.value       = modeKey;
        if (modeHighlightBox)    modeHighlightBox.innerText    = modeData.highlight;

        if (timelineBox) {
            timelineBox.innerHTML = '';
            modeData.itinerary.forEach((item, idx) => {
                const dayBlock = document.createElement('div');
                dayBlock.className = 'timeline-day-block';

                const stepNum  = idx + 1;
                const tagLabel = item.time
                    ? `<span class="day-tag time-tag">${item.time}</span>`
                    : `<span class="day-tag">Step ${stepNum}</span>`;

                dayBlock.innerHTML = `
                    <div class="tl-circle">${stepNum}</div>
                    <div class="tl-body">
                        <div class="tl-head">
                            <h4 class="tl-title">${item.title}</h4>
                            ${tagLabel}
                        </div>
                        <p class="tl-desc">${item.desc.replace(/\n/g, '<br>')}</p>
                    </div>
                `;
                timelineBox.appendChild(dayBlock);
            });
        }

        if (inclusionsList) {
            inclusionsList.innerHTML = '';
            modeData.inclusions.forEach(inc => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <svg class="inc-icon check" width="20" height="20" style="flex-shrink:0;margin-top:1px;" fill="none" stroke="#16a34a" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
                    </svg>
                    ${inc}`;
                inclusionsList.appendChild(li);
            });
        }

        if (exclusionsList) {
            exclusionsList.innerHTML = '';
            modeData.exclusions.forEach(exc => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <svg class="inc-icon cross" width="20" height="20" style="flex-shrink:0;margin-top:1px;" fill="none" stroke="#dc2626" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                    ${exc}`;
                exclusionsList.appendChild(li);
            });
        }
    }

    updateTourDisplay('sunrise');

    // Booking form
    const bookingForm    = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
            submitBtn.innerText = 'Routing to Curator...';
            submitBtn.disabled  = true;

            const data = {
                _subject: 'New Grand Holidays Booking: Taj Mahal Express Entry Sunrise Tour',
                name:            document.getElementById('b-name').value,
                email:           document.getElementById('b-email').value,
                _cc:             document.getElementById('b-email').value,
                mobile:          document.getElementById('b-mobile').value,
                preferredDate:   document.getElementById('b-date').value,
                guestsCount:     document.getElementById('b-travelers').value,
                message:         document.getElementById('b-notes').value,
                estimatedPrice:  document.getElementById('summary-price-display').innerText
            };

            fetch('submit-booking.php', {
                method:  'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body:    JSON.stringify(data)
            })
            .then(r => r.json())
            .then(data => {
                if (data.success || data.success === 'true') {
                    bookingForm.style.display    = 'none';
                    bookingSuccess.style.display = 'flex';
                } else {
                    alert('Server Message: ' + (data.message || 'Email service requires activation. Please check tours@godwinhotels.com for an activation link.'));
                    submitBtn.innerText = 'Submit Reservation Request';
                    submitBtn.disabled  = false;
                }
            })
            .catch(err => {
                console.error(err);
                submitBtn.innerText = 'Error. Try Again.';
                submitBtn.disabled  = false;
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

    // Mobile hamburger
    const hamburger = document.querySelector('.hamburger');
    const navMenu   = document.querySelector('.nav-menu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Mobile dropdown toggle
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        if (toggle) {
            toggle.addEventListener('click', (e) => {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    dropdown.classList.toggle('active');
                }
            });
        }
    });
});
