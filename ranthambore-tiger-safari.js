document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "3 Days / 2 Nights",
            cities: "Delhi → Ranthambore → Delhi",
            price: "₹14,000 per person",
            shortDesc: "A thrilling 3-day wildlife adventure from Delhi to Ranthambore National Park. Experience two exhilarating jeep safaris in search of the majestic Bengal Tiger.",
            highlight: "🐅 Two thrilling jeep safaris in Ranthambore National Park with expert naturalist guides.",
            itinerary: [
                { day: 1, title: "Delhi to Ranthambore", desc: "You will be picked up from your hotel or airport in Delhi in a private, air-conditioned car. You will drive through the scenic North Indian countryside for approximately 6–7 hours (approx. 380 km). Upon arrival at Ranthambore, you will check into your resort or hotel. Spend the rest of the evening relaxing, enjoying the sounds of the jungle around you. Dinner and overnight stay at the resort." },
                { day: 2, title: "Tiger Safari Adventure", desc: "Morning: An early wake-up call for your first jeep safari into the heart of Ranthambore National Park. Your expert naturalist guide will help you spot Bengal tigers, leopards, sloth bears, deer, crocodiles, and hundreds of bird species. Return to the resort for breakfast and rest.\n\nAfternoon: Your second safari ride sets out in the cooler afternoon hours — often the best time for wildlife sightings near watering holes. Return to the resort for dinner and an overnight stay." },
                { day: 3, title: "Ranthambore Fort & Return to Delhi", desc: "After a relaxed breakfast at the resort, you have the option to visit the magnificent Ranthambore Fort — a UNESCO World Heritage Site perched dramatically inside the national park with panoramic jungle views. You will then depart Ranthambore in your private car and drive back to Delhi (approx. 6–7 hours). You will be dropped off at your hotel or the airport, concluding your wildlife adventure." }
            ],
            inclusions: [
                "Private air-conditioned car with driver (entire trip)",
                "Toll taxes, parking fees & fuel",
                "Two jeep safari rides in Ranthambore National Park",
                "English-speaking expert naturalist guide (safaris)",
                "Assistance on Arrival",
                "24-hour helpline"
            ],
            exclusions: [
                "Hotel accommodation (available as add-on)",
                "Meals (unless hotel package includes)",
                "Camera & photography fees in the national park",
                "Personal expenses (tips, beverages, laundry)",
                "Travel insurance",
                "Any extra activities not in the itinerary"
            ]
        }
    };

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

    function updateTourDisplay(modeKey) {
        const modeData = tourModes[modeKey];
        if (!modeData) return;

        if (displayDuration) displayDuration.innerText = modeData.duration;
        if (displayCities) displayCities.innerText = modeData.cities;
        if (displayPrice) displayPrice.innerText = `${modeData.price}`;
        if (tourShortDesc) tourShortDesc.innerText = modeData.shortDesc;
        if (summaryPriceDisplay) summaryPriceDisplay.innerText = `${modeData.price}`;
        if (selectedModeInput) selectedModeInput.value = modeKey;

        if (modeHighlightBox) modeHighlightBox.innerText = modeData.highlight;

        if (timelineBox) {
            timelineBox.innerHTML = '';
            modeData.itinerary.forEach((item, idx) => {
                const dayBlock = document.createElement('div');
                dayBlock.className = 'timeline-day-block';

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
                li.innerText = inc;
                inclusionsList.appendChild(li);
            });
        }

        if (exclusionsList) {
            exclusionsList.innerHTML = '';
            modeData.exclusions.forEach(exc => {
                const li = document.createElement('li');
                li.innerText = exc;
                exclusionsList.appendChild(li);
            });
        }
    }

    updateTourDisplay('car');

    const bookingForm = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
            var origText = submitBtn ? submitBtn.innerText : 'Submit';
            submitBtn.innerText = 'Routing to Curator...';
            submitBtn.disabled = true;

            const data = {
                _subject: `New Grand Holidays Booking: Ranthambore Tiger Safari`,
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
    }

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
