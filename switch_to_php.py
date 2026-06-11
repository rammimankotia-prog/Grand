import os
import re

def switch_to_php():
    url_search = '"https://formsubmit.co/ajax/mail@godwinhotels.com"'
    url_replace = '"submit-booking.php"'
    
    url_search_single = "'https://formsubmit.co/ajax/mail@godwinhotels.com'"
    url_replace_single = "'submit-booking.php'"
    
    for filename in os.listdir('.'):
        if not filename.endswith('.js'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        if url_search in new_content:
            new_content = new_content.replace(url_search, url_replace)
            
        if url_search_single in new_content:
            new_content = new_content.replace(url_search_single, url_replace_single)
            
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Switched to PHP in {filename}")

if __name__ == '__main__':
    switch_to_php()
