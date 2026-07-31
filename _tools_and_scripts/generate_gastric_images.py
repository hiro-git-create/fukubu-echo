import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 30)
            font_large = ImageFont.truetype(fp, 24)
            font_mid = ImageFont.truetype(fp, 21)
            font_small = ImageFont.truetype(fp, 18)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"

def draw_two_line_box(draw, box, fill_bg, outline_c, title, desc_text, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    t_c = title_color if title_color else outline_c
    cx = (x1 + x2) // 2
    draw.text((cx, y1 + 30), title, fill=t_c, font=font_large, anchor="mm")
    draw.text((cx, y1 + 72), desc_text, fill="#1e293b", font=font_mid, anchor="mm")

# 1. Gastric Tumors Flowchart & Matrix Table
def make_gastric_tumors_images():
    # Flowchart
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#0284c7")
    draw.text((550, 45), "胃がん ＆ 胃粘膜下腫瘍 (GIST/SMT) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#e0f2fe", outline="#0284c7", width=3)
    draw.text((550, 125), "上腹部痛・心みぞおち違和感・水飲み法走査", fill="#0369a1", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#0284c7", width=3)
    draw.text((550, 215), "【 胃壁5層構造 ＆ 発生層の判定 】", fill="#0369a1", font=font_large, anchor="mm")
    
    steps = [
        ("1. 胃壁5層構造の破壊・層断裂あり", "進行胃がん (T2～T4): 著明な非対称性壁肥厚 ＋ 5層構造完全消失", "#fee2e2", "#991b1b"),
        ("2. 5層構造保持 ＋ 第1～3層の局所肥厚", "早期胃がん (T1): 粘膜～粘膜下層にとどまる局所低エコー肥厚", "#ffedd5", "#c2410c"),
        ("3. 正常粘膜被覆 ＋ 第4層 (固有筋層) 突出", "胃GIST / SMT: 境界鮮明な低エコー腫瘤 (3cm超は中心壊死伴う)", "#dbeafe", "#1e40af"),
        ("4. 造影超音波 (CEUS: Sonazoid) 濃染相", "GISTは早期多血性濃染 / 進行胃がんは低血流～欠損パターン", "#dcfce7", "#15803d")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "gastric_tumors_flowchart.png"), quality=95)

    # Matrix Table
    w, h = 1400, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1380, 75)], fill="#0284c7")
    draw.text((700, 45), "胃がん vs 胃GIST / 粘膜下腫瘍 (SMT) 比較鑑別マトリックス", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [("評価項目", 20, 300), ("進行胃がん (Gastric Cancer)", 300, 660), ("胃GIST / SMT (粘膜下腫瘍)", 660, 1020), ("超音波診断のポイント", 1020, 1380)]
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#0369a1")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("発生主座・層構造", "第1～5層 全層断裂破壊\n(全層性病変)", "第4層 (固有筋層) 由来 ★\n(上層粘膜は正常被覆)", "層断裂の有無が最重要判定"),
        ("腫瘤形態・輪郭", "境界不鮮明・不整型\n全周性または偏平壁肥厚", "境界極めて鮮明・球形～楕円形\n腔内/壁外突出型", "GISTは滑らかな輪郭を呈する"),
        ("内部エコー・壊死", "不均一低エコー\n潰瘍形成 (Target Sign)", "均一低エコー\n(3cm超で中心壊死・無エコー)", "大型GISTは中心壊死を伴う"),
        ("血流・CEUS濃染", "低血流 (Hypovascular)\nKupffer相欠損", "著明な多血性 (Hyper)\n早期強濃染パターン", "GISTは豊かな血管網を有する")
    ]
    cur_y = 145
    row_h = 125
    for i, (item, gc, gist, pnt) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0f9ff"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        draw.rectangle([(20, cur_y), (300, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((160, cur_y + row_h // 2), item, fill="#0369a1", font=font_large, anchor="mm")
        
        draw.rectangle([(300, cur_y), (660, cur_y + row_h)], outline="#cbd5e1", width=2)
        g_lines = gc.split('\n')
        draw.text((480, cur_y + 40), g_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((480, cur_y + 85), g_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(660, cur_y), (1020, cur_y + row_h)], outline="#cbd5e1", width=2)
        gt_lines = gist.split('\n')
        draw.text((840, cur_y + 40), gt_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((840, cur_y + 85), gt_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(1020, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((1200, cur_y + row_h // 2), pnt, fill="#334155", font=font_mid, anchor="mm")
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#0284c7", width=3)
    img.save(os.path.join(img_dir, "gastric_tumors_matrix_table.png"), quality=95)
    print("Generated Gastric Tumors PNG Images!")

make_gastric_tumors_images()
