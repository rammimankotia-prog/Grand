import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

# Beautiful mega menu HTML
new_dropdown_content = """<div class="dropdown-menu mega-menu">
                            <div class="mega-menu-inner">
                                <div class="mega-col">
                                    <div class="mega-col-header">
                                        <span class="mega-col-icon">◆</span>
                                        Golden Triangle
                                    </div>
                                    <a class="dropdown-item" href="4-days-golden-triangle-tour.html">
                                        <span class="item-icon">🏛️</span>
                                        <span class="item-text">
                                            <span class="item-name">4 Days Golden Triangle</span>
                                            <span class="item-sub">Delhi · Agra · Jaipur</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="5-days-golden-triangle-tour.html">
                                        <span class="item-icon">🕌</span>
                                        <span class="item-text">
                                            <span class="item-name">5 Days Golden Triangle</span>
                                            <span class="item-sub">Delhi · Agra · Jaipur</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="8-days-golden-triangle-tour.html">
                                        <span class="item-icon">⭐</span>
                                        <span class="item-text">
                                            <span class="item-name">8 Days Golden Triangle</span>
                                            <span class="item-sub">Delhi · Agra · Jaipur</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="8-days-golden-triangle-varanasi-tour.html">
                                        <span class="item-icon">🛕</span>
                                        <span class="item-text">
                                            <span class="item-name">8 Days with Varanasi</span>
                                            <span class="item-sub">Golden Triangle + Varanasi</span>
                                        </span>
                                    </a>
                                </div>
                                <div class="mega-col-divider"></div>
                                <div class="mega-col">
                                    <div class="mega-col-header">
                                        <span class="mega-col-icon">◆</span>
                                        Delhi &amp; Agra
                                    </div>
                                    <a class="dropdown-item" href="delhi-sightseeing.html">
                                        <span class="item-icon">🏯</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Sightseeing</span>
                                            <span class="item-sub">Red Fort · Qutub · India Gate</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-food-tour.html">
                                        <span class="item-icon">🍛</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Food &amp; Spice Tour</span>
                                            <span class="item-sub">Chandni Chowk · Street Food</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-spiritual-tour.html">
                                        <span class="item-icon">🙏</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Spiritual Tour</span>
                                            <span class="item-sub">Temples · Gurudwaras · Shrines</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-bicycle-tour.html">
                                        <span class="item-icon">🚴</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Bicycle Tour</span>
                                            <span class="item-sub">Old Delhi · Heritage Lanes</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-tuk-tuk-tour.html">
                                        <span class="item-icon">🛺</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Tuk Tuk Tour</span>
                                            <span class="item-sub">Iconic Delhi Experience</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-museum-tour.html">
                                        <span class="item-icon">🎨</span>
                                        <span class="item-text">
                                            <span class="item-name">Delhi Museum Tour</span>
                                            <span class="item-sub">National Museum · Crafts</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="agra-day-tour.html">
                                        <span class="item-icon">🕍</span>
                                        <span class="item-text">
                                            <span class="item-name">Same Day Agra Tour</span>
                                            <span class="item-sub">Taj Mahal · Agra Fort</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="delhi-agra-2-day-tour.html">
                                        <span class="item-icon">🌅</span>
                                        <span class="item-text">
                                            <span class="item-name">2-Day Taj Mahal &amp; Delhi</span>
                                            <span class="item-sub">Overnight · Sunrise Taj Mahal</span>
                                        </span>
                                    </a>
                                </div>
                                <div class="mega-col-divider"></div>
                                <div class="mega-col">
                                    <div class="mega-col-header">
                                        <span class="mega-col-icon">◆</span>
                                        Rajasthan
                                    </div>
                                    <a class="dropdown-item" href="imperial-rajasthan.html">
                                        <span class="item-icon">👑</span>
                                        <span class="item-text">
                                            <span class="item-name">Imperial Rajasthan</span>
                                            <span class="item-sub">Jaipur · Jodhpur · Udaipur</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="rajasthan-heritage-tour.html">
                                        <span class="item-icon">🏰</span>
                                        <span class="item-text">
                                            <span class="item-name">Rajasthan Heritage Tour</span>
                                            <span class="item-sub">Forts · Palaces · Stepwells</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="marvellous-marwar-tour.html">
                                        <span class="item-icon">🌄</span>
                                        <span class="item-text">
                                            <span class="item-name">Marvellous Marwar Tour</span>
                                            <span class="item-sub">Jodhpur · Jaisalmer · Bikaner</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="rajasthan-desert-adventure.html">
                                        <span class="item-icon">🐪</span>
                                        <span class="item-text">
                                            <span class="item-name">Desert Adventure</span>
                                            <span class="item-sub">Camel Safari · Desert Camps</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="tiger-tour-jaipur.html">
                                        <span class="item-icon">🐯</span>
                                        <span class="item-text">
                                            <span class="item-name">Tiger Tour With Jaipur</span>
                                            <span class="item-sub">Ranthambore Safari · Jaipur</span>
                                        </span>
                                    </a>
                                    <div class="mega-col-header" style="margin-top:1rem;">
                                        <span class="mega-col-icon">◆</span>
                                        Himalayas
                                    </div>
                                    <a class="dropdown-item" href="himachal-exotic-tour.html">
                                        <span class="item-icon">🏔️</span>
                                        <span class="item-text">
                                            <span class="item-name">Himachal Exotic Tour</span>
                                            <span class="item-sub">Shimla · Manali · Spiti</span>
                                        </span>
                                    </a>
                                    <a class="dropdown-item" href="himalayan-sanctuary.html">
                                        <span class="item-icon">🌿</span>
                                        <span class="item-text">
                                            <span class="item-name">Himalayan Sanctuary</span>
                                            <span class="item-sub">Rishikesh · Haridwar · Yoga</span>
                                        </span>
                                    </a>
                                </div>
                            </div>
                        </div>"""

# Regex to find <div class="dropdown-menu ..."> up to its closing </div>
# We need to handle both "mega-menu" class (already updated files) and plain "dropdown-menu"
pattern = re.compile(
    r'(<a [^>]*dropdown-toggle[^>]*>.*?</a>\s*)<div class="dropdown-menu[^"]*">.*?</div>(\s*</div>)',
    re.DOTALL
)

def repl(match):
    return match.group(1) + new_dropdown_content + match.group(2)

updated_count = 0
for filename in os.listdir(repo_path):
    if filename.endswith(".html"):
        filepath = os.path.join(repo_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = pattern.sub(repl, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"Updated {filename}")

print(f"\nDone! Updated {updated_count} files.")
