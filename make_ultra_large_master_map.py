import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 34)
            font_large = ImageFont.truetype(fp, 26)
            font_mid = ImageFont.truetype(fp, 22)
            font_small = ImageFont.truetype(fp, 20)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"

# Ultra Large Text Master Index Map Generator (Height: 1250px)
def make_ultra_large_master_index_map():
    w, h = 1400, 1250
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header Box
    draw.rectangle([(30, 20), (1370, 85)], fill="#1e3a8a")
    draw.text((700, 52), "腹部超音波検査 教科書 (Abdominal US Vault 7-Section Structure)", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(475, 110), (925, 165)], fill="#ffffff", outline="#1e3a8a", width=2)
    draw.text((700, 137), "腹部超音波 Master Index", fill="#1e3a8a", font=font_large, anchor="mm")
    
    # Connecting Lines
    draw.line([(700, 165), (700, 195)], fill="#64748b", width=2)
    draw.line([(140, 195), (1260, 195)], fill="#64748b", width=2)
    
    # Top 4 Modules
    top_mods = [
        ("01. 基本事項・走査法", 30, 320),
        ("02. 臓器別標準解剖", 360, 650),
        ("03. 疾患別超音波所見", 690, 980),
        ("04. 計測手技マニュアル", 1020, 1370)
    ]
    for m_name, x1, x2 in top_mods:
        cx = (x1 + x2) // 2
        draw.line([(cx, 195), (cx, 215)], fill="#64748b", width=2)
        draw.rectangle([(x1, 215), (x2, 270)], fill="#f1f5f9", outline="#334155", width=2)
        draw.text((cx, 242), m_name, fill="#1e293b", font=font_mid, anchor="mm")
        
    draw.line([(835, 270), (835, 300)], fill="#64748b", width=2)
    
    # Large Section Container (Height: 900px)
    draw.rectangle([(30, 300), (1370, 1220)], fill="#ffffff", outline="#2563eb", width=3)
    draw.text((700, 335), "【 03. 疾患別超音波所見 (全7領域 臨床標準ソート) 】", fill="#1d4ed8", font=font_large, anchor="mm")
    
    # 7 Clinical Grid Sections (Spacious height: 180px each)
    grid_boxes = [
        ("1. 肝臓領域 (Liver)", "・脂肪肝 / 肝硬変 (ATI / SWE)", "・肝細胞がん / 血管腫 / 転移性肝がん", 60, 370, 680, 540),
        ("2. 胆道領域 (Biliary)", "・胆石症 (WES sign)", "・急性・慢性胆嚢炎 / ポリープ / ADM", 720, 370, 1340, 540),
        
        ("3. 膵臓領域 (Pancreas)", "・固形 vs 嚢胞性 完全分類", "・膵がん / IPMN / 膵炎", 60, 570, 680, 740),
        ("4. 腎臓領域 (Renal)", "・水腎症 (SFU Grade 1～4)", "・腎嚢胞 / 尿路結石 (Twinkling)", 720, 570, 1340, 740),
        
        ("5. 脾臓領域 (Spleen)", "・脾腫 (Splenomegaly)", "・脾指数 (Spleen Index ≧ 20cm²)", 60, 770, 680, 940),
        ("6. 消化管・血管領域 (GI & Vessels)", "・急性虫垂炎 / 腸閉塞・イレウス", "・腹部大動脈瘤 / ナットクラッカー / MALS / SMA症候群", 720, 770, 1340, 940),
        
        ("7. その他・全身性疾患 (Others & Systemic)", "・IgG4関連疾患 (IgG4-RD)", "自己免疫性膵炎 AIP / 硬化性胆管炎 SC / 腎病変 RKD / 後腹膜線維症 RPF", 60, 970, 1340, 1190)
    ]
    
    for title, line1, line2, x1, y1, x2, y2 in grid_boxes:
        draw.rectangle([(x1, y1), (x2, y2)], fill="#f8fafc", outline="#3b82f6", width=2)
        cx = (x1 + x2) // 2
        
        draw.text((cx, y1 + 40), title, fill="#1d4ed8", font=font_large, anchor="mm")
        draw.text((cx, y1 + 90), line1, fill="#334155", font=font_small, anchor="mm")
        if line2:
            draw.text((cx, y1 + 130), line2, fill="#334155", font=font_small, anchor="mm")

    path = os.path.join(img_dir, "master_index_map.png")
    img.save(path, quality=95)
    print("Ultra Large Text master_index_map.png generated successfully!")

make_ultra_large_master_index_map()
