import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
js_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.js')
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

# 1. Update JS
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Update price
js_content = js_content.replace('price: "Enquire for Price",', 'price: "₹22,050 per person",')

# Update Godwin Deluxe
js_content = js_content.replace(
    "You will be warmly greeted at the airport and chauffeured to your luxury hotel.",
    "You will be warmly greeted at the airport and chauffeured to Hotel Godwin Deluxe, your premium stay in the heart of the city."
)
js_content = js_content.replace(
    "Dive into the heart of India's capital.",
    "After a hearty breakfast at Hotel Godwin Deluxe, dive into the heart of India's capital."
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Update HTML SVG Map and Prices
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace hardcoded html price if any
html_content = html_content.replace('From ₹22,050 per person', 'From ₹22,050 per person') # Just in case

# Replace the Map SVG Path
old_path_block = """<!-- Route Line Paths Connecting Sights -->
  <path d="M340,148 L438,318 L190,318 Z" fill="rgba(166,124,49,0.07)" id="route-path" opacity="0.9" stroke="#a67c31" stroke-dasharray="12,8" stroke-linecap="round" stroke-width="3">
  <animate attributename="stroke-dashoffset" dur="5s" from="0" repeatcount="indefinite" to="-200"></animate>
  </path>
  <!-- Moving Taxi Sedan along route -->
  <g>
  <animatemotion dur="12s" repeatcount="indefinite" rotate="auto">
  <mpath href="#route-path"></mpath>
  </animatemotion>
  <g transform="translate(-10, -5)">"""

new_path_block = """<!-- Route Line Paths Connecting Sights -->
  <!-- Driving Route -->
  <path id="drive-route" d="M340,148 L438,318 L190,318" fill="none" opacity="0.9" stroke="#a67c31" stroke-dasharray="12,8" stroke-linecap="round" stroke-width="3">
  <animate attributename="stroke-dashoffset" dur="5s" from="0" repeatcount="indefinite" to="-200"></animate>
  </path>
  
  <!-- Flight Route -->
  <path id="flight-route" d="M190,318 Q385,250 580,260 Q460,204 340,148" fill="none" opacity="0.9" stroke="#0ea5e9" stroke-dasharray="8,8" stroke-linecap="round" stroke-width="2.5">
  <animate attributename="stroke-dashoffset" dur="8s" from="0" repeatcount="indefinite" to="-200"></animate>
  </path>
  
  <!-- Moving Plane -->
  <g>
  <animatemotion dur="8s" repeatcount="indefinite" rotate="auto">
  <mpath href="#flight-route"></mpath>
  </animatemotion>
  <g transform="translate(-12, -12) scale(0.6) rotate(90)">
  <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="#0ea5e9"></path>
  </g>
  </g>

  <!-- Moving Taxi Sedan along route -->
  <g>
  <animatemotion dur="8s" repeatcount="indefinite" rotate="auto">
  <mpath href="#drive-route"></mpath>
  </animatemotion>
  <g transform="translate(-10, -5)">"""

html_content = html_content.replace(old_path_block, new_path_block)

# We also need to add a Pin for Varanasi
old_pins = """  <!-- Pin: Jaipur -->
  <g class="map-pin-group" transform="translate(190, 318)">"""

new_pins = """  <!-- Pin: Varanasi -->
  <g class="map-pin-group" transform="translate(580, 260)">
  <circle cx="0" cy="0" fill="#fff" filter="url(#pinShadow)" r="8"></circle>
  <circle cx="0" cy="0" fill="#0ea5e9" r="4"></circle>
  <rect fill="#fff" filter="url(#labelShadow)" height="24" rx="12" width="90" x="-45" y="-38"></rect>
  <text fill="#1e293b" font-family="'Outfit', sans-serif" font-size="11" font-weight="600" text-anchor="middle" x="0" y="-22">Varanasi</text>
  </g>
  
  <!-- Pin: Jaipur -->
  <g class="map-pin-group" transform="translate(190, 318)">"""

html_content = html_content.replace(old_pins, new_pins)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated JS and HTML for Godwin Deluxe, Price, and Map.')
