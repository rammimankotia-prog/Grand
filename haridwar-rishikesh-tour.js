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
                <div class="tl-circle">${idx + 1}</div>
                <div class="tl-body">
                    <div class="tl-head">
                        <h4 class="tl-title">${day.title}</h4>
                        <span class="day-tag time-tag">${day.stay}</span>
                    </div>
                    <p class="tl-desc">${day.desc}</p>
                    <p class="tl-desc" style="margin-top: 0.5rem; font-weight: 500; color: #8b6120;">🍲 ${day.meta}</p>
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
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerText;
            submitBtn.innerText = 'Sending...';
            submitBtn.disabled = true;

            const formData = {
                tourName: 'Haridwar & Rishikesh Spiritual Tour',
                name: document.getElementById('b-name').value,
                email: document.getElementById('b-email').value,
            _cc: document.getElementById('b-email').value,
                phone: document.getElementById('b-mobile').value,
                date: document.getElementById('b-date') ? document.getElementById('b-date').value : '',
                travelers: document.getElementById('b-travelers') ? document.getElementById('b-travelers').value : '',
                notes: document.getElementById('b-notes') ? document.getElementById('b-notes').value : ''
            };

            try {
                const response = await            // ── Required-field validation ────────────────────────────
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
 fetch('submit-booking.php', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });
                
                if (response.ok) {
                    form.style.display = 'none';
                    if (successMsg) {
                        successMsg.style.display = 'block';
                        successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                } else {
                    alert('There was a problem sending your request. Please check your details and try again.');
                    submitBtn.innerText = originalText;
                    submitBtn.disabled = false;
                }
            } catch (error) {
                alert('Network error. Please try again or contact us directly via email.');
                submitBtn.innerText = originalText;
                submitBtn.disabled = false;
            }
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
