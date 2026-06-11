for file in ['tiger-tour-jaipur.html', 'himachal-exotic-tour.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # If the layout is broken, "tour-right-col" comes immediately after the FAQ or Inclusions section without closing the main-tour-content div.
    # Actually, in the broken state:
    # </ul>
    # </div>
    # </div>
    # <!-- Right: Booking Form & Sticky Sidebar -->
    # <div class="tour-right-col">
    
    # We just need to replace '<!-- Right: Booking Form & Sticky Sidebar -->'
    # with '</div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->'
    # But ONLY if it's currently broken (i.e. not already preceded by </div>\n\n)
    
    if '</div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->' not in html:
        html = html.replace('<!-- Right: Booking Form & Sticky Sidebar -->', '</div>\n\n                <!-- Right: Booking Form & Sticky Sidebar -->')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
