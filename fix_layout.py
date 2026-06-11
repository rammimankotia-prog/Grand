with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the missing closing </div> for main-tour-content
html = html.replace('<!-- Right: Booking Form & Sticky Sidebar -->', '</div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->')

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
