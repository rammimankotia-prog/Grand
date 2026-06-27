document.addEventListener('DOMContentLoaded', () => {
    // Tour Options Database
    const tourModes = {
        flight: {
            duration: "8 Days / 7 Nights",
            cities: "Delhi - Agra - Jaipur - Varanasi",
            price: "₹22,050 per person",
            shortDesc: "Experience the majestic Golden Triangle combined with the spiritual heart of India. This luxury itinerary includes private chauffeured drives and short domestic flights, allowing you to absorb India's beauty and profound spirituality at your own pace.",
            highlight: "✈️ Includes domestic flights (Jaipur - Varanasi, Varanasi - Delhi), dedicated private car for city tours, and an unforgettable sunrise boat ride on the sacred Ganges.",
            itinerary: [
                { day: 1, title: "Arrival & Welcome to Delhi", desc: "Touch down in the vibrant capital, Delhi. You will be warmly greeted at the airport and chauffeured to Hotel Godwin Deluxe, your premium stay in the heart of the city. Take the evening to rest, relax, and prepare for the incredible journey ahead." },
                { day: 2, title: "Delhi Sightseeing: Historic Marvels", desc: "After a hearty breakfast at Hotel Godwin Deluxe, dive into the heart of India's capital. Explore magnificent landmarks including ancient mosques, bustling heritage markets, towering historical forts, and the iconic India Gate and Qutub Minar." },
                { day: 3, title: "Delhi to Agra: The Mughal Capital", desc: "Enjoy a comfortable private drive to the historical city of Agra. After checking into your hotel, spend the afternoon exploring the massive, red-sandstone Agra Fort, a testament to the grandeur of the Mughal Empire." },
                { day: 4, title: "Sunrise at Taj Mahal & Drive to Jaipur", desc: "Witness the ethereal beauty of the Taj Mahal bathed in the soft glow of sunrise. Afterwards, embark on a scenic drive to the 'Pink City' of Jaipur, pausing en route to explore the fascinating abandoned ghost city of Fatehpur Sikri." },
                { day: 5, title: "Explore Jaipur: The Pink City", desc: "Spend the day immersed in royal Rajasthani heritage. Ascend the majestic Amber Fort, wander through the opulent City Palace, and marvel at the intricate facade of the famous Hawa Mahal (Palace of Winds)." },
                { day: 6, title: "Flight to Varanasi & Spiritual Evening", desc: "Board a short domestic flight from Jaipur to Varanasi, the spiritual capital of India. In the evening, head to the sacred riverbanks to witness the mesmerizing Ganga Aarti—a beautiful, deeply spiritual ceremony of light and chanting." },
                { day: 7, title: "Varanasi: Sunrise Boat Ride & Sarnath", desc: "Experience profound tranquility during a sunrise boat ride on the holy River Ganges. Later, walk through the ancient, labyrinthine alleys of the old city and visit Sarnath, the deeply historic site where Lord Buddha delivered his first sermon." },
                { day: 8, title: "Fly back to Delhi & Departure", desc: "Conclude your incredible spiritual and historical journey with a flight from Varanasi back to Delhi, where you will seamlessly connect to your onward flight or final destination." }
            ],
            inclusions: [
                "Pickup and drop-off at hotels and airports in Delhi",
                "7 nights accommodation in a 3, 4, or 5-star hotel (as per preference)",
                "Breakfast at Hotel",
                "Round Trip Flight Ticket (Jaipur - Varanasi | Varanasi - Delhi)",
                "All Sightseeing by private Air Conditioned Car",
                "Professional Local tour guide in each city destination",
                "Morning boat ride on the holy river Ganges in Varanasi",
                "Battery Rickshaw ride at Taj Mahal",
                "Daily Water Bottle",
                "Hotel/airport pick-up and drop-off"
            ],
            exclusions: [
                "Entrance Tickets of all Monuments",
                "Lunches and dinners",
                "Tips (optional)"
            ],
            highlightsList: [
                "Discover the major sites such as Taj Mahal and River Ganges",
                "Explore Indian culture including Jaipur and Varanasi",
                "See the amazing views of Ganga Aarti Ceremony at Varanasi",
                "On the way to Jaipur, pause in Fatehpur Sikri.",
                "Savor the bright flavors of Indian food"
            ]
        }
    };

    let currentMode = 'flight'; // Default to flight mode
    
    // Elements to update
    const displayDuration = document.getElementById('display-duration');
    const displayCities = document.getElementById('display-cities');
    const displayPrice = document.getElementById('display-price');
    const summaryPriceDisplay = document.getElementById('summary-price-display');
    const shortDesc = document.getElementById('tour-short-desc');
    const modeHighlightBox = document.getElementById('mode-highlight-box');
    const timelineBox = document.getElementById('itinerary-timeline-box');
    const inclusionsBox = document.getElementById('inclusions-list');
    const exclusionsBox = document.getElementById('exclusions-list');
    
    function renderTourData(mode) {
        const modeData = tourModes[mode];
        if (!modeData) return;

        displayDuration.innerText = modeData.duration;
        displayCities.innerText = modeData.cities;
        displayPrice.innerText = `From ${modeData.price}`;
        summaryPriceDisplay.innerText = `${modeData.price}`;
        shortDesc.innerText = modeData.shortDesc;
        
        // Render highlight block
        modeHighlightBox.innerHTML = `
            <div class="highlight-card">
                <p>${modeData.highlight}</p>

            </div>
        `;

        
        // Render split highlights
        const highlightsSplitBox = document.getElementById('tour-highlights-list-split');
        if (highlightsSplitBox && modeData.highlightsList) {
            highlightsSplitBox.innerHTML = modeData.highlightsList.map(h => `
                <li>
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                    ${h}
                </li>
            `).join('');
        }

        // Render timeline
        timelineBox.innerHTML = modeData.itinerary.map(item => `
            <div class="timeline-day-block">
                <div class="timeline-day-number">${item.day}</div>
                <div class="timeline-day-title-wrapper">
                    <div class="timeline-day-title">
                        <span class="day-tag">Day ${item.day}</span>
                        <h4>${item.title}</h4>
                    </div>
                    <p class="timeline-day-desc">${item.desc}</p>
                </div>
            </div>
        `).join('');

        // Render inclusions
        inclusionsBox.innerHTML = modeData.inclusions.map(inc => `
            <li>
                <svg class="inc-icon check" width="20" height="20" style="flex-shrink: 0; margin-top: 1px;" fill="none" stroke="#16a34a" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>${inc}</span>
            </li>
        `).join('');

        // Render exclusions
        exclusionsBox.innerHTML = modeData.exclusions.map(exc => `
            <li>
                <svg class="inc-icon cross" width="20" height="20" style="flex-shrink: 0; margin-top: 1px;" fill="none" stroke="#dc2626" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg>
                <span>${exc}</span>
            </li>
        `).join('');
    }

    renderTourData(currentMode);

    // Make mode switcher hidden since we only have one mode for this tour
    const modeTabs = document.querySelector('.mode-tabs');
    if (modeTabs) {
        modeTabs.style.display = 'none';
    }

    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const answer = item.querySelector('.faq-answer');
            const isOpen = question.classList.contains('open');
            
            faqItems.forEach(i => {
                i.querySelector('.faq-question').classList.remove('open');
                i.querySelector('.faq-answer').classList.remove('open');
            });

            if (!isOpen) {
                question.classList.add('open');
                answer.classList.add('open');
            }
        });
    });
