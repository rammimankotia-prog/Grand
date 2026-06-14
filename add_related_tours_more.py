import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_carousel = """
<!-- Related Tours Carousel -->
<section class="related-tours-section">
    <div class="container">
        <h2 class="section-title" style="text-align:center; margin-bottom: 2rem;">You might also like...</h2>
        <div class="related-carousel">
            <!-- Card 1 -->
            <a href="8-days-golden-triangle-tour.html" class="related-card">
                <img src="assets/golden_triangle_hero.png" alt="8 Days Golden Triangle" class="related-img">
                <div class="related-info">
                    <h4>8 Days Golden Triangle Tour</h4>
                    <p>Experience the ultimate relaxed pace covering Delhi, Agra, and Jaipur over 8 immersive days.</p>
                </div>
            </a>
            <!-- Card 2 -->
            <a href="5-days-golden-triangle-tour.html" class="related-card">
                <img src="assets/taj_mahal.png" alt="5 Days Golden Triangle" class="related-img">
                <div class="related-info">
                    <h4>5 Days Golden Triangle Tour</h4>
                    <p>A classic journey through the three most amazing cities displaying the evidence of the Mughal era.</p>
                </div>
            </a>
            <!-- Card 3 -->
            <a href="tiger-tour-jaipur.html" class="related-card">
                <img src="assets/tiger_tour.png" alt="Tiger Tour" class="related-img">
                <div class="related-info">
                    <h4>Taj Mahal & Wildlife Tiger Tour</h4>
                    <p>Combine the architectural brilliance of the Taj Mahal with an exhilarating Tiger Safari in Ranthambore.</p>
                </div>
            </a>
            <!-- Card 4 -->
            <a href="delhi-sightseeing.html" class="related-card">
                <img src="assets/delhi_sightseeing.png" alt="Delhi Sightseeing" class="related-img">
                <div class="related-info">
                    <h4>Delhi Sightseeing Tour</h4>
                    <p>Explore the heritage of India's capital city, from the Red Fort to the Lotus Temple.</p>
                </div>
            </a>
        </div>
    </div>
</section>
"""

html_4days = os.path.join(repo_path, '4-days-golden-triangle-tour.html')
with open(html_4days, 'r', encoding='utf-8') as f:
    content = f.read()
if '<!-- Related Tours Carousel -->' not in content:
    content = content.replace('<!-- Footer -->', html_carousel + '\n<!-- Footer -->')
    with open(html_4days, 'w', encoding='utf-8') as f:
        f.write(content)

html_carousel_5days = html_carousel.replace('<!-- Card 2 -->', '<!-- Card 2 -->\n            <a href="4-days-golden-triangle-tour.html" class="related-card">\n                <img src="assets/golden_triangle_hero.png" alt="4 Days Golden Triangle" class="related-img">\n                <div class="related-info">\n                    <h4>4 Days Golden Triangle Tour</h4>\n                    <p>Experience the vibrant contrasts of Old and New Delhi, and witness the Taj Mahal at sunrise.</p>\n                </div>\n            </a>\n            <!-- replaced -->').replace('5 Days Golden Triangle Tour', 'replaced').replace('<a href="5-days-golden-triangle-tour.html" class="related-card">', '').replace('<img src="assets/taj_mahal.png" alt="5 Days Golden Triangle" class="related-img">', '').replace('<div class="related-info">', '').replace('<h4>replaced</h4>', '').replace('<p>A classic journey through the three most amazing cities displaying the evidence of the Mughal era.</p>', '').replace('</div>', '', 1).replace('</a>', '', 1)

html_carousel_5days = """
<!-- Related Tours Carousel -->
<section class="related-tours-section">
    <div class="container">
        <h2 class="section-title" style="text-align:center; margin-bottom: 2rem;">You might also like...</h2>
        <div class="related-carousel">
            <!-- Card 1 -->
            <a href="8-days-golden-triangle-tour.html" class="related-card">
                <img src="assets/golden_triangle_hero.png" alt="8 Days Golden Triangle" class="related-img">
                <div class="related-info">
                    <h4>8 Days Golden Triangle Tour</h4>
                    <p>Experience the ultimate relaxed pace covering Delhi, Agra, and Jaipur over 8 immersive days.</p>
                </div>
            </a>
            <!-- Card 2 -->
            <a href="4-days-golden-triangle-tour.html" class="related-card">
                <img src="assets/hawa_mahal_hero.png" alt="4 Days Golden Triangle" class="related-img">
                <div class="related-info">
                    <h4>4 Days Golden Triangle Tour</h4>
                    <p>Experience the vibrant contrasts of Old and New Delhi, and witness the Taj Mahal at sunrise.</p>
                </div>
            </a>
            <!-- Card 3 -->
            <a href="tiger-tour-jaipur.html" class="related-card">
                <img src="assets/tiger_tour.png" alt="Tiger Tour" class="related-img">
                <div class="related-info">
                    <h4>Taj Mahal & Wildlife Tiger Tour</h4>
                    <p>Combine the architectural brilliance of the Taj Mahal with an exhilarating Tiger Safari in Ranthambore.</p>
                </div>
            </a>
            <!-- Card 4 -->
            <a href="delhi-sightseeing.html" class="related-card">
                <img src="assets/delhi_sightseeing.png" alt="Delhi Sightseeing" class="related-img">
                <div class="related-info">
                    <h4>Delhi Sightseeing Tour</h4>
                    <p>Explore the heritage of India's capital city, from the Red Fort to the Lotus Temple.</p>
                </div>
            </a>
        </div>
    </div>
</section>
"""

html_5days = os.path.join(repo_path, '5-days-golden-triangle-tour.html')
with open(html_5days, 'r', encoding='utf-8') as f:
    content = f.read()
if '<!-- Related Tours Carousel -->' not in content:
    content = content.replace('<!-- Footer -->', html_carousel_5days + '\n<!-- Footer -->')
    with open(html_5days, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected carousel into 4-days and 5-days HTML")
