import os
import re

def fix_single_quotes():
    url_search = "'submit-booking.php'"
    url_replace = "'https://formsubmit.co/ajax/mail@godwinhotels.com'"
    
    for filename in os.listdir('.'):
        if not filename.endswith('.js'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if url_search in content:
            content = content.replace(url_search, url_replace)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed single quotes in {filename}")

if __name__ == '__main__':
    fix_single_quotes()
