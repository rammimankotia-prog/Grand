import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add to dropdown
dropdown_link = '                          <a href="rajasthan-heritage-tour.html" class="dropdown-item">Rajasthan Heritage Tour</a>\n'
html = html.replace('<a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan \nTour</a>', 
                    '<a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan Tour</a>\n' + dropdown_link)
# If it was split or not split, let's use a regex just to be safe
html = re.sub(r'(<a href="imperial-rajasthan.html" class="dropdown-item">Imperial Rajasthan.*?Tour</a>)', r'\1\n' + dropdown_link, html)

# 2. Add card after Imperial Rajasthan
new_card = """
                <!-- Card 3b: Rajasthan Heritage Tour -->
                <div class="journey-card reveal reveal-delay-3">
                    <div class="card-img-container">
                        <img src="assets/rajasthan.png" alt="Rajasthan Heritage Tour" class="journey-img">
                        <div class="card-badge">Heritage Journey</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">8 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Jaipur · Jodhpur · Jaisalmer · Udaipur</span>
                        </div>
                        <h3 class="card-title">Rajasthan Heritage Tour</h3>
                        <p class="card-text">Experience the royal heritage of Rajasthan covering the Pink City, Blue City, Golden City, and Lake City.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Daily Breakfast</li>
                            <li>Assistance on Arrival</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="rajasthan-heritage-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

imperial_card_end = r'(<h3 class="card-title">Imperial Rajasthan Retold</h3>.*?<a href="imperial-rajasthan.html" class="btn btn-outline btn-sm">View.*?\n.*?</div>\s*</div>\s*</div>)'
html = re.sub(imperial_card_end, r'\1' + '\n' + new_card, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
