import re

# 1. Update HTML
with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_date_html = """                            <div class="sidebar-form-group">
                                <input type="text" id="b-date" required placeholder=" " class="sidebar-input">
                                <label for="b-date" class="sidebar-label">Preferred Date of Travel</label>
                            </div>"""

new_date_html = """                            <div class="sidebar-form-group">
                                <input type="date" id="b-date" required class="sidebar-input date-input" style="padding-top: 1rem; cursor: pointer;">
                                <label for="b-date" class="sidebar-label" style="top: -0.4rem; font-size: 0.7rem; background: #FFFEFB; padding: 0 0.4rem; color: #6B5F54; font-weight: 700; letter-spacing: 1px;">Preferred Date</label>
                            </div>"""

old_guests_html = """                            <div class="sidebar-form-group">
                                <select id="b-travelers" class="sidebar-input select-input" required>
                                    <option value="" disabled selected hidden></option>
                                    <option value="1">1 Traveler</option>
                                    <option value="2">2 Travelers (Double Sharing)</option>
                                    <option value="3-5">3 - 5 Travelers</option>
                                    <option value="6+">6+ Travelers (Private Group)</option>
                                </select>
                                <label for="b-travelers" class="sidebar-label">Number of Guests</label>
                            </div>"""

new_guests_html = """                            <div class="sidebar-form-group guest-counter-group" style="margin-top: 1.5rem; position: relative;">
                                <label class="sidebar-label" style="top: -0.8rem; font-size: 0.7rem; background: #FFFEFB; padding: 0 0.4rem; color: #6B5F54; font-weight: 700; letter-spacing: 1px;">Number of Guests</label>
                                <div class="guest-counter" style="display: flex; align-items: center; border: 1px solid rgba(24,19,14,0.1); border-radius: 8px; overflow: hidden; background: #FFFEFB;">
                                    <button type="button" class="btn-guest-minus" style="background: rgba(166,124,49,0.05); border: none; color: #A67C31; width: 45px; height: 48px; font-size: 1.4rem; font-weight: 300; cursor: pointer; transition: background 0.2s;">-</button>
                                    <input type="number" id="b-travelers" value="2" min="1" max="16" class="sidebar-input guest-input" readonly style="border: none !important; text-align: center; flex-grow: 1; padding: 0 !important; font-size: 1.1rem !important; font-weight: 600; color: #18130E; -moz-appearance: textfield; pointer-events: none;">
                                    <button type="button" class="btn-guest-plus" style="background: rgba(166,124,49,0.05); border: none; color: #A67C31; width: 45px; height: 48px; font-size: 1.4rem; font-weight: 300; cursor: pointer; transition: background 0.2s;">+</button>
                                </div>
                            </div>"""

html = html.replace(old_date_html, new_date_html)
html = html.replace(old_guests_html, new_guests_html)

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update JS
with open('5-days-golden-triangle-tour.js', 'r', encoding='utf-8') as f:
    js = f.read()

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

    // Sidebar Booking Form Handler
"""

js = js.replace('    // Sidebar Booking Form Handler\n', guest_js)

with open('5-days-golden-triangle-tour.js', 'w', encoding='utf-8') as f:
    f.write(js)
