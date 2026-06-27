"""
add_client_validation_v3.py
Adds client-side validation for Name, Email, Mobile and Preferred Date
to all tour booking form JS handlers by finding the `fetch(` call and inserting
a self-contained validation block before it.
"""

import os
import re

SITE_DIR = r"c:\xampp\htdocs\Grand"

SKIP = {'global-ux.js', 'generate-sitemap.js', 'setup-hooks.js', 'script.js',
        'index.js', 'car-booking.js', 'contact.js', 'update_headers_footers.py',
        'add_client_validation.py', 'add_client_validation_v2.py', 'add_client_validation_v3.py'}

VALIDATION_SNIPPET = """\
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
"""

def read_file(path):
    for enc in ('utf-8', 'utf-8-sig', 'latin-1', 'cp1252'):
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, ValueError):
            continue
    return None, None

def write_file(path, content, enc):
    with open(path, 'w', encoding=enc) as f:
        f.write(content)

def patch(content):
    if 'Required-field validation' in content:
        return content, 'already patched'

    # Ensure origText is defined if we change submitBtn text
    if "const submitBtn = bookingForm.querySelector" in content and "origText = " not in content:
        content = re.sub(
            r"(const submitBtn = bookingForm\.querySelector\(['\"]\.btn-sidebar-submit['\"]\);)",
            r"\1\n            var origText = submitBtn ? submitBtn.innerText : 'Submit';",
            content,
            count=1
        )

    # Find the submit event listener and the fetch call inside it
    # We want the first `fetch(` inside the submit event listener
    
    # We can just look for `fetch("submit-booking.php` or `fetch('submit-booking.php` or `fetch(submitUrl`
    match = re.search(r'([ \t]*)(?:return )?fetch\(\s*["\']?submit-booking\.php["\']?|fetch\(\s*submitUrl', content)
    
    if not match:
        return content, 'fetch submit-booking.php not found'
        
    insert_pos = match.start()
    indent = match.group(1)
    
    new_content = content[:insert_pos] + VALIDATION_SNIPPET + content[insert_pos:]
    return new_content, 'updated'

def main():
    js_files = sorted([
        f for f in os.listdir(SITE_DIR)
        if f.endswith('.js') and f not in SKIP
    ])
    print(f"\\nProcessing {len(js_files)} JS files...\\n")

    for fname in js_files:
        fpath = os.path.join(SITE_DIR, fname)
        content, enc = read_file(fpath)
        if content is None:
            print(f"  !! {fname}  [cannot read]")
            continue

        new_content, reason = patch(content)
        if new_content != content:
            write_file(fpath, new_content, enc)
            print(f"  OK {fname}  [{reason}]")
        else:
            print(f"  -- {fname}  [{reason}]")

    print("\\nDone.")

if __name__ == '__main__':
    main()
