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

# Helper function for perfectly centered two-line boxes (Zero overlap)
def draw_two_line_box(draw, box, fill_bg, outline_c, title, desc_text, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    t_c = title_color if title_color else outline_c
    cx = (x1 + x2) // 2
    
    if not desc_text:
        draw.text((cx, (y1 + y2) // 2), title, fill=t_c, font=font_large, anchor="mm")
    else:
        draw.text((cx, y1 + 30), title, fill=t_c, font=font_large, anchor="mm")
        draw.text((cx, y1 + 72), desc_text, fill="#1e293b", font=font_mid, anchor="mm")

# 1. Appendicitis Flowchart (Perfect Fit Fix)
def make_app_flow_fixed():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 75)], fill="#c2410c")
    draw.text((550, 45), "急性虫垂炎 (Acute Appendicitis) 超音波診断・期別フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root (Height: 60px)
    draw_two_line_box(draw, (250, 95, 850, 155), "#fff7ed", "#c2410c", "右下腹部 段階的圧迫走査 (Graded Compression)", "", title_color="#9a3412")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    # Level 2 Signature Box (Height: 100px)
    draw_two_line_box(draw, (80, 185, 1020, 285), "#f8fafc", "#ea580c", "【 虫垂の描出 ＆ 圧迫消退性の確認 】", "1. 虫垂外径 > 6.0 mm  |  2. 圧迫非消退 (丸い断面のまま)  |  3. Sonographic McBurney 陽性", title_color="#c2410c")
    
    draw.line([(550, 285), (550, 315)], fill="#64748b", width=3)
    
    # Level 3 Container (Height: 450px)
    draw.rectangle([(30, 315), (1070, 765)], fill="#ffffff", outline="#c2410c", width=3)
    draw.text((550, 345), "【 病理病態期別の観察基準 】", fill="#9a3412", font=font_large, anchor="mm")
    
    stages = [
        ("カタル性 (Catarrhal)", "外径 6-8mm / 5層構造完全保持 / 軽度血流増加", "#ffedd5", "#9a3412"),
        ("蜂窩織炎性 (Phlegmonous)", "外径 8-12mm / 粘膜下層肥厚 / ★ 著明な壁内血流増加 (Hyperemia)", "#fed7aa", "#9a3412"),
        ("壊疽性 (Gangrenous)", "外径 > 10mm / 壁層構造断裂 / ★ 壁内血流の完全消失 (無血流/壊死)", "#fee2e2", "#991b1b")
    ]
    
    y = 380
    for title, desc, bg_c, text_c in stages:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
        
    path = os.path.join(img_dir, "appendicitis_flowchart.png")
    img.save(path, quality=95)
    print("Fixed Appendicitis Flowchart: appendicitis_flowchart.png generated successfully!")

make_app_flow_fixed()
