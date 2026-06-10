import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Duplicate Train Booking card to make Car Booking card
car_card = """
                <!-- Card 10: Car Booking -->
                <div class="journey-card reveal reveal-delay-4">
                    <div class="card-img-container" style="background: #2a2a2a;">
                        <img src="assets/golden_triangle.png" alt="All India Car Booking" class="journey-img" style="opacity: 0.8;">
                        <div class="card-badge">Private Fleet</div>
                    </div>
                    <div class="card-content">
                        <div class="card-meta">
                            <span class="duration">Pan-India</span>
                            <span class="divider">|</span>
                            <span class="location">Any Destination</span>
                        </div>
                        <h3 class="card-title">Book Private Car</h3>
                        <p class="card-text">Explore India comfortably. Book private vehicles and chauffeurs for any route, anywhere in India. Safe, reliable, and premium service.</p>
                        <ul class="card-highlights">
                            <li>Sedans, SUVs & Luxury Vans</li>
                            <li>Professional Chauffeurs</li>
                            <li>Custom Multi-City Routing</li>
                        </ul>
                        <div class="card-footer">
                            <span class="price">All India <span class="pp">Network</span></span>
                            <a href="car-booking.html" class="btn btn-outline btn-sm">Book Car</a>
                        </div>
                    </div>
                </div>
"""

# Insert it after Card 9 (train booking)
train_card_end = r'<!-- Card 9: Train Booking -->.*?<a href="train-booking\.html".*?</div>\s*</div>\s*</div>'
html = re.sub(f'({train_card_end})', r'\1' + '\n' + car_card, html, flags=re.DOTALL)

# 2. Add link in Footer
footer_link = '<a href="train-booking.html">Book Train Tickets</a>\n                    <a href="car-booking.html">Book Private Car</a>'
html = html.replace('<a href="train-booking.html">Book Train Tickets</a>', footer_link)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
