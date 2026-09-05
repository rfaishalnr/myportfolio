with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'LEFT SIDEBAR' in line or 'pdf-profile-page' in line or ('pdf-page' in line and 'div' in line):
        print(f"L{i}: {line.rstrip()[:100]}")
