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
            font_small = ImageFont.truetype(fp, 16)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

def make_moc_image():
    w, h = 1100, 520
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 70)], fill="#1e3a8a")
    draw.text((550, 42), "腹部超音波検査 教科書 (Abdominal US Vault Structure)", fill="#ffffff", font=font_title, anchor="mm")
    
    # Root
    draw.rectangle([(320, 90), (780, 140)], fill="#f1f5f9", outline="#1e3a8a", width=3)
    draw.text((550, 115), "腹部超音波 Master Index", fill="#1e293b", font=font_large, anchor="mm")
    
    # Level 2 Chapters
    chaps = [
        ("01. 基本事項・走査法", 100),
        ("02. 臓器別標準解剖", 360),
        ("03. 疾患別超音波所見", 620),
        ("04. 計測手技マニュアル", 880)
    ]
    
    draw.line([(550, 140), (550, 165)], fill="#64748b", width=3)
    draw.line([(190, 165), (970, 165)], fill="#64748b", width=3)
    
    for title, cx in chaps:
        draw.line([(cx + 90, 165), (cx + 90, 190)], fill="#64748b", width=3)
        draw.rectangle([(cx, 190), (cx + 180, 240)], fill="#e2e8f0", outline="#475569", width=2)
        draw.text((cx + 90, 215), title, fill="#1e293b", font=font_mid, anchor="mm")
        
    # Level 3: Diseases Sequence (Clinical Sorted)
    draw.line([(710, 240), (710, 270)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 270), (1070, 490)], fill="#f8fafc", outline="#2563eb", width=3)
    draw.text((550, 298), "【 03. 疾患別超音波所見 (標準臨床順序) 】", fill="#1e40af", font=font_large, anchor="mm")
    
    seq_items = [
        ("1. 肝臓 (Liver)", ["脂肪肝 / 肝硬変", "肝細胞がん / 血管腫"]),
        ("2. 胆道 (Biliary)", ["胆石症 / 急性胆嚢炎", "胆嚢ポリープ / ADM"]),
        ("3. 膵臓 (Pancreas)", ["固形 vs 嚢胞性分類", "膵がん / IPMN / 膵炎"]),
        ("4. 腎臓・脾臓", ["水腎症 / 脾腫", "Twinkling"]),
        ("5. 消化管 (GI)", ["急性虫垂炎", "腸閉塞・イレウス"]),
        ("6. 血管 (Vessels)", ["腹部大動脈瘤", "ナットクラッカー/MALS"])
    ]
    
    x = 45
    for title, desc in seq_items:
        draw.rectangle([(x, 330), (x + 160, 470)], fill="#ffffff", outline="#3b82f6", width=2)
        draw.text((x + 80, 355), title, fill="#1e3a8a", font=font_mid, anchor="mm")
        draw.text((x + 80, 400), desc[0], fill="#475569", font=font_small, anchor="mm")
        draw.text((x + 80, 435), desc[1], fill="#475569", font=font_small, anchor="mm")
        x += 170

    path = os.path.join(img_dir, "master_index_map.png")
    img.save(path, quality=95)
    print("Created master_index_map.png successfully!")

make_moc_image()
