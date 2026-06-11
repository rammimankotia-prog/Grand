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

for file in ['tiger-tour-jaipur.js', 'himachal-exotic-tour.js']:
    with open(file, 'r', encoding='utf-8') as f:
        js = f.read()
    
    if '// FAQ Accordion' not in js:
        # Replace the very last '});' with the faq_js
        parts = js.rsplit('});', 1)
        js = parts[0] + faq_js
        with open(file, 'w', encoding='utf-8') as f:
            f.write(js)

with open('tiger-tour-jaipur.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace(
    'Everything you need to know about the Golden Triangle Tour', 
    'Everything you need to know about the Tiger Tour With Jaipur'
)

with open('tiger-tour-jaipur.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html_content2 = f.read()

html_content2 = html_content2.replace(
    'Everything you need to know about the Golden Triangle Tour', 
    'Everything you need to know about the Himachal Exotic Tour'
)

# And remove the Manali card from tiger tour again since I re-ran the build script!
import re
manali_pattern = r'<div class="gt-city-card">\s*<div class="city-card-num">03</div>\s*<div class="city-card-icon">&#9978;</div>\s*<h3 class="city-card-name">Manali</h3>\s*<p class="city-card-desc">.*?</p>\s*<div class="city-card-tags">.*?</div>\s*</div>'
html_content = re.sub(manali_pattern, '', html_content, flags=re.DOTALL)

with open('tiger-tour-jaipur.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html_content2)
