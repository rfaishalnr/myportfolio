"""
Compress all portfolio and certificate images for faster PDF rendering.
Target: max 1000px wide, JPEG quality 65
"""
from PIL import Image
import os

dirs = [
    "assets/img/portfolio/pataweb",
    "assets/img/portfolio/pesanmakan",
    "assets/img/portfolio/webcigalontang",
    "assets/img/sertif",
]

MAX_WIDTH = 1000
QUALITY = 65

for d in dirs:
    if not os.path.exists(d):
        continue
    for fname in os.listdir(d):
        if not fname.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        fpath = os.path.join(d, fname)
        original_size = os.path.getsize(fpath)
        
        try:
            img = Image.open(fpath).convert("RGB")
            w, h = img.size
            if w > MAX_WIDTH:
                ratio = MAX_WIDTH / w
                img = img.resize((MAX_WIDTH, int(h * ratio)), Image.LANCZOS)
            
            # Save as JPEG for smaller size
            out_path = os.path.splitext(fpath)[0] + ".jpg"
            img.save(out_path, "JPEG", quality=QUALITY, optimize=True)
            
            # Remove original PNG if different path
            if out_path != fpath and os.path.exists(fpath):
                os.remove(fpath)
            
            new_size = os.path.getsize(out_path)
            saved = (1 - new_size / original_size) * 100
            print(f"OK  {fname} -> {new_size//1024}KB (saved {saved:.0f}%)")
        except Exception as e:
            print(f"ERR {fname}: {e}")

print("\nDone! All images compressed.")
