document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "6 Days / 5 Nights",
            cities: "Delhi - Shimla - Manali",
            price: "On Request",
            shortDesc: "Escape to the magnificent Himalayas! This refreshing 6-day journey takes you through the beautiful pine forests and snow-capped peaks of Shimla and Manali, starting and ending in Delhi.",
            highlight: "🚗 Includes private premium A/C transport, daily delicious breakfast, and complete assistance.",
            itinerary: [
                { day: 1, title: "Welcome to Delhi & The Drive to Shimla", desc: "Your adventure begins! We will warmly welcome you at the Delhi airport or railway station. You'll then hop into your private luxury car for a scenic drive up into the mountains to Shimla. Known as the 'Queen of Hills', Shimla boasts a wonderful, laid-back atmosphere. Check into your hotel and enjoy a relaxing evening at your own pace." },
                { day: 2, title: "Shimla Sightseeing & Exploring Kufri", desc: "After a delicious breakfast, we head to Kufri, a stunning nature retreat famous for its snow slopes, winter sports, and the Himalayan Nature Park (home to over 180 animal species!). Later, we'll visit the famous Jhakoo Temple and give you plenty of time to shop and stroll along Shimla's iconic Mall Road before enjoying a mouth-watering dinner back at the resort." },
                { day: 3, title: "The Journey to Manali", desc: "Today, enjoy breakfast and check out, as we hit the road for the beautiful drive from Shimla to Manali. You'll watch the scenery transform as we travel deeper into the Himalayas. After checking into your hotel in Manali, you can spend the evening relaxing or exploring the local markets." },
                { day: 4, title: "Manali Adventure & Sightseeing", desc: "Get ready for a fun-filled day! First, we visit the breathtaking Solang Valley where you can try thrilling activities like paragliding and zorbing. In the afternoon, we'll explore Manali's cultural gems: the peaceful Tibetan Monastery, the natural hot springs at Vashist Village, and the ancient, forest-surrounded Hadimba Devi Temple. Enjoy your evening back at the hotel or taking a walk down Mall Road." },
                { day: 5, title: "Return to Delhi & City Tour", desc: "After breakfast, we take the long, scenic drive back down the mountains to Delhi. Once we arrive in the capital, you'll stretch your legs with a wonderful sightseeing tour of New Delhi! You'll visit the majestic India Gate, the President's House, the historic Qutub Minar, the beautiful Lotus Temple, and Raj Ghat. Check into your Delhi hotel for a restful night." },
                { day: 6, title: "Departure from Delhi", desc: "Enjoy your final breakfast at the hotel. We'll assist you with checking out and provide a comfortable transfer to the Delhi Airport or Railway Station for your journey home, carrying wonderful memories of the Himalayas!" }
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
                _subject: `New Grand Holidays Booking: Himachal Exotic Tour`,
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
