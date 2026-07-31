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

# Perfect Master Table Generator
def make_master_portal_table():
    w, h = 1400, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Title Box
    draw.rectangle([(20, 15), (1380, 75)], fill="#065f46")
    draw.text((700, 45), "門脈高血圧症 (Portal Hypertension) 超音波血流動態評価表", fill="#ffffff", font=font_title, anchor="mm")
    
    # Precise Columns with Generous Padding (Total Width: 1360px)
    # Col 1: 評価項目 (300px) -> 20 to 320
    # Col 2: 正常基準 (300px) -> 320 to 620
    # Col 3: 門脈高血圧症 診断カットオフ (440px) -> 620 to 1060
    # Col 4: 主な臨床的意義 (320px) -> 1060 to 1380
    cols = [
        ("評価項目", 20, 320),
        ("正常基準", 320, 620),
        ("門脈高血圧症 診断カットオフ", 620, 1060),
        ("主な臨床的意義", 1060, 1380)
    ]
    
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#059669")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("脾腫 (Splenomegaly)", "長径 < 10.0 cm\n脾指数(SI) < 20.0 cm²", "長径 ≧ 10.0 cm\n脾指数(SI) ≧ 20.0 cm²", "脾うっ血・血小板減少"),
        ("門脈幹径 (PV Dia.)", "内径 ≦ 12.0 mm", "内径 ≧ 13.0 mm (1.3 cm)", "門脈圧亢進・血管拡張"),
        ("門脈血流速度 (Vmax)", "向肝性 15 ～ 30 cm/s", "減速 (< 15 cm/s)\n向脾性逆流 (Hepatofugal)", "門脈血流の停滞・逆流"),
        ("左胃静脈径 (LGV)", "径 < 4.0 mm", "径 ≧ 5.0 mm", "食道胃静脈瘤ハイリスク"),
        ("臍静脈再開通 (UV)", "完全閉鎖", "肝左葉臍部からの開通血管描出\n(Recanalized UV)", "側副血行路の発達")
    ]
    
    cur_y = 145
    row_h = 105
    for i, (item, norm, abn, desc) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0fdf4"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        
        # Col 1: 評価項目 (Spacious 300px width)
        draw.rectangle([(20, cur_y), (320, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((170, cur_y + row_h // 2), item, fill="#065f46", font=font_large, anchor="mm")
        
        # Col 2: 正常基準
        draw.rectangle([(320, cur_y), (620, cur_y + row_h)], outline="#cbd5e1", width=2)
        n_lines = norm.split('\n')
        if len(n_lines) == 1:
            draw.text((470, cur_y + row_h // 2), norm, fill="#334155", font=font_mid, anchor="mm")
        else:
            draw.text((470, cur_y + 32), n_lines[0], fill="#334155", font=font_mid, anchor="mm")
            draw.text((470, cur_y + 72), n_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        # Col 3: カットオフ (Red BG)
        draw.rectangle([(620, cur_y), (1060, cur_y + row_h)], fill="#fef2f2", outline="#cbd5e1", width=2)
        a_lines = abn.split('\n')
        if len(a_lines) == 1:
            draw.text((840, cur_y + row_h // 2), abn, fill="#991b1b", font=font_large, anchor="mm")
        else:
            draw.text((840, cur_y + 32), a_lines[0], fill="#991b1b", font=font_large, anchor="mm")
            draw.text((840, cur_y + 72), a_lines[1], fill="#991b1b", font=font_large, anchor="mm")
        
        # Col 4: 意義 (Uniform Large Font font_mid!)
        draw.rectangle([(1060, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((1220, cur_y + row_h // 2), desc, fill="#334155", font=font_mid, anchor="mm")
        
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#065f46", width=3)
    path = os.path.join(img_dir, "portal_htn_table.png")
    img.save(path, quality=95)
    print("Master perfect portal_htn_table.png generated!")

make_master_portal_table()
