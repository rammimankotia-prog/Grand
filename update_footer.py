import glob
import re

html_files = glob.glob("*.html")

old_footer_text = "<p>© 2026 Grand Holidays Luxury Tour Company. All rights reserved.</p>"
new_footer_text = """<p>© 2026 Grand Holidays Luxury Tour Company. All rights reserved.<br>
                    <span style="opacity: 0.8; font-size: 0.9em;">Unit of <a href="https://godwinhotels.com/" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: underline; text-underline-offset: 3px;">Godwin Hotels Delhi</a></span></p>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_footer_text in content:
        content = content.replace(old_footer_text, new_footer_text)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No match found in {file_path}")
