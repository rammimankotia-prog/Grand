import os
import re

def fix_forms():
    url_search = '"submit-booking.php"'
    url_replace = '"https://formsubmit.co/ajax/mail@godwinhotels.com"'
    
    for filename in os.listdir('.'):
        if not filename.endswith('.js'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Revert the URL
        if url_search in content:
            content = content.replace(url_search, url_replace)
            
        # Inject _cc into the payload if not present
        # We look for "email: document.getElementById('b-email').value"
        # and add "_cc: document.getElementById('b-email').value" right after it.
        
        # Booking forms
        if "email: document.getElementById('b-email').value," in content and "_cc:" not in content:
            content = content.replace(
                "email: document.getElementById('b-email').value,",
                "email: document.getElementById('b-email').value,\n            _cc: document.getElementById('b-email').value,"
            )
            
        # Newsletter forms (in index.js for example)
        if "email: document.getElementById('nl-email').value," in content and "_cc:" not in content:
            content = content.replace(
                "email: document.getElementById('nl-email').value,",
                "email: document.getElementById('nl-email').value,\n                _cc: document.getElementById('nl-email').value,"
            )

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

if __name__ == '__main__':
    fix_forms()
