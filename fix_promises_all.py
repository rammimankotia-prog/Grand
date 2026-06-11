import os
import re

def fix_js_promises_all():
    for filename in os.listdir('.'):
        if not filename.endswith('.js'):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "fetch(" in content and ".then(() => {" in content:
            pattern = re.compile(r'\.then\(\(\) => \{(.*?)\}\)', re.DOTALL)
            
            def replace_promise(match):
                inner_code = match.group(1)
                return f""".then(response => response.json())
        .then(data => {{
            if (data.success || data.success === "true") {{
{inner_code}
            }} else {{
                alert("Server Message: " + (data.message || "Email service requires activation. Please check mail@godwinhotels.com for an activation link."));
                const submitBtn = document.querySelector('button[type="submit"]') || document.querySelector('.btn-sidebar-submit');
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
    fix_js_promises_all()
