document.addEventListener('DOMContentLoaded', () => {
    // 5 Days Golden Triangle Tour Database
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Delhi - Jaipur - Agra",
            price: "₹38,000 (For 2 Adults)",
            shortDesc: "A Golden triangle tour will take you to the 3 most amazing cities of India which displays the evidence of Mughal era in front of travellers for 5 days. This route consists of 3 major cities-Delhi, Jaipur and Agra. The capital of India will show you the heritage marvels from Mughal era where Agra will display the symbol of love-Tajmahal. Jaipur will fill your heart with most vibrant colors and you will get to explore the rural region of India in Rajasthan.",
            highlight: "🚗 Includes a dedicated private Swift Dzire with personal driver, hotel accommodation, and guided tours throughout your trip.",
            itinerary: [
                { day: 1, title: "Delhi Arrival", desc: "As soon as you will arrive at Delhi airport you will be transferred to your pre-booked hotel. Check into the hotel and spend the rest of the day at your leisure. Stay overnight." },
                { day: 2, title: "Delhi - Jaipur", desc: "Post breakfast visit Lotus Temple built in shape of petals of Lotus where you can meditate for hours in peace, Red Fort built using red sandstones and was residence of Mughals for many years, Rajghat made to commemorate Father of Nation Mahatma Gandhi, India Gate made to honor soldiers who died during wars and Jantar Mantar which is a great place for astronomy lovers. Later on pay a visit at Swaminarayan Akshardham Temple, Qutub Minar one of the tallest masonry minaret with a mosque at foot of minar. You will be transferred to Jaipur after excursion and escorted to hotel for the overnight stay in Jaipur." },
                { day: 3, title: "Jaipur", desc: "Post breakfast visit Amer Fort and enjoy Elephant ride at the Fort ramp. It is situated on hilltop and overlooks Maota Lake where you will be spellbound by the reflection of the Fort in the lake. It comprises many palaces. Next visit, Hawa Mahal built in shape of crown of Hindu Lord Krishna, City Palace which comprises Mubarak Mahal which affords fine view of the surroundings and Chandra Mahal converted into museum where you can see many stuffs related to king and Jantar Mantar, one of the largest observatories in India. Return back to the hotel and enjoy your dinner." },
                { day: 4, title: "Jaipur - Agra", desc: "After having breakfast you will be transferred to Agra. En-route Fatehpur Sikri and visit Panch Mahal a five storied building, Buland Darwaza which was built to celebrate victory of Akbar, Jodha Bai Palace made for Queen's of Akbar with blend of Rajput and Mughal architecture. Next pay a pilgrimage site Tomb of Sheik Salim Chisti made to honor sufi saint and the tomb is covered with intricate carved marble sheets. Continue your tour towards Agra. Check into the hotel and stay overnight." },
                { day: 5, title: "Agra Sightseeing & Departure", desc: "Post breakfast visit Tajmahal and enjoy mesmerizing sunrise views. It looks beyond imagination beautiful when sunrays fall on it. It was made by Shah Jahan in memory of his beloved wife. Next halt at Agra Fort lying parallel to River Yamuna, built using red sand stones and within the premises there are many Palaces with stunning architecture. Next halt will be Tomb of Itimad-ud-Daulah surrounded by lush green meadow also known as Baby Taj and Draft of Jewel, Akbar's Tomb the burial point of Emperor Akbar. In the evening enjoy the mesmerizing views of Tajmahal during sunset from Mehtab Bagh. Later in the day you will be transferred to the nearest airport for boarding your scheduled flight." }
            ],
            inclusions: [
                "Dedicated Swift Dzire A/C car throughout the tour",
                "Private English-speaking guides at all cities",
                "Hotel accommodation with breakfast",
                "All toll taxes, parking, and driver allowances",
                "Elephant ride at Amer Fort (subject to availability)"
            ],
            exclusions: [
                "International flights and travel visas",
                "Monument entry tickets and camera fees",
                "Personal expenses, lunches, and dinners",
                "Customary tipping and gratuities"
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


    // Guest Counter Logic
    const guestMinus = document.querySelector('.btn-guest-minus');
    const guestPlus = document.querySelector('.btn-guest-plus');
    const guestInput = document.getElementById('b-travelers');

    if (guestMinus && guestPlus && guestInput) {
        guestMinus.addEventListener('click', () => {
            let val = parseInt(guestInput.value) || 1;
            if (val > 1) {
                guestInput.value = val - 1;
            }
        });
        guestPlus.addEventListener('click', () => {
            let val = parseInt(guestInput.value) || 1;
            if (val < 16) {
                guestInput.value = val + 1;
            }
        });
    }

    // Sidebar Booking Form Handler
    const bookingForm = document.getElementById('tourBookingForm');
    const bookingSuccess = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = bookingForm.querySelector('.btn-sidebar-submit');
            submitBtn.innerText = 'Routing to Curator...';
            submitBtn.disabled = true;

            const data = {
                _subject: `New Grand Holidays Booking: 5 Days Golden Triangle`,
                name: document.getElementById('b-name').value,
                email: document.getElementById('b-email').value,
                preferredDate: document.getElementById('b-date').value,
                guestsCount: document.getElementById('b-travelers').value,
                message: document.getElementById('b-notes').value,
                estimatedPrice: document.getElementById('summary-price-display').innerText
            };

            fetch("https://formsubmit.co/ajax/mail@godwinhotels.com", {
                method: "POST",
                headers: { 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(() => {
                bookingForm.style.display = 'none';
                bookingSuccess.style.display = 'flex';
            })
            .catch(err => {
                console.error(err);
                submitBtn.innerText = 'Error. Try Again.';
                submitBtn.disabled = false;
            });
        });
    }

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
