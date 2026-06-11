import re

with open('himachal-exotic-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_faq = """<div class="faq-grid" id="faq-grid-gt">
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">What is the best time to take the Himachal Exotic Tour?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>The best time to visit depends on what you wish to experience. For pleasant, cool weather to escape the heat, visit between March and June. If you want to experience the magic of snowfall in Kufri and Manali, November to February is the ideal time.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Are adventure activities in Solang Valley included?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>The package includes private AC transportation to Solang Valley. However, the direct fees for specific adventure activities like paragliding, zorbing, or skiing are excluded and can be paid directly on-site based on your interests.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Is the drive safe in the mountainous terrain?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Absolutely. You will be traveling in a premium, fully-serviced AC car driven by highly experienced, professional drivers who are specifically trained and certified for the Himalayan mountain routes.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">What is excluded from this tour package?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>The package does not include air or train fare to/from Delhi, guide and monument entrance fees, camera/safari charges, or personal travel insurance. You will be responsible for your lunches, dinners, and any personal shopping.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Does the tour start and end in Delhi?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Yes, the tour begins with a pickup from the Delhi Airport or Railway Station and concludes with a drop-off at the same locations in Delhi. This makes it very convenient for international and domestic travelers flying into the capital.</p></div></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">
                        <span class="faq-q-text">Will the AC car be comfortable for the long mountain drives?</span>
                        <span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span>
                    </button>
                    <div class="faq-answer"><div class="faq-answer-inner"><p>Yes, we use premium AC vehicles like Swift Dzire, Toyota Innova, or similar SUVs depending on your group size. They are perfectly maintained and offer excellent legroom and comfort for the scenic but long drives between Delhi, Shimla, and Manali.</p></div></div>
                </div>
            </div>"""

html = re.sub(r'<div class="faq-grid" id="faq-grid-gt">.*?</section>', new_faq + '\n        </section>', html, flags=re.DOTALL)

with open('himachal-exotic-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
