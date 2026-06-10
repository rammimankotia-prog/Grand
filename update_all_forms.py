import os
import glob
import re

html_files = glob.glob("*.html")
js_files = glob.glob("*.js")

new_date_html = """                            <div class="sidebar-form-group">
                                <input type="date" id="b-date" required class="sidebar-input date-input" style="padding-top: 1rem; cursor: pointer;">
                                <label for="b-date" class="sidebar-label" style="top: -0.4rem; font-size: 0.7rem; background: #FFFEFB; padding: 0 0.4rem; color: #6B5F54; font-weight: 700; letter-spacing: 1px;">Preferred Date</label>
                            </div>"""

new_guests_html = """                            <div class="sidebar-form-group guest-counter-group" style="margin-top: 1.5rem; position: relative;">
                                <label class="sidebar-label" style="top: -0.8rem; font-size: 0.7rem; background: #FFFEFB; padding: 0 0.4rem; color: #6B5F54; font-weight: 700; letter-spacing: 1px;">Number of Guests</label>
                                <div class="guest-counter" style="display: flex; align-items: center; border: 1px solid rgba(24,19,14,0.1); border-radius: 8px; overflow: hidden; background: #FFFEFB;">
                                    <button type="button" class="btn-guest-minus" style="background: rgba(166,124,49,0.05); border: none; color: #A67C31; width: 45px; height: 48px; font-size: 1.4rem; font-weight: 300; cursor: pointer; transition: background 0.2s;">-</button>
                                    <input type="number" id="b-travelers" value="2" min="1" max="16" class="sidebar-input guest-input" readonly style="border: none !important; text-align: center; flex-grow: 1; padding: 0 !important; font-size: 1.1rem !important; font-weight: 600; color: #18130E; -moz-appearance: textfield; pointer-events: none;">
                                    <button type="button" class="btn-guest-plus" style="background: rgba(166,124,49,0.05); border: none; color: #A67C31; width: 45px; height: 48px; font-size: 1.4rem; font-weight: 300; cursor: pointer; transition: background 0.2s;">+</button>
                                </div>
                            </div>"""

new_email_and_mobile_html = """                            <div class="sidebar-form-group">
                                <input type="email" id="b-email" required placeholder=" " class="sidebar-input">
                                <label for="b-email" class="sidebar-label">Email Address</label>
                            </div>

                            <div class="sidebar-form-group">
                                <input type="tel" id="b-mobile" required placeholder=" " class="sidebar-input">
                                <label for="b-mobile" class="sidebar-label">Mobile Number</label>
                            </div>"""

guest_js = """
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

"""

for f in html_files:
    if f == 'index.html' or f == '5-days-golden-triangle-tour.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="b-email"' not in content:
        continue
        
    # Replace Email -> Email + Mobile
    email_regex = re.compile(r'<div class="sidebar-form-group">\s*<input type="email" id="b-email" required placeholder=" " class="sidebar-input">\s*<label for="b-email" class="sidebar-label">Email Address</label>\s*</div>')
    content = email_regex.sub(new_email_and_mobile_html, content)
    
    # Replace Date
    date_regex = re.compile(r'<div class="sidebar-form-group">\s*<input type="text" id="b-date" required placeholder=" " class="sidebar-input">\s*<label for="b-date" class="sidebar-label">Preferred Date of Travel</label>\s*</div>')
    content = date_regex.sub(new_date_html, content)
    
    # Replace Travelers
    travelers_regex = re.compile(r'<div class="sidebar-form-group">\s*<select id="b-travelers" class="sidebar-input select-input" required>.*?</select>\s*<label for="b-travelers" class="sidebar-label">Number of Guests</label>\s*</div>', re.DOTALL)
    content = travelers_regex.sub(new_guests_html, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)


for f in js_files:
    if f == '5-days-golden-triangle-tour.js':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'b-travelers' not in content:
        continue
        
    # Add JS Logic
    if 'guest-counter-group' not in content and 'const guestMinus' not in content:
        content = re.sub(r'(const\s+bookingForm\s*=\s*document\.getElementById\(\'tourBookingForm\'\);)', guest_js + r'\1', content)
        
    # Add mobile variable
    if 'b-mobile' not in content:
        # Pattern 1: const email = document.getElementById('b-email').value;
        content = re.sub(r'(const\s+email\s*=\s*document\.getElementById\(\'b-email\'\)\.value.*?;)', r"\1\n            const mobile = document.getElementById('b-mobile').value;", content)
        
        # Pattern 2: email: document.getElementById('b-email').value,
        content = re.sub(r'(email:\s*document\.getElementById\(\'b-email\'\)\.value.*?,)', r"\1\n                mobile: document.getElementById('b-mobile').value,", content)
        
        # Pattern 3 payload injection (if it's using Email: email)
        content = re.sub(r'(Email:\s*email,)', r"\1\n                    Mobile: mobile,", content)
        
        # Pattern 4 mailto injection
        content = re.sub(r'(\\nEmail:\s*\$\{email\})', r"\1\\nMobile: ${mobile}", content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
