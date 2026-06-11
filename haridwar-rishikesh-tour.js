document.addEventListener('DOMContentLoaded', () => {

    const tourData = {
        highlights: [
            "Witness divine Ganga Aarti at Har Ki Pauri in Haridwar.",
            "Visit Mansa Devi & Chandi Devi temples for spiritual blessings.",
            "Explore sacred sites like Daksh Prajapati Temple & Ashrams.",
            "Short trip to Rishikesh covering Ram Jhula & Laxman Jhula.",
            "Enjoy peaceful ghats, spiritual vibes & holy river views."
        ],
        itinerary: [
            {
                day: "Day 1",
                location: "Haridwar",
                title: "Arrive Delhi – Haridwar",
                stay: "1 Night",
                desc: "Upon arrival at Delhi airport/ Railway station our executive will receive you with warm welcome. Our representative will take you to Haridwar. Reach in Haridwar check into the hotel and have some rest. By evening you can attend a heart-touching aarti in Har-Ki-Pauri which is believed to be the place where elixir of immortality Nector (Amrit) fell during Samundra Manthan. Later back to the hotel, have some delicious food and stay overnight.",
                meta: "Accommodation & Dinner Only"
            },
            {
                day: "Day 2",
                location: "Haridwar",
                title: "Haridwar Local + Rishikesh Day Trip",
                stay: "1 Night",
                desc: "After having breakfast, proceed to Haridwar Local Sightseeing. Places to visit will be Daksh Prajapati temple, Ananandamai Ashram, Mata Chanda Devi Temples, Mansa Devi, and Parmarth. Later take a short drive from Haridwar to Rishikesh (20 Kms) while enroute covering Bhuma Niketan and Bharat Mata Mandir. In Rishikesh major attraction to cover will be Ram Jhula & Laxman Jhula. Later it is time to return to Haridwar for an overnight stay. Note: Adventure activities at your own cost.",
                meta: "Accommodation, Breakfast & Lunch or Dinner"
            },
            {
                day: "Day 3",
                location: "Haridwar",
                title: "Haridwar – Delhi Departure",
                stay: "Departure",
                desc: "After a healthy breakfast check out from the hotel of Haridwar. Our representative will take you back to Delhi's Airport/ Railway station for dropping. Take with you good memories with blessings.",
                meta: "Breakfast Only"
            }
        ],
        inclusions: [
            "Pick-up and drop from Delhi Airport/railway station/Bus Stop.",
            "Stay for 2 adults in 1 double room (base category).",
            "2 Breakfasts & 2 Dinners (MAP Plan).",
            "All sightseeing and transfers by private Non-AC Sedan car.",
            "(AC not used in hilly areas. Extra charge if needed in hills – paid to driver).",
            "Parking, fuel, toll tax & driver charges – included.",
            "All taxes included (except GST)."
        ],
        exclusions: [
            "Flights, Trains, Ferries etc.",
            "Monument Entrance Fees & Camera Fees.",
            "Parking Inside Monuments / Parks / Temples Etc.",
            "Personal Expenses - Laundry, Shopping, Telephone bills, tips etc.",
            "Adventure Activities - Safari, Rides, Surfing, Paragliding etc.",
            "Any Extra services - Permits, Volvo Luggage Charges, Heater, Meals etc.",
            "Anything else not listed in above details."
        ]
    };

    const highlightsBox = document.getElementById('mode-highlight-box');
    if(highlightsBox) {
        highlightsBox.innerHTML = `
            <ul style="list-style-type: disc; padding-left: 1.2rem; display: flex; flex-direction: column; gap: 0.5rem;">
                ${tourData.highlights.map(h => `<li style="display: list-item;">${h}</li>`).join('')}
            </ul>
        `;
    }

    const timelineBox = document.getElementById('itinerary-timeline-box');
    if(timelineBox) {
        timelineBox.innerHTML = tourData.itinerary.map((day, idx) => `
            <div class="timeline-day-block">
                <div class="timeline-day-number">${idx + 1}</div>
                <div class="timeline-day-title-wrapper">
                    <div class="timeline-day-title">
                        <h4>${day.title}</h4>
                        <span class="day-tag time-tag">${day.stay}</span>
                    </div>
                    <p class="timeline-day-desc">${day.desc}</p>
                    <div style="font-size:0.8rem; color:#8b6120; font-weight:600; margin-top:0.4rem;">
                        🍲 ${day.meta}
                    </div>
                </div>
            </div>
        `).join('');
    }

    const incList = document.getElementById('inclusions-list');
    if(incList) {
        incList.innerHTML = tourData.inclusions.map(inc => `<li>${inc}</li>`).join('');
    }

    const excList = document.getElementById('exclusions-list');
    if(excList) {
        excList.innerHTML = tourData.exclusions.map(exc => `<li>${exc}</li>`).join('');
    }

    const form = document.getElementById('tourBookingForm');
    const successMsg = document.getElementById('bookingSuccessMessage');
    
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            form.style.display = 'none';
            if (successMsg) successMsg.style.display = 'block';
        });
    }
});
