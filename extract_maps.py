import os
import re

files = [
    "agra-day-tour.html",
    "delhi-bicycle-tour.html",
    "delhi-food-tour.html",
    "delhi-sightseeing.html",
    "delhi-tuk-tuk-tour.html",
    "golden-triangle.html",
    "himalayan-sanctuary.html",
    "imperial-rajasthan.html"
]

out = open("map_data.txt", "w", encoding="utf-8")

for f in files:
    if not os.path.exists(f): continue
    out.write(f"=== {f} ===\n")
    content = open(f, "r", encoding="utf-8").read()
    
    # Extract map SVG
    svg_match = re.search(r'<svg viewBox="0 0 680 480".*?</svg>', content, re.DOTALL)
    if svg_match:
        svg_content = svg_match.group(0)
        # We only care about the path and groups
        path = re.search(r'<path id="route-path"[^>]*>', svg_content)
        if path: out.write("PATH: " + path.group(0) + "\n")
        
        # Extract markers
        markers = re.findall(r'<g>.*?<text[^>]*>([^<]+)</text>.*?</g>', svg_content, re.DOTALL)
        for m in markers:
            # this regex is too simple, let's just find circles and texts in the SVG
            circles = re.findall(r'<circle cx="(\d+)" cy="(\d+)"', svg_content)
            texts = re.findall(r'<text x="(\d+)" y="\d+"[^>]*>([^<]+)</text>', svg_content)
            # Actually, let's just dump the <g> blocks that have markers
            pass
            
    # better approach: just extract all <circle> and <text> lines
    for line in content.split('\n'):
        if '<path id="route-path"' in line:
            out.write("ROUTE: " + line.strip() + "\n")
        if '<circle cx=' in line and 'r="10"' in line or 'r="11"' in line or 'r="15"' in line:
            out.write("MARKER: " + line.strip() + "\n")
        if '<text x=' in line and 'font-weight="800"' in line:
            out.write("LABEL: " + line.strip() + "\n")

    # Extract Itinerary
    itin_match = re.search(r'<div class="itinerary-timeline"[^>]*>(.*?)</div>\s*</div>\s*<!-- Inclusions', content, re.DOTALL)
    if itin_match:
        itin_html = itin_match.group(1)
        # extract days and times
        days = re.findall(r'<h3 class="step-title">(.*?)</h3>', itin_html)
        times = re.findall(r'<strong>(\d{2}:\d{2}\s*[APM]+):</strong>', itin_html)
        out.write(f"ITINERARY DAYS: {days}\n")
        out.write(f"ITINERARY TIMES: {times}\n")
        
    out.write("\n")

out.close()
print("Done")
