import os

file_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo/delhi-museum-tour.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace SVG texts
content = content.replace('JAMA MASJID', 'NATIONAL MUSEUM')
content = content.replace('RED FORT', '')
content = content.replace('RAJ GHAT', '')
content = content.replace('INDIA GATE', 'RAIL MUSEUM')
content = content.replace("HUMAYUN'S TOMB", "")
content = content.replace('LOTUS TEMPLE', '')
content = content.replace('QUTUB MINAR', 'DOLLS MUSEUM')
content = content.replace('DELHI LOCAL SIGHTSEEING CIRCUIT', 'DELHI MUSEUM CIRCUIT')

# Replace tags for Rail Museum
content = content.replace('<span>India Gate</span><span>Rashtrapati Bhavan</span><span>Raj Ghat</span>', '<span>Vintage Locomotives</span><span>Fairy Queen</span><span>Toy Train</span>')

# Replace tags for Dolls Museum
content = content.replace("<span>Humayun's Tomb</span><span>Qutub Minar</span><span>Lotus Temple</span>", "<span>6,000+ Dolls</span><span>85 Countries</span><span>Cultural Costumes</span>")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated route map.")
