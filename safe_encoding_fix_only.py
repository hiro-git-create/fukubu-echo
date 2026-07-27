import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Find all markdown files in current state
md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

for filepath in md_files:
    try:
        # Try reading with different encodings
        content = None
        for enc in ['utf-8-sig', 'utf-8', 'cp932', 'shift_jis']:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        if content is not None:
            # Overwrite keeping exact structure but ensuring clean UTF-8 with BOM for Windows/Obsidian
            with open(filepath, 'w', encoding='utf-8-sig', newline='\n') as f:
                f.write(content)
            print(f"Cleaned encoding for: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Encoding fix completed without touching file paths or contents!")
