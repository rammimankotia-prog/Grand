import re

tour_files = [
    '5-days-golden-triangle-tour.html',
    'agra-day-tour.html',
    'delhi-agra-2-day-tour.html',
    'delhi-bicycle-tour.html',
    'delhi-food-tour.html',
    'delhi-sightseeing.html',
    'delhi-spiritual-tour.html',
    'delhi-tuk-tuk-tour.html',
    'golden-triangle.html',
    'himachal-exotic-tour.html',
    'himalayan-sanctuary.html',
    'imperial-rajasthan.html',
    'marvellous-marwar-tour.html',
    'rajasthan-desert-adventure.html',
    'rajasthan-heritage-tour.html',
    'tiger-tour-jaipur.html',
]

deposit_box = """
                        <div class="deposit-info-box">
                            <p><strong>Deposit Required:</strong> 25%</p>
                            <p><strong>Remaining Balance:</strong> Payable at the time of Arrival.</p>
                        </div>"""

deposit_css = """
        .deposit-info-box {
            background: #eef6fd;
            border: 1.5px solid #4a90c4;
            border-radius: 8px;
            padding: 0.9rem 1.2rem;
            margin-top: 0.8rem;
            margin-bottom: 0.5rem;
        }
        .deposit-info-box p {
            font-family: 'Outfit', sans-serif;
            font-size: 0.82rem;
            color: #1a3550;
            line-height: 1.6;
            margin: 0;
        }
        .deposit-info-box p + p { margin-top: 0.3rem; }
        .deposit-info-box strong { font-weight: 700; color: #1a3550; }"""

updated = []
skipped = []

for fname in tour_files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            html = f.read()

        if 'deposit-info-box' in html:
            skipped.append(fname)
            continue

        pattern = r'(class="price-summary-box[^"]*"[^>]*>.*?</div>)'
        match = re.search(pattern, html, re.DOTALL)

        if match:
            old_str = match.group(0)
            new_str = old_str + deposit_box
            html = html.replace(old_str, new_str, 1)

            if '<style>' in html:
                html = html.replace('<style>', '<style>' + deposit_css, 1)
            else:
                html = html.replace('</head>', '<style>' + deposit_css + '</style>\n</head>', 1)

            with open(fname, 'w', encoding='utf-8') as f:
                f.write(html)
            updated.append(fname)
        else:
            skipped.append(fname + ' (no price box)')

    except Exception as e:
        skipped.append(fname + ' ERROR: ' + str(e))

print("Updated:")
for f in updated:
    print("  " + f)

print("\nSkipped:")
for f in skipped:
    print("  " + f)
