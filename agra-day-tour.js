document.addEventListener('DOMContentLoaded', () => {

    // ── TOUR DATABASE ──────────────────────────────────────────────
    const tourModes = {
        sedan: {
            duration: "Same Day (≈14 Hours)",
            cities: "Delhi · Agra · Delhi",
            price: "$145 (For 2 Adults)",
            shortDesc: "Experience the timeless wonder of the Taj Mahal and the grandeur of Agra Fort on a fully private same-day drive from Delhi. Your dedicated chauffeur picks you up before dawn from Hotel Godwin Deluxe for a smooth Yamuna Expressway journey — returning you safely the same evening.",
            highlight: "🚗 Private AC sedan with professional chauffeur · Complimentary full breakfast in Agra · Pick-up & drop from Hotel Godwin Deluxe, Delhi",
            itinerary: [
                { time: "04:30 AM", title: "Pre-Dawn Pick-Up — Hotel Godwin Deluxe", desc: "Your private chauffeur arrives at Hotel Godwin Deluxe, Paharganj punctually at 04:30 AM. Begin your journey in a clean, air-conditioned sedan along the Yamuna Expressway while Delhi sleeps. Bottled water and light refreshments are provided for the journey." },
                { time: "07:30 AM", title: "Arrival at Taj Mahal — Eastern Gate", desc: "Arrive at the Eastern Gate of the Taj Mahal complex as Agra wakes to a golden sunrise. Your driver assists with parking while you proceed to purchase entry tickets directly at the gate (not included in the package). Step through the grand Darwaza-i-rauza gateway." },
                { time: "08:00 AM", title: "Taj Mahal — The White Marvel", desc: "Walk the full length of the central reflecting pool with the Taj Mahal framed perfectly before you. Marvel at the white Makrana marble mausoleum, the intricate pietra dura inlay work of precious stones, the soaring minarets, and the sweeping Yamuna River view from the rear terrace. Allow approximately 90 minutes inside the complex." },
                { time: "10:00 AM", title: "Complimentary Breakfast in Agra", desc: "Following your Taj Mahal visit, proceed to a curated local restaurant for your complimentary full breakfast — included in your package. Enjoy a spread of North Indian and continental dishes before the next monument." },
                { time: "11:30 AM", title: "Agra Fort — The Red Citadel", desc: "Drive 3 km to the magnificent Agra Fort (UNESCO World Heritage Site). Explore the Diwan-i-Am (Hall of Public Audience), the ornate Diwan-i-Khas, Khas Mahal, and the poignant Musamman Burj — the tower where Emperor Shah Jahan, imprisoned by his own son, spent his final years gazing at the Taj Mahal across the Yamuna. Entry tickets purchased at gate — not included." },
                { time: "02:30 PM", title: "Return Drive to Hotel Godwin Deluxe", desc: "Begin the comfortable return journey along the Yamuna Expressway. Estimated arrival back at Hotel Godwin Deluxe, Paharganj: 05:30–06:00 PM, subject to traffic. Your driver ensures a smooth, unhurried return." }
            ],
            inclusions: [
                "Private air-conditioned Sedan (Toyota Etios / Maruti Ciaz or similar)",
                "Dedicated professional English-speaking chauffeur",
                "Pick-up & drop-off at Hotel Godwin Deluxe, Paharganj, Delhi",
                "One complimentary full breakfast in Agra",
                "All toll charges, parking fees & vehicle fuel",
                "Bottled water in vehicle throughout the day"
            ],
            exclusions: [
                "Taj Mahal entry ticket (approx. ₹1,300/person for foreign nationals)",
                "Agra Fort entry ticket (approx. ₹650/person for foreign nationals)",
                "Lunch and all personal expenses",
                "Personal travel / medical insurance",
                "Guide fees (available as optional add-on)",
                "Any monument or site fees not listed above"
            ]
        },
        suv: {
            duration: "Same Day (≈14 Hours)",
            cities: "Delhi · Agra · Delhi",
            price: "$230 (For 2 Adults)",
            shortDesc: "Elevate your Agra day trip with a spacious Toyota Innova Crysta and a Ministry of Tourism-certified private historian guide. Your guide transforms every monument into a living story — the political intrigue, the architectural genius, and the eternal love behind the world's greatest mausoleum.",
            highlight: "🚙 Premium Innova Crysta SUV · Ministry of Tourism certified historian guide · Complimentary breakfast · Mehtab Bagh visit included",
            itinerary: [
                { time: "04:30 AM", title: "Pre-Dawn Departure — Hotel Godwin Deluxe", desc: "Your private Innova Crysta and Ministry of Tourism-certified historian guide arrive at Hotel Godwin Deluxe, Paharganj at 04:30 AM. Your guide begins an engaging briefing on Mughal history and Shah Jahan's architectural vision as you glide along the Yamuna Expressway — the best possible preparation for the wonders ahead." },
                { time: "07:30 AM", title: "Taj Mahal — Expert-Guided Entry", desc: "Arrive at the Eastern Gate as early morning light kisses the Taj Mahal dome. Your historian guide accompanies you through the full complex — revealing the optical illusion of the inward-leaning minarets, the 28 types of precious stones used in the inlay work, the geometry of the Mughal garden, and the deeply personal story of Shah Jahan's 22-year project of grief. Entry tickets purchased at gate — not included." },
                { time: "08:00 AM", title: "Taj Mahal — Deep Exploration", desc: "Spend a full 90–100 minutes inside the complex with your historian. Walk the full ornamental waterway, visit the mosque and the jawab (its mirror image), enter the main mausoleum chamber, and photograph the Taj from the rear riverside terrace as morning light bathes the marble in gold. Your guide ensures you miss nothing." },
                { time: "10:00 AM", title: "Curated Breakfast in Agra", desc: "A complimentary gourmet breakfast at a Taj-view restaurant in Agra — a freshly prepared spread of North Indian and continental dishes served with the monument you just visited visible on the horizon. A peaceful, unhurried pause before the next chapter." },
                { time: "11:30 AM", title: "Agra Fort — Expert Royal Court Narration", desc: "Your historian transforms Agra Fort from a red sandstone ruin into a living Mughal court. Walk through the Diwan-i-Khas where Akbar held court, stand in Musamman Burj where Shah Jahan breathed his last, and visualise the zenana quarters from archaeological evidence. This is history as it should be told. Entry ticket purchased at gate." },
                { time: "01:30 PM", title: "Mehtab Bagh — The Moonlit Garden", desc: "A unique addition: your guide takes you to Mehtab Bagh, the Mughal 'moonlit garden' located directly across the Yamuna from the Taj Mahal. This vantage point offers the finest reverse-angle view of the monument — exactly the perspective Shah Jahan intended for the black marble Taj he never built. Entry ticket at gate." },
                { time: "03:00 PM", title: "Return to Hotel Godwin Deluxe", desc: "Depart Agra and return comfortably via the Yamuna Expressway. Estimated arrival at Hotel Godwin Deluxe: 06:00–06:30 PM. Your historian continues to answer any questions on the return journey." }
            ],
            inclusions: [
                "Private Toyota Innova Crysta SUV with professional chauffeur",
                "Ministry of Tourism-certified private historian guide (English)",
                "Pick-up & drop-off at Hotel Godwin Deluxe, Paharganj, Delhi",
                "One complimentary gourmet breakfast at Taj-view restaurant",
                "Mehtab Bagh visit (time permitting, entry ticket at gate)",
                "All toll charges, parking fees & vehicle fuel",
                "Bottled water & refreshments in vehicle throughout"
            ],
            exclusions: [
                "Taj Mahal entry ticket (approx. ₹1,300/person for foreign nationals)",
                "Agra Fort entry ticket (approx. ₹650/person for foreign nationals)",
                "Mehtab Bagh entry ticket (approx. ₹200/person for foreign nationals)",
                "Lunch and all personal expenses",
                "Personal travel / medical insurance",
                "Tips & gratuities for guide and driver (customary)"
            ]
        },
        luxury: {
            duration: "Same Day (≈15 Hours)",
            cities: "Delhi · Agra · Delhi",
            price: "$390 (For 2 Adults)",
            shortDesc: "The ultimate same-day Agra experience — a chauffeur-driven Mercedes E-Class or Audi A6, a senior art historian guide, complimentary gourmet breakfast and a three-course Taj-view lunch, and full-day VIP curation. Reserved for guests who demand nothing less than perfection.",
            highlight: "🏆 Mercedes E-Class / Audi A6 · Senior art historian · Gourmet breakfast & Taj-view 3-course lunch · Full-day private curation",
            itinerary: [
                { time: "04:15 AM", title: "VIP Dawn Departure — Hotel Godwin Deluxe", desc: "Your senior chauffeur arrives at Hotel Godwin Deluxe, Paharganj at 04:15 AM in a gleaming Mercedes E-Class or Audi A6, pre-stocked with fresh fruit, premium hot coffee and tea, chilled mineral water, and morning newspapers. Your senior art historian accompanies you from the outset, delivering an engaging private lecture on Mughal dynasty history, Shah Jahan's architectural vision, and the 22-year story of the Taj Mahal's construction." },
                { time: "07:15 AM", title: "Taj Mahal at First Light", desc: "Arrive at the Eastern Gate at 07:15 AM to experience the Taj Mahal in the purest, most magical morning light — before the midday sun and tourist masses arrive. Your art historian guides you with forensic depth: the mathematical precision of the symmetrical Persian-style charbagh garden, the calligraphic Quranic inscriptions framing each archway, the illusion of depth created by the tapering minarets, and the shifting colour of the dome — pearl-white at dawn, soft gold by mid-morning. Entry tickets purchased at gate." },
                { time: "08:30 AM", title: "Exclusive Photography Circuit", desc: "Your historian curates the ultimate photography circuit: the central pool reflection at 08:30 AM (ideal golden light), the rear riverside terrace view with the Yamuna flowing peacefully behind the mausoleum, and close-up detail shots of the pietra dura — hand-carved marble flowers with petals of lapis lazuli, malachite, and amber. You depart with extraordinary photographs and richer memories." },
                { time: "10:00 AM", title: "Gourmet Breakfast with Taj View", desc: "A complimentary curated breakfast at Agra's finest Taj-view rooftop restaurant — a seasonal spread of freshly prepared North Indian and continental dishes, freshly squeezed tropical juices, artisan coffee, and Agra's famous petha sweets. The Taj Mahal dome is visible on the horizon as you dine. An extraordinary morning tableau." },
                { time: "11:30 AM", title: "Agra Fort — Royal Court Immersion", desc: "Your art historian leads an immersive, deeply personal tour of Agra Fort — Akbar's architectural ambition expressed in blood-red Rajasthan sandstone. Walk through the Diwan-i-Am where Akbar held public court, the Diwan-i-Khas where the Peacock Throne once stood, and the devastatingly poignant Musamman Burj where Shah Jahan — under house arrest by his own son Aurangzeb — gazed at the Taj Mahal until his death in 1666. Entry ticket purchased at gate." },
                { time: "01:30 PM", title: "Three-Course Taj-View Lunch", desc: "A complimentary three-course gourmet lunch at a premium rooftop restaurant with unobstructed Taj Mahal dome views. Curated seasonal North Indian cuisine — featuring Awadhi dum biryani, kebab platters, and traditional desserts — accompanied by fresh lime water and regional specialities. One of Agra's finest culinary experiences, reserved exclusively for your table." },
                { time: "02:30 PM", title: "Mehtab Bagh — The Hidden Garden", desc: "After lunch, your historian takes you to Mehtab Bagh — Shah Jahan's 'Moonlit Garden' on the opposite bank of the Yamuna, offering the only reverse-angle panoramic view of the Taj Mahal that Shah Jahan himself designed. The late-afternoon light and the riverine mist create an ethereal scene unlike anything seen from inside the complex." },
                { time: "03:30 PM", title: "Return to Hotel Godwin Deluxe", desc: "Depart Agra in your luxury vehicle for a relaxed, conversation-filled return journey along the Yamuna Expressway. Estimated arrival at Hotel Godwin Deluxe: 06:30–07:00 PM. Your historian answers final questions, and your concierge ensures your day is perfectly rounded off." }
            ],
            inclusions: [
                "Private Mercedes E-Class or Audi A6 with senior professional chauffeur",
                "Senior Ministry of Tourism-certified art historian guide (English)",
                "Pick-up & drop-off at Hotel Godwin Deluxe, Paharganj, Delhi",
                "One complimentary gourmet breakfast at Taj-view restaurant",
                "One complimentary three-course Taj-view lunch at curated restaurant",
                "Mehtab Bagh visit included",
                "All toll charges, parking fees & vehicle fuel",
                "In-vehicle premium refreshment kit (coffee, tea, fresh fruit, mineral water)",
                "24/7 ground support and on-call concierge assistance"
            ],
            exclusions: [
                "Taj Mahal entry ticket (approx. ₹1,300/person for foreign nationals)",
                "Agra Fort entry ticket (approx. ₹650/person for foreign nationals)",
                "Mehtab Bagh entry ticket (approx. ₹200/person for foreign nationals)",
                "Personal travel / medical insurance",
                "Tips & gratuities (customary)",
                "Any services not specifically listed in inclusions"
            ]
        }
    };

    // ── UPDATE DISPLAY ─────────────────────────────────────────────
    function updateTourDisplay(mode) {
        const data = tourModes[mode];
        if (!data) return;

        // Header stats
        document.getElementById('display-duration').textContent  = data.duration;
        document.getElementById('display-cities').textContent    = data.cities;
        document.getElementById('display-price').textContent     = data.price;

        // Description & Highlight
        document.getElementById('tour-short-desc').textContent = data.shortDesc;
        document.getElementById('mode-highlight-box').innerHTML =
            `<div class="highlight-pill">✦ ${data.highlight}</div>`;

        // Sidebar price
        document.getElementById('summary-price-display').textContent = data.price;

        // Itinerary timeline
        const itHtml = data.itinerary.map(item => `
            <div class="timeline-item">
                <div class="timeline-day">${item.time}</div>
                <div class="timeline-content">
                    <h4>${item.title}</h4>
                    <p>${item.desc}</p>
                </div>
            </div>
        `).join('');
        document.getElementById('itinerary-timeline-box').innerHTML = itHtml;

        // Inclusions
        document.getElementById('inclusions-list').innerHTML =
            data.inclusions.map(i => `<li><span class="ie-check">✓</span>${i}</li>`).join('');

        // Exclusions
        document.getElementById('exclusions-list').innerHTML =
            data.exclusions.map(e => `<li><span class="ie-cross">✗</span>${e}</li>`).join('');

        // Update selected-tour-mode hidden input
        const modeInput = document.getElementById('selected-tour-mode');
        if (modeInput) modeInput.value = mode;

        // Active tab styling
        document.querySelectorAll('.mode-tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
    }

    // ── MODE TAB BUTTONS ───────────────────────────────────────────
    document.querySelectorAll('.mode-tab-btn').forEach(btn => {
        btn.addEventListener('click', () => updateTourDisplay(btn.dataset.mode));
    });

    // ── INIT DEFAULT ───────────────────────────────────────────────
    updateTourDisplay('sedan');

    // ── BOOKING FORM ───────────────────────────────────────────────
    
    

const bookingForm       = document.getElementById('tourBookingForm');
    const successMessage    = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const mode     = document.getElementById('selected-tour-mode').value;
            const name     = document.getElementById('b-name').value.trim();
            const email    = document.getElementById('b-email').value.trim();
            const mobile = document.getElementById('b-mobile').value;
            const date     = document.getElementById('b-date').value.trim();
            const travelers= document.getElementById('b-travelers').value;
            const notes    = document.getElementById('b-notes').value.trim();

            const subject  = encodeURIComponent(`Same Day Agra Tour Enquiry — ${tourModes[mode].price}`);
            const body     = encodeURIComponent(
                `Tour: Same Day Agra Tour from Delhi\nMode: ${mode.charAt(0).toUpperCase()+mode.slice(1)}\nPrice: ${tourModes[mode].price}\n\nName: ${name}\nEmail: ${email}\nMobile: ${mobile}\nTravel Date: ${date}\nGuests: ${travelers}\n\nSpecial Notes:\n${notes}`
            );

            const mailtoLink = `mailto:info@grandholidaytours.com?subject=${subject}&body=${body}`;

            fetch(mailtoLink).catch(() => {});
            window.location.href = mailtoLink;

            setTimeout(() => {
                bookingForm.style.display = 'none';
                successMessage.style.display = 'flex';
            }, 600);
        });
    }

    // ── MOBILE NAV DROPDOWN ────────────────────────────────────────
    document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = toggle.closest('.nav-dropdown');
                if (parent) parent.classList.toggle('active');
            }
        });
    });

    // ── FAQ ACCORDION ──────────────────────────────────────────────
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const answer = btn.nextElementSibling;
            const isOpen = btn.classList.contains('open');
            document.querySelectorAll('.faq-question.open').forEach(other => {
                if (other !== btn) {
                    other.classList.remove('open');
                    other.setAttribute('aria-expanded', 'false');
                    other.nextElementSibling.classList.remove('open');
                }
            });
            btn.classList.toggle('open', !isOpen);
            btn.setAttribute('aria-expanded', String(!isOpen));
            answer.classList.toggle('open', !isOpen);
        });
    });

});
