import os
from PIL import Image, ImageDraw, ImageFont

# Create high-res image for pancreatic mass classification flowchart
width, height = 900, 780
image = Image.new("RGB", (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

font_large = None
font_mid = None
font_small = None

font_paths = [
    "C:/Windows/Fonts/meiryo.ttc",
    "C:/Windows/Fonts/msgothic.ttc",
    "C:/Windows/Fonts/yuanti.ttf",
    "C:/Windows/Fonts/arial.ttf"
]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_large = ImageFont.truetype(fp, 22)
            font_mid = ImageFont.truetype(fp, 16)
            font_small = ImageFont.truetype(fp, 13)
            break
        except Exception:
            continue

if font_large is None:
    font_large = font_mid = font_small = ImageFont.load_default()

# Background Header
draw.rectangle([(20, 15), (880, 65)], fill="#1e3a8a")
draw.text((450, 40), "膵腫瘤性病変 (Pancreatic Mass Lesions) 完全分類フロー", fill="#ffffff", font=font_large, anchor="mm")

# Level 1: Root
draw.rectangle([(300, 85), (600, 130)], fill="#f1f5f9", outline="#1e3a8a", width=2)
draw.text((450, 107), "膵腫瘤性病変 (Pancreatic Mass)", fill="#1e293b", font=font_mid, anchor="mm")

# Lines to Level 2
draw.line([(450, 130), (450, 150)], fill="#64748b", width=2)
draw.line([(230, 150), (670, 150)], fill="#64748b", width=2)
draw.line([(230, 150), (230, 170)], fill="#64748b", width=2)
draw.line([(670, 150), (670, 170)], fill="#64748b", width=2)

# Level 2 Boxes
draw.rectangle([(60, 170), (400, 215)], fill="#dbeafe", outline="#2563eb", width=2)
draw.text((230, 192), "1. 固形腫瘤性病変 (Solid Lesions)", fill="#1e40af", font=font_mid, anchor="mm")

draw.rectangle([(500, 170), (840, 215)], fill="#fce7f3", outline="#db2777", width=2)
draw.text((670, 192), "2. 嚢胞性腫瘤性病変 (Cystic Lesions)", fill="#9d174d", font=font_mid, anchor="mm")

# Solid Section
draw.rectangle([(40, 235), (420, 755)], fill="#f8fafc", outline="#94a3b8", width=1)
draw.text((230, 260), "【 固形腫瘤 (Solid) 】", fill="#1e3a8a", font=font_mid, anchor="mm")

solid_items = [
    ("通常型膵がん (PDAC)", "浸潤性管がん (全体の約90%)\n低血流 / 主膵管高度拡張 (>3mm)"),
    ("膵神経内分泌腫瘍 (PanNET)", "境界ナイフ様鮮明 / 多血性 (Hyper)\n血流極めて豊富 / 主膵管拡張なし"),
    ("Solid Pseudopapillary (SPN)", "10〜30代若い女性に好発\n固形 ＋ 出血壊死性嚢胞の混在"),
    ("自己免疫性膵炎 (AIP)", "腫瘤形成性膵炎 (膵がん酷似)\nCapsule-like Rim / 主膵管狭小化")
]

y_start = 290
for title, desc in solid_items:
    draw.rectangle([(60, y_start), (400, y_start + 100)], fill="#ffffff", outline="#3b82f6", width=2)
    draw.text((230, y_start + 25), title, fill="#1e3a8a", font=font_mid, anchor="mm")
    draw.text((230, y_start + 65), desc, fill="#475569", font=font_small, anchor="mm")
    y_start += 112

# Cystic Section
draw.rectangle([(480, 235), (860, 755)], fill="#f8fafc", outline="#94a3b8", width=1)
draw.text((670, 260), "【 嚢胞性腫瘤 (Cystic) 】", fill="#831843", font=font_mid, anchor="mm")

cystic_items = [
    ("IPMN (膵管内乳頭粘液性)", "主膵管連通あり / 葡萄の房状\n壁結節 ≧ 5mm で即手術検討"),
    ("MCN (粘液性嚢胞腫瘍)", "中年女性・膵尾部 / 厚い被膜\n潜在的悪性 (原則全例手術)"),
    ("SCN (漿液性嚢胞腫瘍)", "ハニカム像 / 中央星状石灰化\nほぼ100%良性 (経過観察)"),
    ("仮性嚢胞 (Pseudocyst)", "膵炎既往 / 単房性無エコー\n非腫瘍性嚢胞")
]

y_start = 290
for title, desc in cystic_items:
    fill_bg = "#ffffff"
    border_c = "#ec4899" if "IPMN" in title or "MCN" in title or "SCN" in title else "#6b7280"
    draw.rectangle([(500, y_start), (840, y_start + 100)], fill=fill_bg, outline=border_c, width=2)
    draw.text((670, y_start + 25), title, fill="#831843" if border_c != "#6b7280" else "#1f2937", font=font_mid, anchor="mm")
    draw.text((670, y_start + 65), desc, fill="#475569", font=font_small, anchor="mm")
    y_start += 112

# Save Image safely into images directory
target_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(target_dir, exist_ok=True)
img_path = os.path.join(target_dir, "pancreatic_mass_classification.png")
image.save(img_path, quality=95)
print(f"SUCCESS: Flowchart image saved at {img_path}")
