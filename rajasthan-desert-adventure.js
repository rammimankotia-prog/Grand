document.addEventListener('DOMContentLoaded', () => {
    const tourModes = {
        car: {
            duration: "5 Days / 4 Nights",
            cities: "Jodhpur - Jaisalmer",
            price: "On Request",
            shortDesc: "The Rajasthan Desert Adventure Tour is an experience that lets you explore the vibrant cities of Jodhpur and Jaisalmer, featuring heritage forts and an overnight luxury camp in the Sam Sand Dunes.",
            highlight: "🚗 Includes dedicated premium A/C transport, daily breakfast, and complete assistance throughout the tour.",
            itinerary: [
                { day: 1, title: "Jodhpur Station / Airport – Jaisalmer (285 Km / 5 hrs)", desc: "Meet & Greet on arrival at Jodhpur Railway Station / Airport & transfer to Jaisalmer. Enroute visit Jaisalmer War Museum – The Jaisalmer War Museum is located 10 km short of Jaisalmer on the Jaisalmer – Jodhpur Highway. The unique museum has been designed with the view of honouring the contributions and sacrifices of war heroes, and to highlight their bravery. It also traces the evolution of the Indian Army. On arrival Check-in to hotel. Overnight stay at Jaisalmer." },
                { day: 2, title: "Jaisalmer Sightseeing & Sand Dunes", desc: "After breakfast visit the Jaisalmer Fort which is made by unique Golden Lime stone, that’s why its known as Golden Fort or Sonar Kella. After that visit Patwon-ki-haveli, Nathmal-ki-haveli, Salim singh-ki-Haveli. People still live in these ancient buildings dating from 12th to 15th century. After that also visit Gadishar Lake. In evening proceed for camel ride on Sam Sand Dunes & you can experience the spectacular view of Sun set in Thar desert.\n\nPackage Includes:\n• Traditional welcome with Aarti Tikka\n• Welcome Drink (Non-Alcoholic) On Arrival\n• One Camel Safari in the evening (Two pax each camel)\n• Evening Bonfire with cultural program & veg. snacks\n• Buffet Dinner & Buffet Breakfast (Fixed Menu)\n\nOvernight stay at Camp." },
                { day: 3, title: "Jaisalmer – Jodhpur (285 Km / 5 hrs)", desc: "After breakfast transfer to Jodhpur. On arrival check-in to your hotel. Overnight stay at Jodhpur." },
                { day: 4, title: "Jodhpur Local Sightseeing", desc: "After breakfast start for Jodhpur city tour. Covering Umaid Bhawan Palace Museum, Mehrangarh Fort- situated on a low sandstone hill. Within the fort visit Moti Mahal and Phool Mahal. Also visit Jaswant Thada – an imposing marble cenotaph built in memory of Maharaja Jaswant Singh II around 1899, Kaylana Lake and Mandore Garden. Evening free for leisure. Overnight stay at Jodhpur." },
                { day: 5, title: "Hotel – Jodhpur Railway Station / Airport", desc: "After breakfast check out from hotel and transfer to Jodhpur Railway Station / Airport for your onward journey." }
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
                _subject: `New Grand Holidays Booking: Rajasthan Desert Adventure Tour`,
                name: document.getElementById('b-name').value,
                email: document.getElementById('b-email').value,
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
});