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

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\04_実践スクリーニング・計測\images"
os.makedirs(img_dir, exist_ok=True)

# Perfect Fit Table Generator (Width: 1300px)
def make_perfect_fit_table_image():
    w, h = 1300, 1120
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Main Title Box
    draw.rectangle([(20, 15), (1280, 65)], fill="#1e3a8a")
    draw.text((650, 40), "腹部超音波検査 臓器別 全項目 3段階臨床カットオフ判定表", fill="#ffffff", font=font_title, anchor="mm")
    
    # Precise Column Boundaries (Total Width: 1260px)
    # Col 1: 臓器 (110px) -> 20 to 130
    # Col 2: 評価項目 (250px) -> 130 to 380
    # Col 3: 正常基準 (200px) -> 380 to 580
    # Col 4: 要観察・境界 (200px) -> 580 to 780
    # Col 5: 要精査・異常 (200px) -> 780 to 980
    # Col 6: 主な臨床的意義・アクション (300px) -> 980 to 1280
    cols = [
        ("臓器", 20, 130),
        ("評価項目", 130, 380),
        ("正常基準", 380, 580),
        ("要観察・境界", 580, 780),
        ("要精査・異常", 780, 980),
        ("主な臨床的意義・アクション", 980, 1280)
    ]
    
    # Table Header Row
    y = 80
    draw.rectangle([(20, y), (1280, y + 45)], fill="#2563eb")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 45)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 22), name, fill="#ffffff", font=font_large, anchor="mm")
    
    # Data Rows
    data = [
        ("肝臓", "尾状葉/右葉比 (C/RL)", "< 0.55", "0.55 ～ 0.65", "> 0.65", "肝硬変・門脈高血圧症"),
        ("肝臓", "減衰係数 (ATI/UAP)", "< 0.63 dB/cm/MHz", "0.63 ～ 0.72", "> 0.72 (S2/S3)", "脂肪肝 (MASLD) の定量評価"),
        ("肝臓", "剪断波弾性率 (SWE)", "< 6.0 kPa (<1.4m/s)", "6.0 ～ 10.0 kPa", "> 11.0 kPa (F4)", "肝線維化・肝硬変の非侵襲判定"),
        
        ("胆道", "胆嚢壁厚 (前壁)", "≦ 3.0 mm", "3.1 ～ 3.9 mm", "≧ 4.0 mm", "急性胆嚢炎 / 壁肥厚型胆嚢がん"),
        ("胆道", "胆嚢短径", "< 4.0 cm", "4.0 ～ 4.9 cm", "≧ 5.0 cm", "胆嚢腫大 (Hydrops) / 胆管閉塞"),
        ("胆道", "総胆管径 (CBD)", "≦ 6.0 mm (胆摘≦8)", "6.1 ～ 9.9 mm", "≧ 10.0 mm", "胆管結石 / 胆管がん / 閉塞性黄疸"),
        ("胆道", "胆嚢ポリープ径", "< 5.0 mm", "5.0 ～ 9.9 mm", "≧ 10.0 mm", "10mm以上はEUS精査・手術検討"),
        
        ("膵臓", "主膵管径 (MPD体部)", "≦ 2.0 mm", "2.1 ～ 2.9 mm", "≧ 3.0 mm", "膵がん (PDAC) / IPMN / 膵炎"),
        ("膵臓", "膵体部前後径", "< 1.5 cm", "1.5 ～ 1.9 cm", "≧ 2.0 cm", "膵腫大 (AIP / 膵炎 / 腫瘤)"),
        
        ("腎臓", "腎長径 (Long Dia.)", "9.0 ～ 12.0 cm", "8.0 ～ 8.9 cm", "< 8.0 cm (萎縮)", "慢性腎不全 / 水腎症 / 腎腫瘍"),
        ("腎臓", "腎実質厚", "15.0 ～ 20.0 mm", "10.0 ～ 14.9 mm", "< 10.0 mm (Grade4)", "水腎症による腎機能不可逆障害"),
        
        ("脾臓", "脾指数 (Spleen Index)", "< 20.0 cm²", "20.0 ～ 24.9 cm²", "≧ 25.0 cm² (長径≧10)", "脾腫 (門脈高血圧症 / 血液疾患)"),
        
        ("消化管", "虫垂外径 (Outer Dia.)", "≦ 6.0 mm", "6.1 ～ 7.9 mm", "≧ 8.0 mm", "急性虫垂炎 (段階的圧迫非消退)"),
        ("消化管", "腸管壁厚", "≦ 3.0 mm", "3.1 ～ 4.9 mm", "≧ 5.0 mm", "腸炎 / 炎症性腸疾患(IBD) / 癌"),
        
        ("血管", "腹部大動脈径 (AAA)", "< 2.0 cm", "2.0 ～ 2.9 cm", "≧ 3.0 cm (動脈瘤)", "5.0cm以上・嚢状は破裂リスク"),
        ("血管", "門脈幹径 (PV Dia.)", "≦ 12.0 mm", "12.1 ～ 13.0 mm", "≧ 13.1 mm", "門脈高血圧症 (Portal HTN)"),
        ("血管", "門脈血流速度 (Vmax)", "15 ～ 30 cm/s", "10 ～ 14 cm/s", "< 10 cm/s / 逆流", "門脈血流減速・向脾性逆流")
    ]
    
    cur_y = 125
    row_h = 56
    
    for i, (organ, item, norm, bord, abnorm, desc) in enumerate(data):
        bg_color = "#ffffff" if i % 2 == 0 else "#f8fafc"
        draw.rectangle([(20, cur_y), (1280, cur_y + row_h)], fill=bg_color)
        
        # Col 1: Organ
        draw.rectangle([(20, cur_y), (130, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((75, cur_y + row_h // 2), organ, fill="#1e3a8a", font=font_mid, anchor="mm")
        
        # Col 2: Item
        draw.rectangle([(130, cur_y), (380, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((255, cur_y + row_h // 2), item, fill="#0f172a", font=font_mid, anchor="mm")
        
        # Col 3: Normal (Green BG)
        draw.rectangle([(380, cur_y), (580, cur_y + row_h)], fill="#f0fdf4", outline="#cbd5e1", width=1)
        draw.text((480, cur_y + row_h // 2), norm, fill="#166534", font=font_mid, anchor="mm")
        
        # Col 4: Borderline (Yellow BG)
        draw.rectangle([(580, cur_y), (780, cur_y + row_h)], fill="#fefce8", outline="#cbd5e1", width=1)
        draw.text((680, cur_y + row_h // 2), bord, fill="#854d0e", font=font_mid, anchor="mm")
        
        # Col 5: Abnormal (Red BG)
        draw.rectangle([(780, cur_y), (980, cur_y + row_h)], fill="#fef2f2", outline="#cbd5e1", width=1)
        draw.text((880, cur_y + row_h // 2), abnorm, fill="#991b1b", font=font_mid, anchor="mm")
        
        # Col 6: Desc (300px width - zero overflow)
        draw.rectangle([(980, cur_y), (1280, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((1130, cur_y + row_h // 2), desc, fill="#334155", font=font_small, anchor="mm")
        
        cur_y += row_h

    # Outer Border
    draw.rectangle([(20, 80), (1280, cur_y)], outline="#1e3a8a", width=3)

    path = os.path.join(img_dir, "reference_values_table.png")
    img.save(path, quality=95)
    print("Perfect fit table generated successfully!")

make_perfect_fit_table_image()
