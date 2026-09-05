import fitz
import os

pdf_dir = "assets/img/sertif"

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_dir, filename)
        doc = fitz.open(filepath)
        page = doc.load_page(0)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        outpath = os.path.join(pdf_dir, filename.replace('.pdf', '.png'))
        pix.save(outpath)
        print(f"Converted {filename} to {outpath}")
