import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

for filepath in md_files:
    try:
        # Try reading with utf-8
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback to cp932/shift_jis if needed
        with open(filepath, 'r', encoding='cp932') as f:
            content = f.read()
    
    # Save as UTF-8 with BOM for crisp display in Windows & Obsidian
    with open(filepath, 'w', encoding='utf-8-sig') as f:
        f.write(content)
    print(f"Fixed: {os.path.basename(filepath)}")

print("All encoding fixes completed successfully!")
