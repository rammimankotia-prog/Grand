document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Jaipur - Ranthambore",
            price: "On Request",
            shortDesc: "Experience the ultimate contrast of Rajasthan: the royal grandeur of Jaipur's palaces and the thrilling wilderness of Ranthambore, home to the magnificent Royal Bengal Tiger.",
            highlight: "🐅 Includes private premium A/C transport, comfortable hotel stays, and daily breakfast.",
            itinerary: [
                { day: 1, title: "Welcome to the Pink City!", desc: "Your royal adventure begins today! Upon arriving at the Jaipur airport or railway station, our friendly representative will greet you and drive you to your hotel in a private luxury car. After checking in, the rest of the evening is entirely yours to relax and settle in." },
                { day: 2, title: "Exploring the Royal Wonders of Jaipur", desc: "After a delicious breakfast, get ready for a full day of sightseeing in the beautiful Pink City. We will visit the majestic Amber Fort perched on a hill, stop by the iconic honeycomb-patterned Hawa Mahal (Palace of Winds) for some amazing photos, and explore the ancient Jantar Mantar observatory and the grand City Palace. In the evening, you can relax or shop for vibrant local handicrafts." },
                { day: 3, title: "Journey to the Tiger's Domain", desc: "We start early today with breakfast before hitting the road for Ranthambore (approx. 280 kms, a scenic 6-hour drive). Ranthambore is world-famous for its incredible tiger population! Upon arrival, you'll check into your comfortable hotel and spend the evening relaxing and preparing for tomorrow's big adventure." },
                { day: 4, title: "Thrilling Ranthambore Wildlife Safari", desc: "Wake up early for an unforgettable morning! You'll embark on an exciting wildlife safari deep into the Ranthambore National Park in a shared coach. Keep your eyes peeled for the majestic Royal Bengal Tigers, leopards, and a rich variety of birds and wildlife. After the thrilling safari, the rest of the day is yours to relax at the hotel and soak in the natural surroundings." },
                { day: 5, title: "Farewell & Departure", desc: "Enjoy your final breakfast of the trip. We will then provide a comfortable transfer back to the Jaipur Airport or Railway Station for your onward journey. Your holiday concludes here, leaving you with incredible memories of palaces and tigers. See you again soon!" }
            ],
            inclusions: [
                "Assistance on Arrival.",
                "A 24 – hour helpline.",
                "Daily Breakfast",
                "Hotel Accommodation",
                "Travelling in an AC car."
            ],
            exclusions: [
                "Air fare / train fare.",
                "Guide & Monuments fees",
                "Camera & safari Charges",
                "Insurance",
                "Any other item not specified."
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
            submitBtn.innerText = 'Routing to Curator...';
            submitBtn.disabled = true;

            const data = {
                _subject: `New Grand Holidays Booking: Tiger Tour With Jaipur`,
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
