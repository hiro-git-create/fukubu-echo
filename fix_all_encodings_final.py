import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Find all markdown files recursively
md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

fixed_count = 0
for filepath in md_files:
    try:
        # Read content using flexible encoding handling
        content = None
        for enc in ['utf-8-sig', 'utf-8', 'cp932', 'shift_jis']:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        if content is not None:
            # Overwrite with clean UTF-8 without BOM (Standard Unix/Obsidian format)
            with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
            fixed_count += 1
            print(f"Re-encoded safely: {os.path.relpath(filepath, base_dir)}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print(f"Total files verified and clean UTF-8 encoded: {fixed_count}")
