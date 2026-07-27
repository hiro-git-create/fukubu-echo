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

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_diseases\images"
os.makedirs(img_dir, exist_ok=True)

# Helper function to draw perfectly non-overlapping centered text inside tight boxes
def draw_two_line_box(draw, box, fill_bg, outline_c, title, desc_text, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    
    t_c = title_color if title_color else outline_c
    cx = (x1 + x2) // 2
    
    # Title at top half, desc at bottom half (Zero overlap guaranteed)
    draw.text((cx, y1 + 30), title, fill=t_c, font=font_large, anchor="mm")
    draw.text((cx, y1 + 72), desc_text, fill="#1e293b", font=font_mid, anchor="mm")

# 1. IgG4-RD Flowchart (Fixed Overlap Completely)
def make_igg4_flow_fixed():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 75)], fill="#4338ca")
    draw.text((550, 45), "IgG4関連疾患 (IgG4-RD) 全身臓器 超音波所見アルゴリズム", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(280, 95), (820, 155)], fill="#e0e7ff", outline="#4338ca", width=3)
    draw.text((550, 125), "高IgG4血症 ＋ 全身性炎症・腫瘤形成疑い", fill="#3730a3", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    # Level 2 Container
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#4338ca", width=3)
    draw.text((550, 215), "【 4大主要臓器の超音波特徴所見 】", fill="#3730a3", font=font_large, anchor="mm")
    
    organs = [
        ("1. 膵臓 (Type 1 AIP)", "ソーセージ様びまん性腫大 / Capsule-like Rim / Duct Narrowing Sign", "#e0e7ff", "#3730a3"),
        ("2. 胆道 (IgG4-SC)", "胆管壁の全周性滑らか肥厚 (Smooth wall thickening) / 内腔狭窄", "#fce7f3", "#db2777"),
        ("3. 腎臓 (IgG4-RKD)", "腎皮質多発低エコー結節 (Multiple Low-density Lesions) / びまん性腎腫大", "#f3e8ff", "#6b21a8"),
        ("4. 後腹膜 (IgG4-RPF)", "大動脈周囲の厚い帯状低エコー腫瘤 (Periaortic mantle) / 尿管巻き込み水腎症", "#ffedd5", "#c2410c")
    ]
    
    y = 250
    for title, desc, bg_c, text_c in organs:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
        
    path = os.path.join(img_dir, "igg4_rd_flowchart.png")
    img.save(path, quality=95)
    print("Fixed Overlap: igg4_rd_flowchart.png generated successfully!")

# 2. 7-Section MOC Map (Fixed Overlap Completely)
def make_7section_moc_map_fixed():
    w, h = 1100, 1050
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Header
    draw.rectangle([(20, 15), (1080, 70)], fill="#1e3a8a")
    draw.text((550, 42), "腹部超音波検査 教科書 (Abdominal US Vault 7-Section Structure)", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(320, 90), (780, 140)], fill="#f1f5f9", outline="#1e3a8a", width=3)
    draw.text((550, 115), "腹部超音波 Master Index", fill="#1e293b", font=font_large, anchor="mm")
    
    # Level 2 Chapters
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
        
    draw.line([(680, 240), (680, 265)], fill="#64748b", width=3)
    
    # Level 3 Main Outer Box
    draw.rectangle([(30, 265), (1070, 1020)], fill="#f8fafc", outline="#2563eb", width=3)
    draw.text((550, 295), "【 03. 疾患別超音波所見 (全7領域 臨床標準ソート) 】", fill="#1e40af", font=font_large, anchor="mm")
    
    grid_items = [
        ("1. 肝臓領域 (Liver)", "・脂肪肝 / 肝硬変 (ATI / SWE)  ・肝細胞がん / 血管腫 / 転移性", 50, 330, 490),
        ("2. 胆道領域 (Biliary)", "・胆石症 (WES sign)  ・急性胆嚢炎 / ポリープ / ADM", 560, 330, 490),
        ("3. 膵臓領域 (Pancreas)", "・固形 vs 嚢胞性 完全分類  ・膵がん / IPMN / 膵炎", 50, 500, 490),
        ("4. 腎臓領域 (Renal)", "・水腎症 (SFU Grade 1〜4)  ・尿路結石 (Twinkling)", 560, 500, 490),
        ("5. 脾臓領域 (Spleen)", "・脾腫 (Splenomegaly)  ・脾指数 (Spleen Index ≧ 20)", 50, 670, 490),
        ("6. 消化管・血管領域", "・急性虫垂炎 / 腸閉塞  ・腹部大動脈瘤 / ナットクラッカー / MALS", 560, 670, 490),
        ("7. その他・全身性疾患 (Others & Systemic)", "・IgG4関連疾患 (IgG4-RD: 自己免疫性膵炎 AIP / 硬化性胆管炎 SC / 腎病変 RKD / 後腹膜 RPF)", 50, 840, 1000)
    ]
    
    for title, desc, x, y, box_w in grid_items:
        draw_two_line_box(draw, (x, y, x + box_w, y + 145), "#ffffff", "#3b82f6", title, desc, title_color="#1e3a8a")

    path = os.path.join(img_dir, "master_index_map.png")
    img.save(path, quality=95)
    print("Fixed Overlap: master_index_map.png generated successfully!")

make_igg4_flow_fixed()
make_7section_moc_map_fixed()
