import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 28)
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

# 1. Fatty Liver Flowchart (Large Text)
def make_fatty_flow():
    w, h = 1000, 750
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (980, 75)], fill="#15803d")
    draw.text((500, 45), "脂肪肝 (Fatty Liver / MASLD) 重症度・局所性変化 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (750, 150)], fill="#f0fdf4", outline="#15803d", width=3)
    draw.text((500, 122), "上腹部走査: 肝腎長軸像 ＆ 右肋骨下斜断像", fill="#14532d", font=font_large, anchor="mm")
    
    draw.line([(500, 150), (500, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(100, 185), (900, 275)], fill="#f8fafc", outline="#16a34a", width=3)
    draw.text((500, 212), "【 4大サイン ＆ 減衰係数 ATI / UAP の評価 】", fill="#15803d", font=font_large, anchor="mm")
    draw.text((500, 248), "1. 肝腎コントラスト | 2. 深部減衰 | 3. 門脈壁消退 | 4. ATI > 0.63 dB/cm/MHz", fill="#1e293b", font=font_mid, anchor="mm")
    
    draw.line([(500, 275), (500, 310)], fill="#64748b", width=3)
    draw.line([(280, 310), (720, 310)], fill="#64748b", width=3)
    draw.line([(280, 310), (280, 340)], fill="#64748b", width=3)
    draw.line([(720, 310), (720, 340)], fill="#64748b", width=3)
    
    # Left: Severity Grades
    draw.rectangle([(40, 340), (480, 710)], fill="#ffffff", outline="#16a34a", width=3)
    draw.text((260, 370), "【 全般性脂肪肝 Grade 分類 】", fill="#15803d", font=font_large, anchor="mm")
    draw.text((260, 520), "・Grade 1 (軽度): 肝腎コントラスト軽度陽性\n・Grade 2 (中等度): 深部減衰・門脈壁不鮮明\n・Grade 3 (高度): 肝深部・横隔膜描出不能\n★ SWE線維化評価: F4(肝硬変) > 11 kPa", fill="#1e293b", font=font_mid, anchor="mm")
    
    # Right: Focal Sparing
    draw.rectangle([(520, 340), (960, 710)], fill="#ffffff", outline="#eab308", width=3)
    draw.text((740, 370), "【 局所性脂肪回避 (Focal Sparing) 】", fill="#a16207", font=font_large, anchor="mm")
    draw.text((740, 520), "・好発部位: 胆嚢床(S5) / 門脈臍部(S4)\n・非門脈系第三の血流流入による\n★ 腫瘍(Mass)との鑑別:\n   血管が病変内を直進貫通 (Mass effect無)", fill="#1e293b", font=font_mid, anchor="mm")
    
    path = os.path.join(img_dir, "liver_fatty_flowchart.png")
    img.save(path, quality=95)
    print("Saved liver_fatty_flowchart.png")

# 2. Appendicitis Flowchart (Large Text)
def make_app_flow():
    w, h = 1000, 750
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (980, 75)], fill="#c2410c")
    draw.text((500, 45), "急性虫垂炎 (Acute Appendicitis) 超音波診断・期別フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (750, 150)], fill="#fff7ed", outline="#c2410c", width=3)
    draw.text((500, 122), "右下腹部 段階的圧迫走査 (Graded Compression)", fill="#9a3412", font=font_large, anchor="mm")
    
    draw.line([(500, 150), (500, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(100, 185), (900, 275)], fill="#f8fafc", outline="#ea580c", width=3)
    draw.text((500, 212), "【 虫垂の描出 ＆ 圧迫消退性の確認 】", fill="#c2410c", font=font_large, anchor="mm")
    draw.text((500, 248), "1. 虫垂外径 > 6.0 mm | 2. 圧迫非消退 (丸いまま) | 3. Sonographic McBurney 陽性", fill="#1e293b", font=font_mid, anchor="mm")
    
    draw.line([(500, 275), (500, 310)], fill="#64748b", width=3)
    
    # 3 Pathological Stages
    draw.rectangle([(40, 310), (960, 710)], fill="#ffffff", outline="#c2410c", width=3)
    draw.text((500, 340), "【 病理病態期別の観察基準 】", fill="#9a3412", font=font_large, anchor="mm")
    
    stages = [
        ("カタル性 (Catarrhal)", "外径 6-8mm / 5層構造完全保持 / 軽度血流増加", "#ffedd5", "#9a3412"),
        ("蜂窩織炎性 (Phlegmonous)", "外径 8-12mm / 粘膜下層肥厚 / ★ 著明な壁内血流増加 (Hyperemia)", "#fed7aa", "#9a3412"),
        ("壊疽性 (Gangrenous)", "外径 > 10mm / 壁層構造断裂 / ★ 壁内血流の完全消失 (無血流/壊死)", "#fee2e2", "#991b1b")
    ]
    
    y = 380
    for title, desc, bg_c, text_c in stages:
        draw.rectangle([(60, y), (940, y + 95)], fill=bg_c, outline=text_c, width=2)
        draw.text((230, y + 47), title, fill=text_c, font=font_large, anchor="mm")
        draw.text((610, y + 47), desc, fill="#1e293b" if text_c != "#991b1b" else "#7f1d1d", font=font_mid, anchor="mm")
        y += 105
        
    path = os.path.join(img_dir, "appendicitis_flowchart.png")
    img.save(path, quality=95)
    print("Saved appendicitis_flowchart.png")

make_fatty_flow()
make_app_flow()
