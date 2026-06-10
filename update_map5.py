import re

with open('5-days-golden-triangle-tour.html', 'r', encoding='utf-8') as f:
    html = f.read()

key_info_strip = """
                    <!-- Key Info Strip -->
                    <div class="detail-block glass-card" style="padding: 1.4rem 2rem;">
                        <div style="display:grid; grid-template-columns: repeat(auto-fit,minmax(160px,1fr)); gap: 1.2rem;">
                            <div style="text-align:center; padding: 0.8rem; background:var(--gold-bg); border:1px solid var(--gold-border); border-radius:var(--r2);">
                                <div style="font-size:1.6rem; margin-bottom:0.3rem;">🏨</div>
                                <div style="font-family:var(--f-body); font-size:0.7rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--ink-soft);">Pick-Up &amp; Stay</div>
                                <div style="font-family:var(--f-body); font-size:0.88rem; font-weight:600; color:var(--ink); margin-top:0.3rem;">Hotel Grand Godwin</div>
                            </div>
                            <div style="text-align:center; padding: 0.8rem; background:var(--gold-bg); border:1px solid var(--gold-border); border-radius:var(--r2);">
                                <div style="font-size:1.6rem; margin-bottom:0.3rem;">🍳</div>
                                <div style="font-family:var(--f-body); font-size:0.7rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--ink-soft);">Breakfast Location</div>
                                <div style="font-family:var(--f-body); font-size:0.88rem; font-weight:600; color:var(--ink); margin-top:0.3rem;">Indian Grill Restaurant</div>
                            </div>
                            <div style="text-align:center; padding: 0.8rem; background:var(--gold-bg); border:1px solid var(--gold-border); border-radius:var(--r2);">
                                <div style="font-size:1.6rem; margin-bottom:0.3rem;">🚗</div>
                                <div style="font-family:var(--f-body); font-size:0.7rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--ink-soft);">Private Transfer</div>
                                <div style="font-family:var(--f-body); font-size:0.88rem; font-weight:600; color:var(--ink); margin-top:0.3rem;">Pickup &amp; Drop-off</div>
                            </div>
                            <div style="text-align:center; padding: 0.8rem; background:var(--gold-bg); border:1px solid var(--gold-border); border-radius:var(--r2);">
                                <div style="font-size:1.6rem; margin-bottom:0.3rem;">🎟️</div>
                                <div style="font-family:var(--f-body); font-size:0.7rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--ink-soft);">Monument Tickets</div>
                                <div style="font-family:var(--f-body); font-size:0.88rem; font-weight:600; color:#ef4444; margin-top:0.3rem;">Not Included</div>
                            </div>
                        </div>
                    </div>
"""

target = """                    <!-- Day by Day Itinerary -->"""

html = html.replace(target, key_info_strip + '\n' + target)

with open('5-days-golden-triangle-tour.html', 'w', encoding='utf-8') as f:
    f.write(html)
