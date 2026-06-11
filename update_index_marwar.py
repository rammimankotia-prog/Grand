import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add to dropdown
dropdown_link = '                          <a href="marvellous-marwar-tour.html" class="dropdown-item">Marvellous Marwar Tour</a>\n'
html = re.sub(r'(<a href="rajasthan-heritage-tour.html" class="dropdown-item">Rajasthan Heritage Tour</a>)', r'\1\n' + dropdown_link, html)

# 2. Add card after Rajasthan Heritage Tour
new_card = """
                <!-- Card X: Marvellous Marwar Tour -->
                <div class="journey-card reveal reveal-delay-4">
                    <div class="card-img-container">
                        <img src="assets/rajasthan.png" alt="Marvellous Marwar Tour" class="journey-img">
                        <div class="card-badge">Heritage Journey</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">5 Days</span>
                            <span class="divider">|</span>
                            <span class="location">Jodhpur · Bikaner · Jaisalmer</span>
                        </div>
                        <h3 class="card-title">Marvellous Marwar Tour</h3>
                        <p class="card-text">Experience the Marvellous Marwar Tour traversing through the Blue City, royal dunes of Bikaner, and the Golden Sands of Jaisalmer.</p>
                        <ul class="card-highlights">
                            <li>Premium A/C Transport</li>
                            <li>Daily Breakfast</li>
                            <li>Tent Stay at Sam Dunes</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">On Request</span>
                            <a href="marvellous-marwar-tour.html" class="btn btn-outline btn-sm">View Tour</a>
                        </div>
                    </div>
                </div>
"""

rajasthan_card_end = r'(<h3 class="card-title">Rajasthan Heritage Tour</h3>.*?<a href="rajasthan-heritage-tour.html" class="btn btn-outline btn-sm">View.*?\n.*?</div>\s*</div>\s*</div>)'
html = re.sub(rajasthan_card_end, r'\1' + '\n' + new_card, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
