import os
import glob
import re

html_files = glob.glob("*.html")
js_files = glob.glob("*.js")

simple_guest_input = """                            <div class="sidebar-form-group">
                                <input type="number" id="b-travelers" value="2" min="1" max="16" required class="sidebar-input" style="padding-top: 1rem;">
                                <label for="b-travelers" class="sidebar-label" style="top: -0.4rem; font-size: 0.7rem; background: #FFFEFB; padding: 0 0.4rem; color: #6B5F54; font-weight: 700; letter-spacing: 1px;">Number of Guests</label>
                            </div>"""

for f in html_files:
    if f == 'index.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove Hotel Field
    hotel_regex = re.compile(r'<div class="sidebar-form-group">\s*<input[^>]+id="b-hotel"[^>]*>.*?</div>', re.DOTALL)
    content = hotel_regex.sub('', content)
    
    # 2. Replace Guest Counter with Native Input
    guest_regex = re.compile(r'<div class="sidebar-form-group guest-counter-group"[^>]*>.*?<div class="guest-counter"[^>]*>.*?<button[^>]+btn-guest-minus[^>]*>.*?</button>.*?<input[^>]+id="b-travelers"[^>]*>.*?<button[^>]+btn-guest-plus[^>]*>.*?</button>\s*</div>\s*</div>', re.DOTALL)
    content = guest_regex.sub(simple_guest_input, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

for f in js_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # 1. Remove JS Guest Counter Logic
    js_guest_logic = re.compile(r'// Guest Counter Logic.*?}\s*}\s*(?=// Sidebar Booking Form Handler|const\s+bookingForm)', re.DOTALL)
    content = js_guest_logic.sub('', content)
    
    # Also another version if it didn't match the exact trailing context
    js_guest_logic2 = re.compile(r'// Guest Counter Logic\s*const guestMinus.*?(?=\s*const bookingForm)', re.DOTALL)
    content = js_guest_logic2.sub('', content)

    # 2. Remove b-hotel variable definition
    content = re.sub(r'const\s+hotel\s*=\s*document\.getElementById\(\'b-hotel\'\)\.value.*?\n', '', content)
    content = re.sub(r'hotel:\s*document\.getElementById\(\'b-hotel\'\)\.value.*?\n', '', content)
    
    # 3. Remove payload insertions
    content = re.sub(r'Pickup_Hotel:\s*hotel,\s*\n', '', content)
    content = re.sub(r'\\nHotel:\s*\$\{hotel\}', '', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
