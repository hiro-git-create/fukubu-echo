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

# Perfect Fit Portal HTN Table (Width: 1350px)
def make_perfect_portal_table():
    w, h = 1350, 520
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1330, 65)], fill="#065f46")
    draw.text((675, 40), "門脈高血圧症 (Portal Hypertension) 超音波血流動態評価表", fill="#ffffff", font=font_title, anchor="mm")
    
    # Cols: 臓器項目(250), 正常(280), カットオフ(450), 意義(320) -> Total 1300
    cols = [
        ("評価項目", 25, 275),
        ("正常基準", 275, 555),
        ("門脈高血圧症 診断カットオフ", 555, 1005),
        ("主な臨床的意義", 1005, 1325)
    ]
    
    y = 80
    draw.rectangle([(25, y), (1325, y + 45)], fill="#059669")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 45)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 22), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("脾腫 (Splenomegaly)", "長径 < 10.0 cm\n脾指数(SI) < 20.0 cm²", "長径 ≧ 10.0 cm\n脾指数(SI) ≧ 20.0 cm²", "脾うっ血・血小板減少の指標"),
        ("門脈幹径 (PV Dia.)", "内径 ≦ 12.0 mm", "内径 ≧ 13.0 mm (1.3 cm)", "門脈圧亢進による血管拡張"),
        ("門脈血流速度 (Vmax)", "向肝性 15 ～ 30 cm/s", "減速 (< 15 cm/s)\n向脾性逆流 (Hepatofugal)", "門脈血流の停滞・逆流"),
        ("左胃静脈径 (LGV)", "径 < 4.0 mm", "径 ≧ 5.0 mm", "食道胃静脈瘤ハイリスク"),
        ("臍静脈再開通 (UV)", "完全閉鎖", "肝左葉臍部からの開通血管描出\n(Recanalized UV)", "側副血行路の発達")
    ]
    
    cur_y = 125
    row_h = 72
    for i, (item, norm, abn, desc) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0fdf4"
        draw.rectangle([(25, cur_y), (1325, cur_y + row_h)], fill=bg_c)
        
        # Col 1
        draw.rectangle([(25, cur_y), (275, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((150, cur_y + row_h // 2), item, fill="#065f46", font=font_mid, anchor="mm")
        
        # Col 2
        draw.rectangle([(275, cur_y), (555, cur_y + row_h)], outline="#cbd5e1", width=1)
        n_lines = norm.split('\n')
        if len(n_lines) == 1:
            draw.text((415, cur_y + row_h // 2), norm, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((415, cur_y + 22), n_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((415, cur_y + 50), n_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3
        draw.rectangle([(555, cur_y), (1005, cur_y + row_h)], fill="#fef2f2", outline="#cbd5e1", width=1)
        a_lines = abn.split('\n')
        if len(a_lines) == 1:
            draw.text((780, cur_y + row_h // 2), abn, fill="#991b1b", font=font_mid, anchor="mm")
        else:
            draw.text((780, cur_y + 22), a_lines[0], fill="#991b1b", font=font_mid, anchor="mm")
            draw.text((780, cur_y + 50), a_lines[1], fill="#991b1b", font=font_mid, anchor="mm")
        
        # Col 4
        draw.rectangle([(1005, cur_y), (1325, cur_y + row_h)], outline="#cbd5e1", width=1)
        draw.text((1165, cur_y + row_h // 2), desc, fill="#334155", font=font_small, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(25, 80), (1325, cur_y)], outline="#065f46", width=3)
    path = os.path.join(img_dir, "portal_htn_table.png")
    img.save(path, quality=95)
    print("Perfect Golden Portal HTN Table Generated!")

make_perfect_portal_table()
