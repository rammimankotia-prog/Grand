"""
patch_missing_handlers.py
Adds missing JS form handlers to specific files
"""
import os, re

SITE_DIR = r"c:\xampp\htdocs\Grand"
files = [
    "4-days-golden-triangle-tour.js",
    "8-days-golden-triangle-varanasi-tour.js"
]

HANDLER = """
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
                alert('Please fill in the required fields:\\n\\u2022 ' + missing.join('\\n\\u2022 '));
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
"""

for fname in files:
    fpath = os.path.join(SITE_DIR, fname)
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'tourBookingForm' in content:
        print(f'{fname} already has form handler')
        continue
        
    idx = content.rfind('});')
    if idx != -1:
        new_content = content[:idx] + '\\n' + HANDLER + '\\n});\\n'
    else:
        new_content = content + '\\n' + HANDLER + '\\n'
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Patched {fname}')

