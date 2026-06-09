import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_card = '''
                <!-- Card 6: 2-Day Agra -->
                <div class="journey-card reveal reveal-delay-1">
                    <div class="card-img-container">
                        <img src="assets/agra_2day_hero.png" alt="2-Day Taj Mahal & Delhi Tour" class="journey-img">
                        <div class="card-badge">Bestseller</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">1 Night A 2 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Delhi A Agra</span>
                        </div>
                        <h3>2-Day Taj Mahal &amp; Delhi</h3>
                        <p>A bespoke luxury journey covering the Taj Mahal in Agra and the iconic heritage sites of Old &amp; New Delhi.</p>
                        <div class="card-footer" style="margin-top: 1.5rem;">
                            <span class="price" style="font-size: 1.1rem; color: var(--gold); font-weight: 600;">Price on Request</span>
                            <a href="delhi-agra-2-day-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
'''

# Find the end of the journey-grid
if '<!-- Card 5: Tuk Tuk Tour -->' in html:
    # Just find the end of card 5
    pass

html = html.replace('<!-- Grid End -->', new_card + '\n            </div>\n            <!-- Grid End -->')
# wait, there's no <!-- Grid End --> comment. I will just insert before </section> of signature journeys

# Let's do a reliable replace by finding the section end
html = re.sub(r'(</section>\s*<!-- Divider -->)', r'</div>\n' + new_card + r'\n\1', html)

# Actually let's use a more precise replacement.
# Let's check the bottom of the journeys grid
