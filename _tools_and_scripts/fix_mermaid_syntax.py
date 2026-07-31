import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Fix subgraph lines like `subgraph 固形腫瘤 (Solid)` to `subgraph SubSolid ["固形腫瘤 (Solid)"]`
    def fix_subgraph(match):
        label = match.group(1).strip()
        # Create a safe ASCII identifier
        safe_id = "Sub_" + re.sub(r'[^a-zA-Z0-9]', '', label)
        if not safe_id or safe_id == "Sub_":
            safe_id = "Sub_Group"
        return f'subgraph {safe_id} ["{label}"]'

    new_content = re.sub(r'subgraph\s+([^\n\["]+)\n', fix_subgraph, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8-sig', newline='\n') as f:
            f.write(new_content)
        print(f"Fixed Mermaid in {os.path.basename(filepath)}")

print("All Mermaid diagrams checked and fixed for syntax safety!")
