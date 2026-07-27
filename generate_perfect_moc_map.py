import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 30)
            font_large = ImageFont.truetype(fp, 24)
            font_mid = ImageFont.truetype(fp, 20)
            font_small = ImageFont.truetype(fp, 17)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

def make_moc_vertical_map():
    w, h = 1100, 920
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Header
    draw.rectangle([(20, 15), (1080, 70)], fill="#1e3a8a")
    draw.text((550, 42), "腹部超音波検査 教科書 (Abdominal US Vault Structure)", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(320, 90), (780, 140)], fill="#f1f5f9", outline="#1e3a8a", width=3)
    draw.text((550, 115), "腹部超音波 Master Index", fill="#1e293b", font=font_large, anchor="mm")
    
    # Level 2 Chapters (Horizontal 4 Boxes)
    chaps = [
        ("01. 基本事項・走査法", 40),
        ("02. 臓器別標準解剖", 300),
        ("03. 疾患別超音波所見", 560),
        ("04. 計測手技マニュアル", 820)
    ]
    
    draw.line([(550, 140), (550, 165)], fill="#64748b", width=3)
    draw.line([(160, 165), (940, 165)], fill="#64748b", width=3)
    
    for title, cx in chaps:
        draw.line([(cx + 120, 165), (cx + 120, 190)], fill="#64748b", width=3)
        draw.rectangle([(cx, 190), (cx + 240, 240)], fill="#e2e8f0", outline="#475569", width=2)
        draw.text((cx + 120, 215), title, fill="#1e293b", font=font_mid, anchor="mm")
        
    # Line to Level 3
    draw.line([(680, 240), (680, 265)], fill="#64748b", width=3)
    
    # Level 3 Main Outer Box (Height: 630px)
    draw.rectangle([(30, 265), (1070, 895)], fill="#f8fafc", outline="#2563eb", width=3)
    draw.text((550, 295), "【 03. 疾患別超音波所見 (標準臨床順序) 】", fill="#1e40af", font=font_large, anchor="mm")
    
    # 2 Columns x 3 Rows Layout (Spacious & Clean)
    grid_items = [
        # Col 0, Row 0
        ("1. 肝臓領域 (Liver)", ["・脂肪肝 / 肝硬変 (ATI / SWE)", "・肝細胞がん / 血管腫 / 転移性"], 50, 330),
        # Col 1, Row 0
        ("2. 胆道領域 (Biliary)", ["・胆石症 (WES sign / 4極鑑別)", "・急性胆嚢炎 / ポリープ / ADM"], 560, 330),
        
        # Col 0, Row 1
        ("3. 膵臓領域 (Pancreas)", ["・固形 vs 嚢胞性 完全分類", "・膵がん / IPMN / 膵炎"], 50, 515),
        # Col 1, Row 1
        ("4. 腎臓・脾臓領域", ["・水腎症 (SFU Grade 1〜4)", "・Twinkling / 脾指数"], 560, 515),
        
        # Col 0, Row 2
        ("5. 消化管領域 (GI)", ["・急性虫垂炎 (外径6mm/壊疽性)", "・腸閉塞・イレウス (ザーゲ像)"], 50, 700),
        # Col 1, Row 2
        ("6. 血管領域 (Vessels)", ["・腹部大動脈瘤 (AAA Outer-to-Outer)", "・ナットクラッカー / MALS"], 560, 700)
    ]
    
    for title, lines, x, y in grid_items:
        draw.rectangle([(x, y), (x + 490, y + 160)], fill="#ffffff", outline="#3b82f6", width=2)
        draw.text((x + 245, y + 35), title, fill="#1e3a8a", font=font_large, anchor="mm")
        draw.text((x + 245, y + 85), lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((x + 245, y + 120), lines[1], fill="#334155", font=font_mid, anchor="mm")

    path = os.path.join(img_dir, "master_index_map.png")
    img.save(path, quality=95)
    print("Vertical Balance Map: master_index_map.png generated!")

make_moc_vertical_map()
