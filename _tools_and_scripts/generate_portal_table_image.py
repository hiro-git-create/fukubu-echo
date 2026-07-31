import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 26)
            font_large = ImageFont.truetype(fp, 21)
            font_mid = ImageFont.truetype(fp, 18)
            font_small = ImageFont.truetype(fp, 16)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"

# 2. Portal HTN Table Image for Cirrhosis
def make_portal_htn_table():
    w, h = 1150, 420
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1130, 65)], fill="#065f46")
    draw.text((575, 40), "門脈高血圧症 (Portal Hypertension) 超音波血流動態評価表", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [("評価項目", 20, 240), ("正常基準", 240, 460), ("門脈高血圧症 診断カットオフ", 460, 800), ("臨床的意義", 800, 1130)]
    
    y = 80
    draw.rectangle([(20, y), (1130, y + 45)], fill="#059669")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 45)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 22), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("脾腫 (Splenomegaly)", "長径 < 10cm / SI < 20cm²", "長径 ≧ 10.0 cm / 脾指数(SI) ≧ 20 cm²", "脾うっ血・血小板減少の指標"),
        ("門脈幹径 (PV Dia.)", "内径 ≦ 12.0 mm", "内径 ≧ 13.0 mm (1.3 cm)", "門脈圧亢進による血管拡張"),
        ("門脈血流速度 (Vmax)", "向肝性 15 ～ 30 cm/s", "減速 (< 15cm/s) / 向脾性逆流 (Hepatofugal)", "門脈血流の停滞・逆流"),
        ("左胃静脈径 (LGV)", "径 < 4.0 mm", "径 ≧ 5.0 mm", "食道胃静脈瘤ハイリスク"),
        ("臍静脈再開通 (UV)", "完全閉鎖", "肝左葉臍部からの開通血管描出 (Recanalized)", "側副血行路の発達")
    ]
    
    cur_y = 125
    row_h = 55
    for i, (item, norm, abn, desc) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0fdf4"
        draw.rectangle([(20, cur_y), (1130, cur_y + row_h)], fill=bg_c)
        draw.rectangle([(20, cur_y), (240, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((130, cur_y + row_h // 2), item, fill="#065f46", font=font_mid, anchor="mm")
        
        draw.rectangle([(240, cur_y), (460, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((350, cur_y + row_h // 2), norm, fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(460, cur_y), (800, cur_y + row_h)], fill="#fef2f2", outline="#cbd5e1", width=1)
        draw.text((630, cur_y + row_h // 2), abn, fill="#991b1b", font=font_mid, anchor="mm")
        
        draw.rectangle([(800, cur_y), (1130, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((965, cur_y + row_h // 2), desc, fill="#334155", font=font_small, anchor="mm")
        cur_y += row_h

    draw.rectangle([(20, 80), (1130, cur_y)], outline="#065f46", width=3)
    path = os.path.join(img_dir, "portal_htn_table.png")
    img.save(path, quality=95)
    print("Generated portal_htn_table.png successfully!")

make_portal_htn_table()
