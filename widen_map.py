import re

with open('delhi-sightseeing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Scale distances
# <rect x="-38" y="-12" width="76" height="24" rx="12" fill="#1a1208" opacity="0.85"/>
# <text x="0" y="3" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="700" fill="#f0c060">~6 km / 20m</text>
html = html.replace('rect x="-38" y="-12" width="76" height="24" rx="12"', 'rect x="-48" y="-14" width="96" height="28" rx="14"')
html = re.sub(r'(fill="#f0c060">~.*? km / .*?m</text>)', lambda m: m.group(1).replace('y="3"', 'y="5"'), html)
html = html.replace('font-size="8.5" font-weight="700" fill="#f0c060">~', 'font-size="10" font-weight="700" fill="#f0c060">~')

# TOUR STARTS & ENDS
html = html.replace('rect x="180" y="30" width="140" height="20" rx="10"', 'rect x="160" y="28" width="180" height="24" rx="12"')
html = html.replace('font-size="8.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS & ENDS</text>', 'font-size="10.5" font-weight="800" fill="#fff" letter-spacing="1">TOUR STARTS & ENDS</text>')
html = html.replace('<text x="250" y="43"', '<text x="250" y="45"')

# Time Labels (e.g. 09:00 AM)
# <rect x="190" y="53" width="40" height="14" rx="4" fill="#1a1208"/>
# <text x="210" y="63" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7" font-weight="700" fill="#f0c060">09:00 AM</text>
def scale_time(m):
    x = int(m.group(1))
    y = int(m.group(2))
    w = int(m.group(3))
    tx = int(m.group(4))
    ty = int(m.group(5))
    return f'rect x="{x-10}" y="{y-2}" width="{w+20}" height="18" rx="6" fill="#1a1208"/>\n                            <text x="{tx}" y="{ty+1}" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5"'
html = re.sub(r'rect x="(\d+)" y="(\d+)" width="(\d+)" height="14" rx="4" fill="#1a1208"/>\s*<text x="(\d+)" y="(\d+)" text-anchor="middle" font-family="Outfit,sans-serif" font-size="7"', scale_time, html)

# Major Locations (GODWIN DELUXE, JAMA MASJID, INDIA GATE, HUMAYUN'S TOMB, QUTUB MINAR)
# e.g., <rect x="200" y="60" width="100" height="20" rx="10" fill="#fff" stroke="#2d3748" stroke-width="1.5" filter="url(#labelShadow)"/>
# <text x="250" y="73" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="#2d3748" letter-spacing="1">GODWIN DELUXE</text>
def scale_major(m):
    x = int(m.group(1))
    y = int(m.group(2))
    w = int(m.group(3))
    fill = m.group(4)
    stroke = m.group(5)
    tx = int(m.group(6))
    ty = int(m.group(7))
    tfill = m.group(8)
    text = m.group(9)
    
    new_w = w + 40
    new_x = x - 20
    new_h = 26
    new_y = y - 3
    new_ty = ty + 2
    return f'rect x="{new_x}" y="{new_y}" width="{new_w}" height="{new_h}" rx="13" fill="{fill}" stroke="{stroke}" stroke-width="1.5" filter="url(#labelShadow)"/>\n                            <text x="{tx}" y="{new_ty}" text-anchor="middle" font-family="Outfit,sans-serif" font-size="10.5" font-weight="800" fill="{tfill}" letter-spacing="1">{text}</text>'

html = re.sub(r'rect x="(\d+)" y="(\d+)" width="(\d+)" height="20" rx="10" fill="([^"]+)" stroke="([^"]+)" stroke-width="1.5" filter="url\(#labelShadow\)"/>\s*<text x="(\d+)" y="(\d+)" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8.5" font-weight="800" fill="([^"]+)" letter-spacing="1">([^<]+)</text>', scale_major, html)

# Minor Locations (RED FORT, RAJ GHAT, LOTUS TEMPLE)
# e.g., <rect x="375" y="93" width="70" height="18" rx="9" fill="#fff" stroke="#a67c31" stroke-width="1" filter="url(#labelShadow)"/>
# <text x="410" y="105" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" font-weight="700" fill="#6b4c12">RED FORT</text>
def scale_minor(m):
    x = int(m.group(1))
    y = int(m.group(2))
    w = int(m.group(3))
    tx = int(m.group(4))
    ty = int(m.group(5))
    text = m.group(6)
    
    new_w = w + 30
    new_x = x - 15
    new_h = 24
    new_y = y - 3
    new_ty = ty + 2
    return f'rect x="{new_x}" y="{new_y}" width="{new_w}" height="{new_h}" rx="12" fill="#fff" stroke="#a67c31" stroke-width="1" filter="url(#labelShadow)"/>\n                            <text x="{tx}" y="{new_ty}" text-anchor="middle" font-family="Outfit,sans-serif" font-size="9.5" font-weight="700" fill="#6b4c12">{text}</text>'

html = re.sub(r'rect x="(\d+)" y="(\d+)" width="(\d+)" height="18" rx="9" fill="#fff" stroke="#a67c31" stroke-width="1" filter="url\(#labelShadow\)"/>\s*<text x="(\d+)" y="(\d+)" text-anchor="middle" font-family="Outfit,sans-serif" font-size="8" font-weight="700" fill="#6b4c12">([^<]+)</text>', scale_minor, html)


with open('delhi-sightseeing.html', 'w', encoding='utf-8') as f:
    f.write(html)
