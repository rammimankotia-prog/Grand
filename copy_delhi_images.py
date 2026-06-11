import shutil
import glob
import os

brain = r"C:\Users\raman\.gemini\antigravity\brain\435f7721-6eb8-4ae2-9dc6-ab15c40122f9"
assets = r"C:\Users\raman\.gemini\antigravity\scratch\grand_repo\assets"

images = {
    "india_gate_delhi": "india_gate_delhi.png",
    "chandni_chowk_market": "chandni_chowk_market.png",
    "delhi_food_street": "delhi_food_street.png",
    "lotus_temple_delhi": "lotus_temple_delhi.png",
    "delhi_nightlife": "delhi_nightlife.png",
    "qutub_minar_delhi": "qutub_minar_delhi.png",
}

for prefix, dest_name in images.items():
    matches = sorted(glob.glob(os.path.join(brain, f"{prefix}_*.png")))
    if matches:
        src = matches[-1]
        dest = os.path.join(assets, dest_name)
        shutil.copy2(src, dest)
        print(f"Copied {src} -> {dest}")
    else:
        print(f"NOT FOUND: {prefix}")
