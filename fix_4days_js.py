import os
import re

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
js_file = os.path.join(repo_path, '4-days-golden-triangle-tour.js')

with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_car_data = """        car: {
            duration: "4 Days / 3 Nights",
            cities: "Delhi - Agra - Jaipur",
            price: "$190 p.p.",
            shortDesc: "Embark on an unforgettable 4-day private journey through India's famed Golden Triangle. Travel comfortably in a private, air-conditioned vehicle with expert local guides bringing history to life at every stop.",
            highlight: "✨ Includes a dedicated private car with personal driver, hotel pickups, and scenic highway drives between the major cities.",
            itinerary: [
                { day: 1, title: "The Magic of Delhi & Journey to Agra", desc: "Your adventure begins with a flexible morning pickup from anywhere in the Delhi NCR region. We dive straight into history at the towering Qutub Minar, followed by the peaceful, lotus-shaped Bahá'í House of Worship. Enjoy a scenic drive past the majestic Red Fort, India Gate, and the grand Parliament House. Uncover the mysteries of the ancient Agrasen Ki Baoli stepwell, and marvel at Humayun's Tomb, the inspiration for the Taj Mahal. After a delicious local lunch at Connaught Place, we’ll explore the vibrant chaos of Old Delhi—riding through the spice-scented lanes of Chandni Chowk, admiring the grand Jama Masjid, and visiting Asia's largest spice market, Khari Baoli. In the evening, relax on a comfortable drive to Agra, where you'll check into your hotel for the night." },
                { day: 2, title: "Sunrise at the Taj Mahal & The Road to the Pink City", desc: "Rise early for an unforgettable sunrise visit to the Taj Mahal. Watch the marble monument change colors in the morning light as your guide shares the timeless love story behind its creation. After breakfast at your hotel, we’ll explore the sprawling courtyards of the imposing Agra Fort. Next, visit the delicate Itmad-ud-Daulah, affectionately known as the \\"Baby Taj.\\" After savoring authentic Agra cuisine for lunch, you'll be driven comfortably to the vibrant \\"Pink City\\" of Jaipur to relax and spend the night." },
                { day: 3, title: "Royal Jaipur City Tour", desc: "After a hearty breakfast, begin your exploration of Jaipur's royal heritage. Start at the formidable Jaigarh Fort, perched high on the Aravalli hills and home to the world's largest wheeled cannon. Next, wander through the opulent City Palace, a dazzling blend of Rajasthani and Mughal architecture. Take a moment to photograph the serene Jal Mahal (Water Palace) floating in Man Sagar Lake, and admire the iconic Hawa Mahal (Palace of Winds), with its intricate lattice windows designed for royal ladies. Conclude your day of sightseeing at the Jantar Mantar observatory, a fascinating collection of giant astronomical instruments." },
                { day: 4, title: "Farewell and Departure", desc: "Enjoy your final morning in Rajasthan. Depending on your onward travel plans, your driver will either take you on a comfortable drive back to your requested drop-off point in Delhi, or provide a convenient drop-off at Jaipur Airport." }
            ],
            inclusions: [
                "Private air-conditioned vehicle",
                "Hotel pickup and drop-off",
                "English-speaking local guides",
                "3 nights accommodation (with breakfast)",
                "Bottled water"
            ],
            exclusions: [
                "Monument admission tickets (unless specifically requested)",
                "Meals (lunch/dinner)",
                "Gratuities"
            ]
        },
"""

# Use regex to replace the 'car: { ... },' object entirely
pattern = re.compile(r'car:\s*\{.*?(?=\s+train:|\s+flight:)', re.DOTALL)
js_content = pattern.sub(new_car_data, js_content)

# The user might have selected 'train' or 'flight', but since this is 'by Car', let's hide the mode selector if it exists in the HTML.
with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)
