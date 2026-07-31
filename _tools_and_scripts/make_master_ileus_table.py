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

# Master Ileus Table Generator (Width: 1400px, Height: 580px)
def make_master_ileus_table():
    w, h = 1400, 580
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Title Box
    draw.rectangle([(20, 15), (1380, 75)], fill="#1e3a8a")
    draw.text((700, 45), "腸閉塞・イレウス (Ileus) 分類 ＆ 絞扼性 (Strangulation) 緊急鑑別表", fill="#ffffff", font=font_title, anchor="mm")
    
    # Cols: 分類型(280), 腸管拡張(240), 蠕動運動(280), 壁厚血流(300), 対応(260) -> Total 1360
    cols = [
        ("分類型", 20, 300),
        ("腸管拡張・径", 300, 540),
        ("蠕動運動 (Peristalsis)", 540, 820),
        ("壁厚・壁血流", 820, 1120),
        ("緊急性と対応", 1120, 1380)
    ]
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#2563eb")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("単純性機械的イレウス", "小腸 > 2.5 ～ 3.0 cm", "著明亢進\n(To-and-fro 往復運動)", "壁厚正常\n血流信号良好", "減圧保存的治療\n待機手術検討", "#ffffff"),
        ("麻痺性イレウス\n(Paralytic)", "小腸・大腸\n全域拡張", "完全消失・麻痺・静止", "壁厚正常\n血流保たれる", "保存的治療\n(絶食・輸液・消炎)", "#f8fafc"),
        ("絞扼性イレウス\n(Strangulated)", "虚脱腸管 ＋\n局所拡張腸管", "静止・消失", "壁肥厚 (> 3mm) ＋\n★ 壁血流完全消失", "★ 超緊急外科手術\n(腸管壊死・切除)", "#fee2e2")
    ]
    
    cur_y = 145
    row_h = 135
    for i, (ctype, dia, peri, wall, act, bg_c) in enumerate(data):
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        # Col 1: Type (280px)
        draw.rectangle([(20, cur_y), (300, cur_y + row_h)], outline="#cbd5e1", width=2)
        c_lines = ctype.split('\n')
        t_color = "#991b1b" if bg_c == "#fee2e2" else "#1e3a8a"
        if len(c_lines) == 1:
            draw.text((160, cur_y + row_h // 2), ctype, fill=t_color, font=font_large, anchor="mm")
        else:
            draw.text((160, cur_y + 45), c_lines[0], fill=t_color, font=font_large, anchor="mm")
            draw.text((160, cur_y + 90), c_lines[1], fill=t_color, font=font_mid, anchor="mm")
        
        # Col 2: Dia
        draw.rectangle([(300, cur_y), (540, cur_y + row_h)], outline="#cbd5e1", width=2)
        d_lines = dia.split('\n')
        if len(d_lines) == 1:
            draw.text((420, cur_y + row_h // 2), dia, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((420, cur_y + 45), d_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((420, cur_y + 90), d_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3: Peri
        draw.rectangle([(540, cur_y), (820, cur_y + row_h)], outline="#cbd5e1", width=2)
        p_lines = peri.split('\n')
        if len(p_lines) == 1:
            draw.text((680, cur_y + row_h // 2), peri, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((680, cur_y + 45), p_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((680, cur_y + 90), p_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 4: Wall
        draw.rectangle([(820, cur_y), (1120, cur_y + row_h)], outline="#cbd5e1", width=2)
        w_lines = wall.split('\n')
        if len(w_lines) == 1:
            draw.text((970, cur_y + row_h // 2), wall, fill="#991b1b" if "消失" in wall else "#334155", font=font_mid, anchor="mm")
        else:
            draw.text((970, cur_y + 45), w_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((970, cur_y + 90), w_lines[1], fill="#991b1b" if "消失" in wall else "#334155", font=font_mid, anchor="mm")
        
        # Col 5: Act
        draw.rectangle([(1120, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        a_lines = act.split('\n')
        a_color = "#991b1b" if bg_c == "#fee2e2" else "#1e293b"
        if len(a_lines) == 1:
            draw.text((1250, cur_y + row_h // 2), act, fill=a_color, font=font_mid, anchor="mm")
        else:
            draw.text((1250, cur_y + 45), a_lines[0], fill=a_color, font=font_large if bg_c == "#fee2e2" else font_mid, anchor="mm")
            draw.text((1250, cur_y + 90), a_lines[1], fill=a_color, font=font_mid, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#1e3a8a", width=3)
    path = os.path.join(img_dir, "ileus_classification_table.png")
    img.save(path, quality=95)
    print("Master perfect ileus_classification_table.png generated successfully!")

make_master_ileus_table()
