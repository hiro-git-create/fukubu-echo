import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 30)
            font_large = ImageFont.truetype(fp, 24)
            font_mid = ImageFont.truetype(fp, 20)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = ImageFont.load_default()

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

# Nutcracker Flowchart Image
def make_nutcracker_flow():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 75)], fill="#0d9488")
    draw.text((550, 45), "ナットクラッカー症候群 (Nutcracker) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw.rectangle([(250, 95), (850, 155)], fill="#ccfbf1", outline="#0d9488", width=3)
    draw.text((550, 125), "若年者の原因不明 無症候性血尿 ＋ 左腰背部痛", fill="#0f766e", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    # Level 2 Container
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#0d9488", width=3)
    draw.text((550, 215), "【 4大超音波所見 ＆ 定量的血流動態カットオフ 】", fill="#0f766e", font=font_large, anchor="mm")
    
    steps = [
        ("1. 左腎静脈 Beak Sign (クチバシサイン)", "SMA-AO間で左腎静脈がクチバシ状に途絶・腎門部側が怒張", "#ccfbf1", "#0f766e"),
        ("2. 左腎静脈 径比 (Dh / De Ratio)", "腎門部太さ (Dh) ÷ SMA下狭窄部太さ (De) ≧ 4.0 ～ 5.0", "#d1fae5", "#047857"),
        ("3. PW血流流速比 (Ve / Vh Ratio)", "狭窄部流速 (Ve) ÷ 腎門部流速 (Vh) ≧ 5.0 (狭窄部流速 > 100cm/s)", "#fef3c7", "#b45309"),
        ("4. 左性腺静脈への逆流 (Reflux Sign)", "左卵巣/精索静脈へ血流逆流 (骨盤うっ血症候群・精索静脈瘤の併発)", "#fee2e2", "#b91c1c")
    ]
    
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
        
    path = os.path.join(img_dir, "nutcracker_flowchart.png")
    img.save(path, quality=95)
    print("Generated nutcracker_flowchart.png successfully!")

make_nutcracker_flow()
