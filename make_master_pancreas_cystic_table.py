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

# Master Pancreatic Cystic Tumors Table Generator
def make_master_pancreas_cystic_table():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Title Box
    draw.rectangle([(20, 15), (1380, 75)], fill="#0284c7")
    draw.text((700, 45), "膵嚢胞性腫瘍 3大疾患 (IPMN / MCN / SCN) 比較鑑別マトリックス", fill="#ffffff", font=font_title, anchor="mm")
    
    # Cols: 評価項目(280), IPMN(360), MCN(360), SCN(360) -> Total 1360
    cols = [
        ("評価項目", 20, 300),
        ("IPMN (管内乳頭粘液性)", 300, 660),
        ("MCN (粘液性嚢胞腫瘍)", 660, 1020),
        ("SCN (漿液性嚢胞腫瘍)", 1020, 1380)
    ]
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#0369a1")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("内部形態・エコー所見", "葡萄の房状多房性嚢胞\n(Bunch of grapes)", "大円形多房性嚢胞\n(Orange-like / 蜜柑状)", "ハニカム構造 (Honeycomb)\n微小多房性嚢胞群"),
        ("主膵管 (MPD) 連通", "あり ★\n(Communication (+))", "なし\n(Communication (-))", "なし\n(Communication (-))"),
        ("特徴的画像所見", "粘液排出による\nファーター壺腹部開口部拡張", "厚い包膜 ＋ 卵殻状石灰化\n(Ovarian-like stroma)", "中央星状石灰化 ★\n(Central Stellate Scar)"),
        ("好発性別・年齢・部位", "高齢男性・女性\n(男女同等)", "ほぼ100% 30～50代女性 ★\n(膵体尾部に好発)", "60代以上 女性に多い\n(全域に発生)"),
        ("悪性度・治療方針", "壁結節 ≧ 5mm で悪性疑い\n(High-risk stigmata)", "潜在的悪性 (全例切除検討)\n(Mucinous Cystic)", "ほぼ100% 良性 (経過観察)\n(Serous Cystic)")
    ]
    
    cur_y = 145
    row_h = 135
    for i, (item, ipmn, mcn, scn) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0f9ff"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        # Col 1: Item
        draw.rectangle([(20, cur_y), (300, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((160, cur_y + row_h // 2), item, fill="#0369a1", font=font_large, anchor="mm")
        
        # Col 2: IPMN
        draw.rectangle([(300, cur_y), (660, cur_y + row_h)], outline="#cbd5e1", width=2)
        ip_lines = ipmn.split('\n')
        if len(ip_lines) == 1:
            draw.text((480, cur_y + row_h // 2), ipmn, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((480, cur_y + 45), ip_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((480, cur_y + 90), ip_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3: MCN
        draw.rectangle([(660, cur_y), (1020, cur_y + row_h)], outline="#cbd5e1", width=2)
        m_lines = mcn.split('\n')
        if len(m_lines) == 1:
            draw.text((840, cur_y + row_h // 2), mcn, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((840, cur_y + 45), m_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((840, cur_y + 90), m_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 4: SCN
        draw.rectangle([(1020, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        s_lines = scn.split('\n')
        if len(s_lines) == 1:
            draw.text((1200, cur_y + row_h // 2), scn, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((1200, cur_y + 45), s_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((1200, cur_y + 90), s_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#0284c7", width=3)
    path = os.path.join(img_dir, "pancreatic_cystic_tumors_table.png")
    img.save(path, quality=95)
    print("Master pancreatic_cystic_tumors_table.png generated successfully!")

make_master_pancreas_cystic_table()
