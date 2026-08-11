document.addEventListener('DOMContentLoaded', () => {
    // 5 Days Golden Triangle Tour Database
    const tourModes = {
        car: {
            duration: "8 Hours / 80 Kilometers",
            cities: "Delhi Local Sightseeing",
            price: "₹4,500 - ₹6,000 (Based on seating capacity)",
            shortDesc: "Experience the vibrant city of Delhi at your own pace with our 8 Hours / 80 Kilometers day sightseeing tour in a spacious and comfortable Tempo Traveller. Perfect for families and groups, this package offers the flexibility to explore the capital's iconic monuments, bustling markets, and historical landmarks together.",
            highlight: "🚐 Includes a dedicated fully air-conditioned Tempo Traveller with a professional local driver for 8 Hours and 80 Kilometers within Delhi.",
            itinerary: [
                { day: 1, time: "09:00 AM", title: "Pick-up & Old Delhi Exploration", desc: "Your chauffeur will pick you up from your hotel or residence in Delhi NCR. Start your day by visiting the historical Red Fort and Jama Masjid in Old Delhi, followed by a drive past the bustling lanes of Chandni Chowk." },
                { day: 1, time: "12:00 PM", title: "New Delhi Monuments", desc: "Head towards New Delhi to visit the iconic India Gate, Parliament House, and Rashtrapati Bhavan (President's Estate). Perfect spots for photography." },
                { day: 1, time: "02:00 PM", title: "Lunch & South Delhi Highlights", desc: "After lunch, visit the serene Lotus Temple and the towering Qutub Minar, a UNESCO World Heritage site showcasing brilliant Indo-Islamic architecture." },
                { day: 1, time: "05:00 PM", title: "Evening Drop-off", desc: "Conclude your 8-hour sightseeing tour with a convenient drop-off at your hotel or any desired location within the city limits." }
            ],
            inclusions: [
                "Air-conditioned Tempo Traveller for 8 Hours / 80 KM",
                "Professional English-speaking driver",
                "Fuel, state taxes, and toll charges within Delhi",
                "Pick-up and drop-off within Delhi NCR"
            ],
            exclusions: [
                "Monument entry fees and camera charges",
                "Meals and beverages",
                "Guide services (can be arranged on request)",
                "Extra kilometers/hours charges beyond 80KM/8Hrs",
                "Parking charges"
            ]
        }
    };

    // UI Elements
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
        if (displayDuration) displayDuration.innerText = modeData.duration;
        if (displayCities) displayCities.innerText = modeData.cities;
        if (displayPrice) displayPrice.innerText = `From ${modeData.price}`;
        if (tourShortDesc) tourShortDesc.innerText = modeData.shortDesc;
        if (summaryPriceDisplay) summaryPriceDisplay.innerText = `${modeData.price}`;
        if (selectedModeInput) selectedModeInput.value = modeKey;

        // Highlight box
        if (modeHighlightBox) modeHighlightBox.innerText = modeData.highlight;

        // Render Timeline
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
                        <p class="tl-desc">${item.desc}</p>
                    </div>
                `;
                timelineBox.appendChild(dayBlock);
            });
        }

        // Render Inclusions
        if (inclusionsList) {
            inclusionsList.innerHTML = '';
            modeData.inclusions.forEach(inc => {
                const li = document.createElement('li');
                li.innerText = inc;
                inclusionsList.appendChild(li);
            });
        }

        // Render Exclusions
        if (exclusionsList) {
            exclusionsList.innerHTML = '';
            modeData.exclusions.forEach(exc => {
                const li = document.createElement('li');
                li.innerText = exc;
                exclusionsList.appendChild(li);
            });
        }
    }

    // Initialize display with default 'car' mode
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
                _subject: `New Grand Holidays Booking: 5 Days Golden Triangle`,
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
