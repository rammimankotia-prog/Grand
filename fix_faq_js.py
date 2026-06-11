import re

# 1. Add FAQ logic to tiger-tour-jaipur.js
with open('tiger-tour-jaipur.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

faq_js = """
    // FAQ Accordion
    document.querySelectorAll('.faq-question').forEach(btn => {
        btn.addEventListener('click', () => {
            const answer = btn.nextElementSibling;
            const isOpen = btn.classList.contains('open');
            // Close all others
            document.querySelectorAll('.faq-question.open').forEach(other => {
                if (other !== btn) {
                    other.classList.remove('open');
                    other.setAttribute('aria-expanded', 'false');
                    other.nextElementSibling.classList.remove('open');
                }
            });
            // Toggle current
            btn.classList.toggle('open', !isOpen);
            btn.setAttribute('aria-expanded', String(!isOpen));
            answer.classList.toggle('open', !isOpen);
        });
    });
});
"""

if '// FAQ Accordion' not in js_content:
    js_content = js_content.replace('});', faq_js, 1)
    with open('tiger-tour-jaipur.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

# 2. Add FAQ logic to himachal-exotic-tour.js
with open('himachal-exotic-tour.js', 'r', encoding='utf-8') as f:
    js_content2 = f.read()

if '// FAQ Accordion' not in js_content2:
    js_content2 = js_content2.replace('});', faq_js, 1)
    with open('himachal-exotic-tour.js', 'w', encoding='utf-8') as f:
        f.write(js_content2)

# 3. Fix the "Golden Triangle Tour" text in tiger-tour-jaipur.html
with open('tiger-tour-jaipur.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace(
    'Everything you need to know about the Golden Triangle Tour', 
    'Everything you need to know about the Tiger Tour With Jaipur'
)

with open('tiger-tour-jaipur.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 4. Fix the "Golden Triangle Tour" text in himachal-exotic-tour.html
with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html_content2 = f.read()

html_content2 = html_content2.replace(
    'Everything you need to know about the Golden Triangle Tour', 
    'Everything you need to know about the Himachal Exotic Tour'
)

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html_content2)
