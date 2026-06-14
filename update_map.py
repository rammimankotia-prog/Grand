import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-varanasi-tour.html')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

svg_content = """<svg class="gt-svg" viewbox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
      <filter id="drop-shadow">
          <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.15" />
      </filter>
      <filter id="glow">
          <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
          <feMerge>
              <feMergeNode in="coloredBlur"/>
              <feMergeNode in="SourceGraphic"/>
          </feMerge>
      </filter>
  </defs>

  <!-- Background Base -->
  <rect width="800" height="600" fill="#eae2d1" />
  
  <!-- Map Amorphous Blob (simulating landmass) -->
  <path d="M100,100 C200,20 600,50 720,150 C820,250 780,450 700,550 C550,650 200,600 80,450 C-20,300 0,180 100,100 Z" fill="#f4ecdc" opacity="0.8" />
  
  <!-- Faint Grid Lines -->
  <line x1="400" y1="0" x2="400" y2="600" stroke="#d5c8b3" stroke-width="1" stroke-dasharray="5,5" />
  <line x1="0" y1="300" x2="800" y2="300" stroke="#d5c8b3" stroke-width="1" stroke-dasharray="5,5" />

  <!-- Compass Top Right -->
  <g transform="translate(720, 80)">
      <circle cx="0" cy="0" r="30" fill="#fff" filter="url(#drop-shadow)" />
      <!-- Triangles -->
      <polygon points="-5,-10 0,-22 5,-10" fill="#a67c31" />
      <polygon points="-5,10 0,22 5,10" fill="#c4b59d" />
      <!-- Letters -->
      <text x="0" y="-25" font-family="'Outfit', sans-serif" font-size="12" font-weight="bold" fill="#a67c31" text-anchor="middle">N</text>
      <text x="0" y="32" font-family="'Outfit', sans-serif" font-size="10" font-weight="bold" fill="#888" text-anchor="middle">S</text>
      <text x="25" y="4" font-family="'Outfit', sans-serif" font-size="10" font-weight="bold" fill="#888" text-anchor="middle">E</text>
      <text x="-25" y="4" font-family="'Outfit', sans-serif" font-size="10" font-weight="bold" fill="#888" text-anchor="middle">W</text>
  </g>

  <!-- LINES -->
  <!-- Drive: Delhi to Agra -->
  <path d="M400,150 L550,350" fill="none" stroke="#a67c31" stroke-width="4" stroke-dasharray="12,12" />
  <!-- Drive: Agra to Jaipur -->
  <path d="M550,350 L250,350" fill="none" stroke="#a67c31" stroke-width="4" stroke-dasharray="12,12" />
  <!-- Flight: Jaipur to Varanasi -->
  <path id="flight1" d="M250,350 Q475,480 700,450" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="8,8" />
  <!-- Flight: Varanasi to Delhi -->
  <path id="flight2" d="M700,450 Q600,200 400,150" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="8,8" />

  <!-- DISTANCE PILLS -->
  <!-- Delhi to Agra -->
  <g transform="translate(475, 250)">
      <rect x="-60" y="-25" width="120" height="50" rx="25" fill="#2d2926" filter="url(#drop-shadow)" />
      <text x="0" y="-5" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" fill="#facc15" text-anchor="middle">240 km</text>
      <text x="0" y="12" font-family="'Outfit', sans-serif" font-size="11" fill="#ccc" text-anchor="middle">~4 hrs drive</text>
  </g>
  <!-- Agra to Jaipur -->
  <g transform="translate(400, 350)">
      <rect x="-60" y="-25" width="120" height="50" rx="25" fill="#2d2926" filter="url(#drop-shadow)" />
      <text x="0" y="-5" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" fill="#facc15" text-anchor="middle">240 km</text>
      <text x="0" y="12" font-family="'Outfit', sans-serif" font-size="11" fill="#ccc" text-anchor="middle">~4 hrs drive</text>
  </g>
  <!-- Jaipur to Varanasi Flight -->
  <g transform="translate(475, 410)">
      <rect x="-50" y="-20" width="100" height="40" rx="20" fill="#0284c7" filter="url(#drop-shadow)" />
      <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">✈️ Flight</text>
  </g>
  <!-- Varanasi to Delhi Flight -->
  <g transform="translate(580, 260)">
      <rect x="-50" y="-20" width="100" height="40" rx="20" fill="#0284c7" filter="url(#drop-shadow)" />
      <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">✈️ Flight</text>
  </g>

  <!-- NODES -->
  
  <!-- Jaipur (Day 4) -->
  <g transform="translate(250, 350)">
      <!-- Day Tag -->
      <g transform="translate(0, -45)">
          <rect x="-25" y="-12" width="50" height="24" rx="8" fill="#111" />
          <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">Day 4</text>
      </g>
      <!-- Circle -->
      <circle cx="0" cy="0" r="22" fill="#a67c31" stroke="#fff" stroke-width="4" filter="url(#drop-shadow)" />
      <text x="0" y="6" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">J</text>
      <!-- Pill -->
      <g transform="translate(0, 35)">
          <rect x="-50" y="-15" width="100" height="30" rx="15" fill="#fff" stroke="#a67c31" stroke-width="2" filter="url(#drop-shadow)" />
          <text x="0" y="5" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" letter-spacing="1" fill="#5c4212" text-anchor="middle">JAIPUR</text>
      </g>
  </g>

  <!-- Agra (Day 3) -->
  <g transform="translate(550, 350)">
      <!-- Day Tag -->
      <g transform="translate(0, -45)">
          <rect x="-25" y="-12" width="50" height="24" rx="8" fill="#111" />
          <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="11" font-weight="bold" fill="#facc15" text-anchor="middle">Day 3</text>
      </g>
      <!-- Circle -->
      <circle cx="0" cy="0" r="22" fill="#a67c31" stroke="#fff" stroke-width="4" filter="url(#drop-shadow)" />
      <text x="0" y="6" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">A</text>
      <!-- Pill -->
      <g transform="translate(0, 35)">
          <rect x="-45" y="-15" width="90" height="30" rx="15" fill="#fff" stroke="#a67c31" stroke-width="2" filter="url(#drop-shadow)" />
          <text x="0" y="5" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" letter-spacing="1" fill="#5c4212" text-anchor="middle">AGRA</text>
      </g>
  </g>

  <!-- Varanasi (Day 6) -->
  <g transform="translate(700, 450)">
      <!-- Day Tag -->
      <g transform="translate(0, -45)">
          <rect x="-25" y="-12" width="50" height="24" rx="8" fill="#111" />
          <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="11" font-weight="bold" fill="#0ea5e9" text-anchor="middle">Day 6</text>
      </g>
      <!-- Circle -->
      <circle cx="0" cy="0" r="22" fill="#0284c7" stroke="#fff" stroke-width="4" filter="url(#drop-shadow)" />
      <text x="0" y="6" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">V</text>
      <!-- Pill -->
      <g transform="translate(0, 35)">
          <rect x="-55" y="-15" width="110" height="30" rx="15" fill="#fff" stroke="#0284c7" stroke-width="2" filter="url(#drop-shadow)" />
          <text x="0" y="5" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" letter-spacing="1" fill="#0369a1" text-anchor="middle">VARANASI</text>
      </g>
  </g>

  <!-- Delhi (Starts & Ends) -->
  <g transform="translate(400, 150)">
      <!-- Starts & Ends Tag -->
      <g transform="translate(0, -50)">
          <rect x="-80" y="-15" width="160" height="30" rx="15" fill="#cfa55b" stroke="#fff" stroke-width="2" filter="url(#drop-shadow)" />
          <text x="0" y="4" font-family="'Outfit', sans-serif" font-size="11" font-weight="bold" fill="#fff" letter-spacing="1" text-anchor="middle">TOUR STARTS &amp; ENDS</text>
      </g>
      <!-- Circle -->
      <circle cx="0" cy="0" r="22" fill="#a67c31" stroke="#fff" stroke-width="4" filter="url(#drop-shadow)" />
      <text x="0" y="6" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fff" text-anchor="middle">D</text>
      <!-- Pill -->
      <g transform="translate(0, 35)">
          <rect x="-50" y="-15" width="100" height="30" rx="15" fill="#fff" stroke="#a67c31" stroke-width="2" filter="url(#drop-shadow)" />
          <text x="0" y="5" font-family="'Outfit', sans-serif" font-size="15" font-weight="bold" letter-spacing="1" fill="#5c4212" text-anchor="middle">DELHI</text>
      </g>
  </g>

  <!-- ANIMATIONS -->
  <!-- Car driving from Delhi to Agra to Jaipur -->
  <g>
      <animateMotion dur="8s" repeatCount="indefinite" rotate="auto">
          <mpath href="#drive-path-anim"/>
      </animateMotion>
      <g transform="translate(-15, -8)">
          <!-- Car Body -->
          <rect x="0" y="0" width="30" height="16" rx="4" fill="#f59e0b" stroke="#78350f" stroke-width="2" />
          <rect x="6" y="2" width="18" height="12" rx="2" fill="#e0f2fe" stroke="#0369a1" stroke-width="1" />
      </g>
  </g>
  <path id="drive-path-anim" d="M400,150 L550,350 L250,350" fill="none" opacity="0" />

  <!-- Plane flying Jaipur -> Varanasi -->
  <g>
      <animateMotion dur="6s" repeatCount="indefinite" rotate="auto">
          <mpath href="#flight1"/>
      </animateMotion>
      <g transform="translate(-15, -15) rotate(90)">
          <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="#0ea5e9" filter="url(#drop-shadow)"></path>
      </g>
  </g>

  <!-- Plane flying Varanasi -> Delhi -->
  <g>
      <animateMotion dur="6s" repeatCount="indefinite" rotate="auto" begin="3s">
          <mpath href="#flight2"/>
      </animateMotion>
      <g transform="translate(-15, -15) rotate(90)">
          <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="#0ea5e9" filter="url(#drop-shadow)"></path>
      </g>
  </g>

</svg>"""

# Find the start and end of the current <svg> map
start_tag = '<svg class="gt-svg"'
end_tag = '</svg>'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx) + len(end_tag)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + svg_content + content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced SVG map successfully.")
else:
    print("Could not find SVG block.")
