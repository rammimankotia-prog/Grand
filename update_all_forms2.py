import os
import glob
import re

html_files = glob.glob("*.html")

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

for f in html_files:
    if f == 'index.html' or f == '5-days-golden-triangle-tour.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="b-date"' not in content:
        continue
        
    # Replace Date
    date_regex = re.compile(r'<div class="sidebar-form-group">\s*<input[^>]+id="b-date"[^>]*>.*?</div>', re.DOTALL)
    content = date_regex.sub(new_date_html, content)
    
    # Replace Travelers
    travelers_regex = re.compile(r'<div class="sidebar-form-group">\s*<(input|select)[^>]+id="b-travelers"[^>]*>.*?</div>', re.DOTALL)
    content = travelers_regex.sub(new_guests_html, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

