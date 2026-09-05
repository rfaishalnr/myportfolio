import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Directories containing compressed images
prefixes = [
    'assets/img/portfolio/pataweb/',
    'assets/img/portfolio/pesanmakan/',
    'assets/img/portfolio/webcigalontang/',
    'assets/img/sertif/',
]

for prefix in prefixes:
    # Replace all occurrences of prefix + filename.png with prefix + filename.jpg
    pattern = re.compile(r'(' + re.escape(prefix) + r'[^"]+)\.png')
    content = pattern.sub(r'\1.jpg', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! All portfolio .png paths updated to .jpg')
