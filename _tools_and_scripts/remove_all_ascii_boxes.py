import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

# Pattern to catch ASCII boxes like ```text ┌─────┐ ... └─────┘ ```
box_pattern = re.compile(r'```text\s*┌[─┬┐\s\S]*?└[─┴┘\s\S]*?```', re.MULTILINE)

def clean_ascii_box(match):
    text = match.group(0)
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        if '```' in line or '┌' in line or '└' in line or '├' in line:
            continue
        # Remove leading/trailing box borders | or │
        line = re.sub(r'^[│|]\s*', '- ', line)
        line = re.sub(r'\s*[│|]$', '', line)
        if line.strip():
            cleaned_lines.append(line.strip())
    
    formatted = "> [!IMPORTANT] 要点・チェックポイント\n" + "\n".join([f"> {l}" if not l.startswith(">") else l for l in cleaned_lines])
    return formatted

count = 0
for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    if '┌' in content or '└' in content or '│' in content:
        new_content = box_pattern.sub(clean_ascii_box, content)
        
        # Secondary cleanup for any loose ascii borders
        new_content = re.sub(r'┌[─┬┐]+┐', '', new_content)
        new_content = re.sub(r'└[─┴┘]+┘', '', new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8-sig', newline='\n') as f:
                f.write(new_content)
            print(f"Fixed ASCII box in: {os.path.basename(filepath)}")
            count += 1

print(f"ASCII border cleanup completed in {count} files!")
