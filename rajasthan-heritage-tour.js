document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "8 Days / 7 Nights",
            cities: "Jaipur - Jodhpur - Jaisalmer - Jodhpur - Udaipur",
            price: "On Request",
            shortDesc: "Experience the royal heritage of Rajasthan. This tour covers the Pink City of Jaipur, the Blue City of Jodhpur, the Golden City of Jaisalmer, and the romantic Lake City of Udaipur.",
            highlight: "🚗 Includes dedicated premium A/C transport, daily breakfast, and complete assistance throughout the tour.",
            itinerary: [
                { day: 1, title: "Arrival Jaipur", desc: "Jaipur – Jaipur the PINK CITY of Indian and Popularly known as Pink city in Tourism world, pink colour is associated with hospitality in Rajasthan. So it is only appropriate that Jaipur, the Capital of the state be washed in this shade-spreading out the Pink Carpet for visitors. Planned by a young Bengali architect, Vidyadhar Bhattacharya, Jaipur was built by Maharaja Sawai Jai Singh II in 1727 A.D. Laid in a grid system, with straight avenues, roads, streets, lanes criss cross the city with rows of shops on either side of main bazaars arranged in nine rectangular city sectors (Chowkris). The planning of the city followed the principles of Shilpaslastra, an epochal treatise on Hindu architecture. Check in at hotel and evening free for independent activity Choki Dhani and over night stay at hotel ." },
                { day: 2, title: "Jaipur Sightseeing", desc: "After a Lovely Breakfast at hotel proceed for sightseeing tour of Pink City including Amer fort where you can enjoy elephant ride (Cost optional) and later City Palace Museum , Hawa Mahal & Jantar Mantar. After that you are free to explore the local Bazars and evening return back to hotel." },
                { day: 3, title: "Jaipur - Jodhpur ( 350 Kms )", desc: "After Lovely breakfast check out and continue drive to Jodhpur. Jodhpur the Sun City of India and also known as the Blue city. On Arrival check in at Hotel and in evening free for independent activity and return back to hotel for over night stay." },
                { day: 4, title: "Jodhpur - Jaisalmer ( 300 Kms )", desc: "After lovely breakfasts check out and proceed for onward journey towards Golden City Jaisalmer. Jaisalmer, the “ Golden City “ , is located on the westernmost frontiers of India in the state of Rajasthan the largest state of the country Close to the border of Pakistan. The city is known for its proximity to Thar Desert. The city is dominated by the Jaisalmer Fort, unlike most of the forts in the country this fort is a living fort. There are shops and hotels and age old havelies. After check in at hotel later visit Jain temple Manak Chowk and Havelis like Patwon ki Haveli and Jaisalmer Fort. Overnight stay." },
                { day: 5, title: "Jaisalmer - Jodhpur ( 300 Kms )", desc: "After breakfast check out and departure for onward journey for Jodhpur, proceed for city tour of jodhpur to Climb up the majestic Mehrangarh fort and explore the various sections within.Also visit the marble cenotaph at Jaswant Thada and visit Mandore Garden and over night at hotel." },
                { day: 6, title: "Jodhpur - Udaipur ( 265 Kms )", desc: "After breakfast check out and departure for onward journey for Udaipur also known as Lake City enroute visit Ranakpur Jain Temple. . After check in at your hotel for overnight stay." },
                { day: 7, title: "Udpaiur", desc: "After lovely breakfast, proceed for a city sightseeing tour of Udaipur. The city is built in 1559 A.D. by Maharaja Udai Singh and has been described as the most romantic city of Mewar Region on the banks of Lake Pichola and surrounded by the Hills of Aravali Mountains Range. The Aravalli Mountains is the oldest in the world after Himalayas. During your tour to city you will visit the City Palace, famous Jagdish Temple, Vintage car Museum , Sahelion Ki Bari the fountain Garden . Overnight at hotel." },
                { day: 8, title: "Udaipur Departure", desc: "After breakfast at your hotel check out and leave for onwards destination .Tours ends with fond memories." }
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
                        <p class="tl-desc">${item.desc}</p>
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
                _subject: `New Grand Holidays Booking: Rajasthan Heritage Tour`,
                name: document.getElementById('b-name').value,
                email: document.getElementById('b-email').value,
            _cc: document.getElementById('b-email').value,
                mobile: document.getElementById('b-mobile').value,
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
            .then(response => response.json())
        .then(data => {
            if (data.success || data.success === "true") {

                bookingForm.style.display = 'none';
                bookingSuccess.style.display = 'flex';
            
            } else {
                alert("Server Message: " + (data.message || "Email service requires activation. Please check mail@godwinhotels.com for an activation link."));
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
});