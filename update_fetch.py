import os

def update_files():
    search_str = '"https://formsubmit.co/ajax/mail@godwinhotels.com"'
    replace_str = '"submit-booking.php"'
    
    for filename in os.listdir('.'):
        if filename.endswith('.js'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if search_str in content:
                content = content.replace(search_str, replace_str)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")

if __name__ == '__main__':
    update_files()
