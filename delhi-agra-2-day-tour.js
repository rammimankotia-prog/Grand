document.addEventListener('DOMContentLoaded', () => {
    // Delhi Agra 2-Day Tour Database
    const tourModes = {
        sedan: {
            price: "₹18,000 (For 2 Adults)",
            highlight: "🚗 Travel in comfort with a private Sedan (Toyota Etios/Dzire). Ideal for couples or solo travelers. Includes dedicated chauffeur, hotel pickup, and drop-off.",
        },
        suv: {
            price: "₹24,000 (For 3-4 Adults)",
            highlight: "🚙 Upgrade to a spacious SUV (Toyota Innova Crysta). Perfect for small families, offering extra legroom and a higher vantage point for sightseeing.",
        },
        minivan: {
            price: "₹32,000 (For 5-6 Adults)",
            highlight: "🚐 Experience luxury group travel in a premium Minivan (Tempo Traveller). Features push-back seats and superior comfort for larger families.",
        }
    };

    // UI Elements
    const tabButtons = document.querySelectorAll('.mode-tab-btn');
    const displayPrice = document.getElementById('display-price');
    const modeHighlightBox = document.getElementById('mode-highlight-box');
    const summaryPriceDisplay = document.getElementById('summary-price-display');
    const selectedModeInput = document.getElementById('selected-tour-mode');

    // Function to render active tour mode
    function updateTourDisplay(modeKey) {
        const modeData = tourModes[modeKey];
        if (!modeData) return;

        // Update price
        if(displayPrice) displayPrice.innerHTML = modeData.price;
        if(summaryPriceDisplay) summaryPriceDisplay.innerHTML = modeData.price;
        if(selectedModeInput) selectedModeInput.value = modeKey;

        // Highlight box
        if(modeHighlightBox) modeHighlightBox.innerHTML = modeData.highlight;
    }

    // Set Initial Load
    updateTourDisplay('sedan');

    // Tab Event Listeners
    if(tabButtons) {
        tabButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                tabButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                updateTourDisplay(btn.getAttribute('data-mode'));
            });
        });
    }

    // Mobile Navigation Toggle
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.querySelector('.nav-menu');
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }

    // Dropdown toggle for mobile viewports
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const navDropdown = document.querySelector('.nav-dropdown');
    if (dropdownToggle && navDropdown) {
        dropdownToggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                navDropdown.classList.toggle('active');
            }
        });
    }

    // Handle Form Booking Request
    
    

const bookingForm = document.getElementById('tourBookingForm');
    const successMessage = document.getElementById('bookingSuccessMessage');

    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const name = document.getElementById('b-name').value;
            const email = document.getElementById('b-email').value;
            const mobile = document.getElementById('b-mobile').value;
            const date = document.getElementById('b-date').value;
            const guests = document.getElementById('b-travelers').value;
                        const notes = document.getElementById('b-notes').value;
            const mode = selectedModeInput.value;

            const submitUrl = "submit-booking.php";

            // Client-side required-field validation
            if (!name || !email || !mobile || !date) {
                let missing = [];
                if (!name)   missing.push('Full Name');
                if (!email)  missing.push('Email Address');
                if (!mobile) missing.push('Mobile Number');
                if (!date)   missing.push('Preferred Date');
                alert('Please fill in the following required fields:\n\u2022 ' + missing.join('\n\u2022 '));
                if (submitBtn) { submitBtn.innerText = origBtnText; submitBtn.disabled = false; }
                return;
            }

            // ── Required-field validation ────────────────────────────
            if (!name || !email || !mobile || !date) {
                var missing = [];
                if (!name)   missing.push('Full Name');
                if (!email)  missing.push('Email Address');
                if (!mobile) missing.push('Mobile Number');
                if (!date)   missing.push('Preferred Date');
                alert('Please fill in the required fields:\n\u2022 ' + missing.join('\n\u2022 '));
                if (submitBtn) { submitBtn.innerText = origText; submitBtn.disabled = false; }
                return;
            }
            // ────────────────────────────────────────────────────────
            fetch(submitUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    _subject: `Grand Holidays - 2-Day Taj Mahal & Delhi Request`,
                    Name: name,
                    Email: email,
                    Mobile: mobile,
                    Preferred_Date: date,
                    Guests: guests,
                                        Selected_Mode: mode,
                    Additional_Notes: notes
                })
            })
            .then(response => response.json())
            .then(data => {
                bookingForm.style.display = 'none';
                successMessage.style.display = 'flex';
            })
            .catch(error => {
                console.error("Booking submit error: ", error);
                bookingForm.style.display = 'none';
                successMessage.innerHTML = `<h3>Request Submitted</h3><p>Your details were routed to our curator team. We will connect with you shortly.</p>`;
                successMessage.style.display = 'flex';
            });
        });
    }

    // FAQ Accordion
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