\n
    // Form Booking Handler
    const bookingForm = document.getElementById('tourBookingForm');
    const successMessage = document.getElementById('bookingSuccessMessage');
    
    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = bookingForm.querySelector('button[type="submit"]') || bookingForm.querySelector('.btn-sidebar-submit');
            var origText = submitBtn ? submitBtn.innerText : 'Submit';
            if (submitBtn) {
                submitBtn.innerText = 'Sending...';
                submitBtn.disabled = true;
            }

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

            const data = {
                _subject: 'Grand Holidays Booking Request',
                name: valName,
                email: valEmail,
                mobile: valMobile,
                preferredDate: valDate,
                guestsCount: document.getElementById('b-travelers') ? document.getElementById('b-travelers').value : '',
                message: document.getElementById('b-notes') ? document.getElementById('b-notes').value.trim() : '',
                estimatedPrice: document.getElementById('summary-price-display') ? document.getElementById('summary-price-display').innerText : ''
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
                if (data.success || data.success === 'true' || data.success === true) {
                    bookingForm.style.display = 'none';
                    if (successMessage) successMessage.style.display = 'flex';
                } else {
                    alert('Could not send request: ' + (data.message || 'Please try again or contact us directly.'));
                    if (submitBtn) {
                        submitBtn.innerText = origText;
                        submitBtn.disabled = false;
                    }
                }
            })
            .catch(error => {
                console.error('Booking submit error: ', error);
                bookingForm.style.display = 'none';
                if (successMessage) {
                    successMessage.innerHTML = '<h3>Request Received</h3><p>Your details were routed to our curator team. We will connect with you shortly.</p>';
                    successMessage.style.display = 'flex';
                }
            });
        });
    }
\n});\n