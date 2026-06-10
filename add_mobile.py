import re

# 1. Update HTML
with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_email_html = """                            <div class="sidebar-form-group">
                                <input type="email" id="b-email" required placeholder=" " class="sidebar-input">
                                <label for="b-email" class="sidebar-label">Email Address</label>
                            </div>"""

new_email_and_mobile_html = """                            <div class="sidebar-form-group">
                                <input type="email" id="b-email" required placeholder=" " class="sidebar-input">
                                <label for="b-email" class="sidebar-label">Email Address</label>
                            </div>

                            <div class="sidebar-form-group">
                                <input type="tel" id="b-mobile" required placeholder=" " class="sidebar-input">
                                <label for="b-mobile" class="sidebar-label">Mobile Number</label>
                            </div>"""

html = html.replace(old_email_html, new_email_and_mobile_html)

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update JS
with open('5-days-golden-triangle-tour.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_js = "email: document.getElementById('b-email').value,"
new_js = "email: document.getElementById('b-email').value,\n                mobile: document.getElementById('b-mobile').value,"

js = js.replace(old_js, new_js)

with open('5-days-golden-triangle-tour.js', 'w', encoding='utf-8') as f:
    f.write(js)
