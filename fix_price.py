import os

repo_path = 'C:/Users/raman/.gemini/antigravity/scratch/grand_repo'

for fn in ['index.html', 'all-tours.html']:
    fp = os.path.join(repo_path, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<span class="price"> <span class="pp">/ person</span></span>', '<span class="price">$68 <span class="pp">/ person</span></span>')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)

fp = os.path.join(repo_path, 'delhi-museum-tour.html')
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()
    
# Replace FAQ answer
c = c.replace('Your $65 per person package', 'Your $68 per person package')

# Replace the meta-icon from 55 to 68
c = c.replace('From $55 p.p.', 'From $68 p.p.')

with open(fp, 'w', encoding='utf-8') as f:
    f.write(c)

print('Done.')
