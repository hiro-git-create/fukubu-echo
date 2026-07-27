import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"
img_dir = os.path.join(base_dir, "03_疾患別超音波所見", "images")

# List of files with remaining text tables
target_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

# Precision script for Nutcracker and any other file with markdown tables
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

def make_nutcracker_table_img():
    w, h = 1400, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1380, 75)], fill="#0d9488")
    draw.text((700, 45), "ナットクラッカー症候群 4大定量的計測カットオフマトリックス", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [
        ("計測項目", 20, 320),
        ("正常基準 (Normal)", 320, 600),
        ("ナットクラッカー症候群 診断カットオフ", 600, 1040),
        ("臨床的意義・メカニズム", 1040, 1380)
    ]
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#0f766e")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("LRV 径比\n(Diameter Ratio: Dh/De)", "< 2.5", "≧ 4.0 ～ 5.0 ★\n(高度狭窄)", "腎門部径(Dh) ÷ 狭窄部径(De)\nの拡大比"),
        ("LRV 最高血流速度比\n(Ve / Vh Ratio)", "< 3.0", "≧ 5.0 ★\n(狭窄部 Ve > 100 cm/s)", "狭窄部流速(Ve) ÷ 腎門部流速(Vh)\nのJet加速"),
        ("AO-SMA 分岐角\n(SMA Angle)", "45° ～ 60°", "< 35° ★\n(高度例では < 20°)", "SMA分岐角度の鋭角化・挟み込み"),
        ("左性腺静脈血流\n(Gonadal Vein)", "順胞性 (向心性)", "逆流信号 (Reflux) 陽性 ★", "骨盤うっ血症候群 / 精索静脈瘤\nの直接原因")
    ]
    
    cur_y = 145
    row_h = 125
    for i, (item, norm, abn, desc) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0fdf4"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        # Col 1
        draw.rectangle([(20, cur_y), (320, cur_y + row_h)], outline="#cbd5e1", width=2)
        i_lines = item.split('\n')
        if len(i_lines) == 1:
            draw.text((170, cur_y + row_h // 2), item, fill="#0d9488", font=font_large, anchor="mm")
        else:
            draw.text((170, cur_y + 40), i_lines[0], fill="#0d9488", font=font_large, anchor="mm")
            draw.text((170, cur_y + 85), i_lines[1], fill="#0d9488", font=font_mid, anchor="mm")
            
        # Col 2
        draw.rectangle([(320, cur_y), (600, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((460, cur_y + row_h // 2), norm, fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3
        draw.rectangle([(600, cur_y), (1040, cur_y + row_h)], fill="#fef2f2", outline="#cbd5e1", width=2)
        a_lines = abn.split('\n')
        if len(a_lines) == 1:
            draw.text((820, cur_y + row_h // 2), abn, fill="#991b1b", font=font_large, anchor="mm")
        else:
            draw.text((820, cur_y + 40), a_lines[0], fill="#991b1b", font=font_large, anchor="mm")
            draw.text((820, cur_y + 85), a_lines[1], fill="#991b1b", font=font_mid, anchor="mm")
            
        # Col 4
        draw.rectangle([(1040, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        d_lines = desc.split('\n')
        if len(d_lines) == 1:
            draw.text((1210, cur_y + row_h // 2), desc, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((1210, cur_y + 40), d_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((1210, cur_y + 85), d_lines[1], fill="#334155", font=font_mid, anchor="mm")
            
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#0d9488", width=3)
    path = os.path.join(img_dir, "nutcracker_matrix_table.png")
    img.save(path, quality=95)
    print("Generated nutcracker_matrix_table.png successfully!")

make_nutcracker_table_img()
