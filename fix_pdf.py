import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: object-fit: cover -> object-fit: contain (only inside pdf-template)
# We only change the images inside the pdf-template section
pdf_start = content.find('<div id="pdf-template"')
pdf_end = content.find('<!-- Footer -->', pdf_start)

pdf_section = content[pdf_start:pdf_end]
pdf_section_fixed = pdf_section.replace('object-fit: cover', 'object-fit: contain')
# Also add white background for contain mode
pdf_section_fixed = pdf_section_fixed.replace(
    'object-fit: contain; border-radius: 2mm; border: 0.3mm solid #ddd;',
    'object-fit: contain; border-radius: 2mm; border: 0.3mm solid #ddd; background: #f8f8f8;'
)

content = content[:pdf_start] + pdf_section_fixed + content[pdf_end:]

# Fix 2: Replace flag emojis with styled text badges
content = content.replace(
    '🇮🇩 Indonesia <span style="color: rgba(255,255,255,0.65);">(Native)</span>',
    '<span style="display:inline-block;background:rgba(255,255,255,0.2);padding:0.5mm 2mm;border-radius:1mm;font-size:6.5pt;font-weight:700;margin-right:1.5mm;">ID</span> Indonesia <span style="color: rgba(255,255,255,0.65);">(Native)</span>'
)
content = content.replace(
    '🇬🇧 English <span style="color: rgba(255,255,255,0.65);">(Intermediate)</span>',
    '<span style="display:inline-block;background:rgba(255,255,255,0.2);padding:0.5mm 2mm;border-radius:1mm;font-size:6.5pt;font-weight:700;margin-right:1.5mm;">EN</span> English <span style="color: rgba(255,255,255,0.65);">(Intermediate)</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! object-fit and flag fixes applied.')
