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
            font_small = ImageFont.truetype(fp, 17)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

# Helper function
def draw_two_line_box(draw, box, fill_bg, outline_c, title, desc_text, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    t_c = title_color if title_color else outline_c
    cx = (x1 + x2) // 2
    draw.text((cx, y1 + 30), title, fill=t_c, font=font_large, anchor="mm")
    draw.text((cx, y1 + 72), desc_text, fill="#1e293b", font=font_mid, anchor="mm")

# SMA Syndrome Flowchart Image
def make_sma_flow():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 75)], fill="#0284c7")
    draw.text((550, 45), "SMA症候群 (上腸間膜動脈症候群) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(250, 95), (850, 155)], fill="#e0f2fe", outline="#0284c7", width=3)
    draw.text((550, 125), "消瘦・痩せ ＋ 食後膨満感・胆汁性嘔吐", fill="#0369a1", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    # Level 2 Container
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#0284c7", width=3)
    draw.text((550, 215), "【 3大定量的カットオフ ＆ 体位動態観察サイン 】", fill="#0369a1", font=font_large, anchor="mm")
    
    steps = [
        ("1. AO-SMA 分岐角 (SMA Angle)", "角度 < 20° 〜 22° (正常 45°〜60°) に高度鋭角化", "#e0f2fe", "#0369a1"),
        ("2. AO-SMA 血管間距離 (Aorta-SMA Distance)", "距離 < 8.0 mm (特に < 5.0 mm) に挟み込み狭小化", "#dbeafe", "#1e40af"),
        ("3. 十二指腸水平部拡張 ＆ To-and-fro運動", "口側十二指腸径 > 20mm ＋ 内容物の強烈な往復逆流運動", "#fef3c7", "#b45309"),
        ("4. 体位変換解除試験 (Prone Relief Test)", "うつ伏せ / 左側臥位でSMAが前方へ下がり、閉塞が即座に開通・通液", "#dcfce7", "#15803d")
    ]
    
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
        
    path = os.path.join(img_dir, "sma_syndrome_flowchart.png")
    img.save(path, quality=95)
    print("Generated sma_syndrome_flowchart.png successfully!")

make_sma_flow()
