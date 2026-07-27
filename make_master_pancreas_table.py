import os
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

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"

# Master Pancreatic Solid Tumors Table Generator
def make_master_pancreas_solid_table():
    w, h = 1400, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Title Box
    draw.rectangle([(20, 15), (1380, 75)], fill="#581c87")
    draw.text((700, 45), "固形膵腫瘍 (Solid Pancreatic Lesions) 4大疾患 比較鑑別表", fill="#ffffff", font=font_title, anchor="mm")
    
    # Cols: 疾患名(300), Bモード(320), 主膵管(260), カラードプラ(300), 患者層(180) -> Total 1360
    cols = [
        ("疾患名", 20, 320),
        ("Bモード像・輪郭特徴", 320, 640),
        ("主膵管 (MPD) の変化", 640, 900),
        ("カラードプラ / 造影所見", 900, 1200),
        ("好発患者層", 1200, 1380)
    ]
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#7e22ce")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("通常型膵がん\n(PDAC)", "境界不鮮明・不整型\n内部低エコー", "高度拡張 (>3mm)\n描出途絶", "低血流 (Hypovascular)\nKupffer相濃染なし", "高齢男女\n(60～80代)"),
        ("膵神経内分泌腫瘍\n(PanNET)", "境界極めて鮮明\n円形～楕円形・均一低エコー", "拡張を伴いにくい\n(MPD非拡張)", "著明な多血性 (Hyper)\n早期濃染パターン", "中高齢男女\n(50～70代)"),
        ("SPN (Solid Pseudo-)\n(擬乳頭状腫瘍)", "境界鮮明・固形部と\n壊死性嚢胞の混在像", "主膵管拡張なし", "固形部に血流信号あり\n変性・嚢胞化伴う", "若年女性★\n(10～30代)"),
        ("自己免疫性膵炎\n(Type 1 AIP)", "びまん性びん詰大\n(ソーセージ様腫大)", "主膵管のびまん性狭小化\n(Duct Narrowing)", "早期均一濃染\nCapsule-like Rim", "高齢男性★\n(60代以上)")
    ]
    
    cur_y = 145
    row_h = 125
    for i, (dis, bmode, mpd, dopp, pts) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#faf5ff"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        # Col 1: Disease
        draw.rectangle([(20, cur_y), (320, cur_y + row_h)], outline="#cbd5e1", width=2)
        d_lines = dis.split('\n')
        if len(d_lines) == 1:
            draw.text((170, cur_y + row_h // 2), dis, fill="#581c87", font=font_large, anchor="mm")
        else:
            draw.text((170, cur_y + 40), d_lines[0], fill="#581c87", font=font_large, anchor="mm")
            draw.text((170, cur_y + 85), d_lines[1], fill="#581c87", font=font_mid, anchor="mm")
        
        # Col 2: Bmode
        draw.rectangle([(320, cur_y), (640, cur_y + row_h)], outline="#cbd5e1", width=2)
        b_lines = bmode.split('\n')
        if len(b_lines) == 1:
            draw.text((480, cur_y + row_h // 2), bmode, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((480, cur_y + 40), b_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((480, cur_y + 85), b_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3: MPD
        draw.rectangle([(640, cur_y), (900, cur_y + row_h)], outline="#cbd5e1", width=2)
        m_lines = mpd.split('\n')
        if len(m_lines) == 1:
            draw.text((770, cur_y + row_h // 2), mpd, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((770, cur_y + 40), m_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((770, cur_y + 85), m_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 4: Doppler
        draw.rectangle([(900, cur_y), (1200, cur_y + row_h)], outline="#cbd5e1", width=2)
        p_lines = dopp.split('\n')
        if len(p_lines) == 1:
            draw.text((1050, cur_y + row_h // 2), dopp, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((1050, cur_y + 40), p_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((1050, cur_y + 85), p_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 5: Pts
        draw.rectangle([(1200, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        pt_lines = pts.split('\n')
        if len(pt_lines) == 1:
            draw.text((1290, cur_y + row_h // 2), pts, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((1290, cur_y + 40), pt_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((1290, cur_y + 85), pt_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#581c87", width=3)
    path = os.path.join(img_dir, "pancreatic_solid_tumors_table.png")
    img.save(path, quality=95)
    print("Master pancreatic_solid_tumors_table.png generated successfully!")

make_master_pancreas_solid_table()
