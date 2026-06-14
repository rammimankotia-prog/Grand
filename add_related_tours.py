import os
from bs4 import BeautifulSoup

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
html_file = os.path.join(repo_path, '8-days-golden-triangle-tour.html')
css_file = os.path.join(repo_path, '8-days-golden-triangle-tour.css')

html_carousel = """
<!-- Related Tours Carousel -->
<section class="related-tours-section">
    <div class="container">
        <h2 class="section-title" style="text-align:center; margin-bottom: 2rem;">You might also like...</h2>
        <div class="related-carousel">
            <!-- Card 1 -->
            <a href="4-days-golden-triangle-tour.html" class="related-card">
                <img src="assets/golden_triangle_hero.png" alt="4 Days Golden Triangle" class="related-img">
                <div class="related-info">
                    <h4>4 Days Golden Triangle Tour</h4>
                    <p>Experience the vibrant contrasts of Old and New Delhi, and witness the Taj Mahal at sunrise.</p>
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

css_carousel = """
/* Related Tours Carousel */
.related-tours-section {
    padding: 4rem 0;
    background: #fdfaf6;
    border-top: 1px solid rgba(0,0,0,0.05);
}
.related-carousel {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 1.5rem;
    padding-bottom: 2rem;
    scrollbar-width: thin;
    scrollbar-color: var(--primary) #eee;
}
.related-carousel::-webkit-scrollbar {
    height: 8px;
}
.related-carousel::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}
.related-carousel::-webkit-scrollbar-thumb {
    background: var(--primary);
    border-radius: 4px;
}
.related-card {
    flex: 0 0 calc(25% - 1.125rem);
    min-width: 260px;
    scroll-snap-align: start;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    background: #fff;
    text-decoration: none;
    color: inherit;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}
.related-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.1);
}
.related-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.related-info {
    padding: 1.5rem;
}
.related-info h4 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.15rem;
    color: var(--secondary-dark);
}
.related-info p {
    font-size: 0.9rem;
    opacity: 0.75;
    margin: 0;
    line-height: 1.5;
}

@media (max-width: 992px) {
    .related-card {
        flex: 0 0 calc(33.333% - 1rem);
    }
}
@media (max-width: 768px) {
    .related-card {
        flex: 0 0 calc(50% - 0.75rem);
    }
}
@media (max-width: 480px) {
    .related-card {
        flex: 0 0 85%;
    }
}
"""

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(css_carousel)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before <!-- Footer -->
content = content.replace('<!-- Footer -->', html_carousel + '\n<!-- Footer -->')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected carousel into 8-days HTML and CSS")
