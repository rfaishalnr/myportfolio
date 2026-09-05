with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 1038 onward until <footer id="footer"> is the old duplicate
# New template ends at line ~1034 (closing </div>)
# Old content starts at line 1039 (we know LEFT SIDEBAR is at 1041)
# Real footer is somewhere after line 1211

new_lines = []
skip = False
footer_found = False

for i, line in enumerate(lines, 1):
    if i == 1039:  # Start skipping from here (after new template ends)
        skip = True
    
    if skip and '<footer id="footer">' in line:
        skip = False
        footer_found = True
        new_lines.append('\n  <!-- Footer -->\n')
    
    if not skip:
        new_lines.append(line)

print(f"Footer found: {footer_found}")
print(f"New line count: {len(new_lines)}")

with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.writelines(new_lines)

print("Done!")
