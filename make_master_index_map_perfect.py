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

# Master Index Map Generator (Perfect Width: 1350px, Height: 950px)
def make_perfect_master_index_map():
    w, h = 1350, 950
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header Box
    draw.rectangle([(30, 20), (1320, 80)], fill="#1e3a8a")
    draw.text((675, 50), "腹部超音波検査 教科書 (Abdominal US Vault 7-Section Structure)", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(475, 105), (875, 155)], fill="#ffffff", outline="#1e3a8a", width=2)
    draw.text((675, 130), "腹部超音波 Master Index", fill="#1e3a8a", font=font_large, anchor="mm")
    
    # Connecting Lines
    draw.line([(675, 155), (675, 185)], fill="#64748b", width=2)
    draw.line([(140, 185), (1210, 185)], fill="#64748b", width=2)
    
    # Top 4 Modules
    top_mods = [
        ("01. 基本事項・走査法", 40, 310),
        ("02. 臓器別標準解剖", 340, 610),
        ("03. 疾患別超音波所見", 640, 910),
        ("04. 計測手技マニュアル", 940, 1210)
    ]
    for m_name, x1, x2 in top_mods:
        cx = (x1 + x2) // 2
        draw.line([(cx, 185), (cx, 205)], fill="#64748b", width=2)
        draw.rectangle([(x1, 205), (x2, 255)], fill="#f1f5f9", outline="#334155", width=2)
        draw.text((cx, 230), m_name, fill="#1e293b", font=font_mid, anchor="mm")
        
    draw.line([(775, 255), (775, 285)], fill="#64748b", width=2)
    
    # Large Section Container
    draw.rectangle([(30, 285), (1320, 920)], fill="#ffffff", outline="#2563eb", width=3)
    draw.text((675, 315), "【 03. 疾患別超音波所見 (全7領域 臨床標準ソート) 】", fill="#1d4ed8", font=font_large, anchor="mm")
    
    # 7 Clinical Grid Sections (Width: 610px each)
    grid_boxes = [
        # (Title, Line1, Line2, x1, y1, x2, y2)
        ("1. 肝臓領域 (Liver)", "・脂肪肝 / 肝硬変 (ATI / SWE)", "・肝細胞がん / 血管腫 / 転移性肝がん", 60, 345, 660, 480),
        ("2. 胆道領域 (Biliary)", "・胆石症 (WES sign)", "・急性・慢性胆嚢炎 / ポリープ / ADM", 690, 345, 1290, 480),
        
        ("3. 膵臓領域 (Pancreas)", "・固形 vs 嚢胞性 完全分類", "・膵がん / IPMN / 膵炎", 60, 500, 660, 635),
        ("4. 腎臓領域 (Renal)", "・水腎症 (SFU Grade 1～4)", "・腎嚢胞 / 尿路結石 (Twinkling)", 690, 500, 1290, 635),
        
        ("5. 脾臓領域 (Spleen)", "・脾腫 (Splenomegaly)", "・脾指数 (Spleen Index ≧ 20cm²)", 60, 655, 660, 790),
        ("6. 消化管・血管領域 (GI & Vessels)", "・急性虫垂炎 / 腸閉塞・イレウス", "・腹部大動脈瘤 / ナットクラッカー / MALS / SMA症候群", 690, 655, 1290, 790),
        
        ("7. その他・全身性疾患 (Others & Systemic)", "・IgG4関連疾患 (IgG4-RD: 自己免疫性膵炎 AIP / 硬化性胆管炎 SC / 腎病変 RKD / 後腹膜線維症 RPF)", "", 60, 810, 1290, 900)
    ]
    
    for title, line1, line2, x1, y1, x2, y2 in grid_boxes:
        draw.rectangle([(x1, y1), (x2, y2)], fill="#f8fafc", outline="#3b82f6", width=2)
        cx = (x1 + x2) // 2
        
        if y2 - y1 > 100:
            draw.text((cx, y1 + 30), title, fill="#1d4ed8", font=font_large, anchor="mm")
            draw.text((cx, y1 + 70), line1, fill="#334155", font=font_small, anchor="mm")
            if line2:
                draw.text((cx, y1 + 102), line2, fill="#334155", font=font_small, anchor="mm")
        else:
            draw.text((cx, y1 + 28), title, fill="#1d4ed8", font=font_large, anchor="mm")
            draw.text((cx, y1 + 62), line1, fill="#334155", font=font_small, anchor="mm")

    path = os.path.join(img_dir, "master_index_map.png")
    img.save(path, quality=95)
    print("Master perfect master_index_map.png generated successfully!")

make_perfect_master_index_map()
