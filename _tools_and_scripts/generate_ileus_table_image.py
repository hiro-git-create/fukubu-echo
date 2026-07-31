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
os.makedirs(img_dir, exist_ok=True)

# 1. Ileus Classification Table Image
def make_ileus_table():
    w, h = 1200, 360
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1180, 65)], fill="#1e3a8a")
    draw.text((600, 40), "腸閉塞・イレウス (Ileus) 分類 ＆ 絞扼性 (Strangulation) 緊急鑑別表", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [
        ("分類型", 20, 240),
        ("腸管拡張・径", 240, 440),
        ("蠕動運動 (Peristalsis)", 440, 700),
        ("壁厚・壁血流 (Color Doppler)", 700, 960),
        ("緊急性と対応", 960, 1180)
    ]
    
    y = 80
    draw.rectangle([(20, y), (1180, y + 45)], fill="#2563eb")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 45)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 22), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("単純性機械的イレウス", "小腸 > 2.5 ～ 3.0 cm", "著明亢進 (To-and-fro 往復運動)", "壁厚正常, 血流信号良好", "減圧保存的治療 / 待機手術", "#ffffff"),
        ("麻痺性イレウス (Paralytic)", "小腸・大腸 全域拡張", "完全消失・麻痺・静止", "壁厚正常, 血流保たれる", "保存的治療 (絶食・輸液)", "#f8fafc"),
        ("絞扼性イレウス (Strangulated)", "虚脱腸管 ＋ 局所拡張腸管", "静止・消失", "壁肥厚(>3mm) ＋ ★壁血流完全消失", "★ 超緊急外科手術 (腸管壊死)", "#fee2e2")
    ]
    
    cur_y = 125
    row_h = 70
    for i, (ctype, dia, peri, wall, act, bg_c) in enumerate(data):
        draw.rectangle([(20, cur_y), (1180, cur_y + row_h)], fill=bg_c)
        
        # Col 1: Type
        draw.rectangle([(20, cur_y), (240, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((130, cur_y + row_h // 2), ctype, fill="#1e3a8a" if bg_c != "#fee2e2" else "#991b1b", font=font_large if bg_c == "#fee2e2" else font_mid, anchor="mm")
        
        # Col 2: Dia
        draw.rectangle([(240, cur_y), (440, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((340, cur_y + row_h // 2), dia, fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3: Peri
        draw.rectangle([(440, cur_y), (700, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((570, cur_y + row_h // 2), peri, fill="#334155", font=font_mid, anchor="mm")
        
        # Col 4: Wall
        draw.rectangle([(700, cur_y), (960, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((830, cur_y + row_h // 2), wall, fill="#991b1b" if "消失" in wall else "#334155", font=font_mid, anchor="mm")
        
        # Col 5: Act
        draw.rectangle([(960, cur_y), (1180, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((1070, cur_y + row_h // 2), act, fill="#991b1b" if bg_c == "#fee2e2" else "#1e293b", font=font_large if bg_c == "#fee2e2" else font_mid, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(20, 80), (1180, cur_y)], outline="#1e3a8a", width=3)
    path = os.path.join(img_dir, "ileus_classification_table.png")
    img.save(path, quality=95)
    print("Generated ileus_classification_table.png successfully!")

make_ileus_table()
