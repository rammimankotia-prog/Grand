import os
import re

def fix_js_promises():
    for filename in os.listdir('.'):
        if not filename.endswith('.js'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We want to replace:
        # .then(() => {
        #     bookingForm.style.display = 'none';
        #     bookingSuccess.style.display = 'flex'; // or similar
        # })
        # With a robust json parser
        
        if "fetch(" in content and "formsubmit" in content and ".then(() => {" in content:
            # We'll use regex to find the .then(() => { ... }) block
            pattern = re.compile(r'\.then\(\(\) => \{(.*?)\}\)', re.DOTALL)
            
            def replace_promise(match):
                inner_code = match.group(1)
                return f""".then(response => response.json())
        .then(data => {{
            if (data.success || data.success === "true") {{
{inner_code}
            }} else {{
                alert("Server Message: " + (data.message || "Email service requires activation. Please check mail@godwinhotels.com for an activation link."));
                const submitBtn = bookingForm.querySelector('button[type="submit"]') || bookingForm.querySelector('.btn-sidebar-submit');
                if (submitBtn) {{
                    submitBtn.innerText = 'Submit Reservation Request';
                    submitBtn.disabled = false;
                }}
            }}
        }})"""
            
            new_content = pattern.sub(replace_promise, content)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed promise in {filename}")

if __name__ == '__main__':
    fix_js_promises()
