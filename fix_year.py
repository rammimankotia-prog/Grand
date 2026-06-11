with open('delhi-travel-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('2025', '2026')

with open('delhi-travel-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
