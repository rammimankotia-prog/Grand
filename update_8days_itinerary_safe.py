import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'
js_file = os.path.join(repo_path, '8-days-golden-triangle-tour.js')

with open(js_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_itinerary = """            itinerary: [
                { day: 1, title: "Arrival & Welcome to Delhi", desc: "Arrive at New Delhi International Airport where our representative will warmly welcome you. Transfer via private luxury car to Hotel Godwin Deluxe, your premium stay in the heart of the city. Spend the evening relaxing and acclimatizing to the vibrant energy of India." },
                { day: 2, title: "Delhi Sightseeing: Old & New", desc: "After a hearty breakfast at Hotel Godwin Deluxe, dive into Delhi's rich history. Explore the grand Jama Masjid, enjoy a thrilling rickshaw ride through Chandni Chowk, and visit the serene Rajghat. Later, marvel at the towering Qutub Minar and the magnificent Humayun's Tomb, before driving past the grand India Gate and Parliament House." },
                { day: 3, title: "Delhi to Agra: The City of Love", desc: "Enjoy a morning drive to Agra via the Yamuna Expressway. Upon arrival, check-in to your luxury hotel. In the afternoon, visit the imposing Agra Fort, a UNESCO World Heritage site showcasing spectacular Mughal architecture, followed by a sunset view of the Taj Mahal from Mehtab Bagh." },
                { day: 4, title: "Sunrise at Taj Mahal & Artisan Tour", desc: "Experience the ethereal beauty of the Taj Mahal at dawn. Return for breakfast, then explore the exquisite Tomb of I'timad-ud-Daulah, often called the 'Baby Taj'. Spend the evening visiting local marble inlay artisans whose ancestors built the Taj Mahal." },
                { day: 5, title: "Agra to Jaipur via Fatehpur Sikri", desc: "Depart for Jaipur, the famed Pink City. En route, explore the abandoned red sandstone city of Fatehpur Sikri, built by Emperor Akbar, and marvel at the stunning stepwell, Chand Baori, in Abhaneri village. Arrive in Jaipur and check into your royal heritage hotel." },
                { day: 6, title: "Jaipur Sightseeing & Royal Forts", desc: "Ascend the majestic Amber Fort via a royal elephant or jeep ride. Stop to photograph the breathtaking Jal Mahal sitting in Man Sagar Lake. Later, explore the intricate Hawa Mahal (Palace of Winds), the grand City Palace, and the astronomical wonders of Jantar Mantar." },
                { day: 7, title: "Cultural Immersion in the Pink City", desc: "Spend the morning visiting the historic Nahargarh Fort, offering panoramic views of Jaipur. Later, enjoy a guided heritage walk through the vibrant local bazaars famous for block printing, blue pottery, and exquisite jewelry. Enjoy a traditional Rajasthani dinner in the evening." },
                { day: 8, title: "Jaipur to Delhi & Departure", desc: "After breakfast, enjoy a scenic drive back to New Delhi. Upon arrival, depending on your flight schedule, you can do some last-minute shopping at Connaught Place or be transferred directly to the airport for your onward journey, bringing your Golden Triangle tour to a memorable close." }
            ],
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'car: {' in line:
        # found the car section
        for j in range(i, len(lines)):
            if 'itinerary: [' in lines[j] and start_idx == -1:
                start_idx = j
            elif start_idx != -1 and '],' in lines[j]:
                end_idx = j
                break
        break

if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx+1] = [new_itinerary]

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(''.join(lines))
    
print("Successfully replaced itinerary securely!")
