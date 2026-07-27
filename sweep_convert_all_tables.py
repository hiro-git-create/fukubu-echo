import os
import glob
import re
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 30)
            font_large = ImageFont.truetype(fp, 24)
            font_mid = ImageFont.truetype(fp, 21)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = ImageFont.load_default()

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"
img_dir = os.path.join(base_dir, "03_疾患別超音波所見", "images")
os.makedirs(img_dir, exist_ok=True)

md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

def render_md_table_to_png(headers, rows, img_filename, doc_title):
    num_cols = len(headers)
    w = 1400
    col_w = (w - 40) // num_cols
    cols = []
    for i, h_name in enumerate(headers):
        x1 = 20 + i * col_w
        x2 = 20 + (i + 1) * col_w if i < num_cols - 1 else 1380
        cols.append((h_name, x1, x2))
        
    row_h = 120
    h = 100 + len(rows) * row_h + 30
    
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1380, 75)], fill="#1e3a8a")
    draw.text((700, 45), doc_title, fill="#ffffff", font=font_title, anchor="mm")
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#2563eb")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        clean_name = re.sub(r'[*_`$]', '', name)
        draw.text(((x1 + x2) // 2, y + 28), clean_name, fill="#ffffff", font=font_large, anchor="mm")
        
    cur_y = 145
    for r_idx, row in enumerate(rows):
        bg_c = "#ffffff" if r_idx % 2 == 0 else "#f8fafc"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        for c_idx, cell in enumerate(row):
            x1, x2 = cols[c_idx][1], cols[c_idx][2]
            draw.rectangle([(x1, cur_y), (x2, cur_y + row_h)], outline="#cbd5e1", width=2)
            
            clean_cell = re.sub(r'[*_`$]', '', cell).replace('<br>', '\n')
            lines = clean_cell.split('\n')
            if len(lines) == 1:
                draw.text(((x1 + x2) // 2, cur_y + row_h // 2), clean_cell, fill="#1e293b", font=font_mid, anchor="mm")
            else:
                draw.text(((x1 + x2) // 2, cur_y + 40), lines[0], fill="#1e293b", font=font_mid, anchor="mm")
                draw.text(((x1 + x2) // 2, cur_y + 85), lines[1], fill="#1e293b", font=font_mid, anchor="mm")
                
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#1e3a8a", width=3)
    img_path = os.path.join(img_dir, img_filename)
    img.save(img_path, quality=95)

table_block_re = re.compile(r'(\|[^\n]+\|\n\|[-:| ]+\|\n(?:\|[^\n]+\|\n?)+)', re.MULTILINE)

total_converted = 0
for filepath in md_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    blocks = table_block_re.findall(content)
    if blocks:
        new_content = content
        for idx, block in enumerate(blocks):
            lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
            if len(lines) >= 3:
                headers = [c.strip() for c in lines[0].split('|')[1:-1]]
                rows = []
                for r_line in lines[2:]:
                    cols = [c.strip() for c in r_line.split('|')[1:-1]]
                    if len(cols) == len(headers):
                        rows.append(cols)
                        
                if headers and rows:
                    img_name = f"auto_table_{fname.replace('.md', '')}_{idx+1}.png"
                    doc_t = fname.replace('.md', '').replace('_', ' ') + " 比較判定表"
                    render_md_table_to_png(headers, rows, img_name, doc_t)
                    
                    new_content = new_content.replace(block, f"![[{img_name}]]")
                    total_converted += 1
                    
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8-sig', newline='\n') as f:
                f.write(new_content)
            print(f"Auto-converted text tables to PNG in: {fname}")

print(f"Total tables converted across entire vault: {total_converted}")
