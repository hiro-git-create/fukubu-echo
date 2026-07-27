import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 26)
            font_large = ImageFont.truetype(fp, 22)
            font_mid = ImageFont.truetype(fp, 18)
            font_small = ImageFont.truetype(fp, 16)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

# Helper to draw multiline centered text inside a box perfectly
def draw_textbox(draw, box, fill_bg, outline_c, title, desc_lines, is_header=False):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    
    # Title
    t_y = y1 + 25 if desc_lines else (y1 + y2) // 2
    draw.text(((x1 + x2) // 2, t_y), title, fill=outline_c if not is_header else "#ffffff", font=font_large, anchor="mm")
    
    # Desc lines
    if desc_lines:
        line_y = y1 + 55
        for line in desc_lines:
            draw.text(((x1 + x2) // 2, line_y), line, fill="#1e293b", font=font_mid, anchor="mm")
            line_y += 26

# 1. Pancreatic Mass (Perfect Fit)
def make_panc_mass_fit():
    w, h = 1100, 1000
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (1080, 75)], fill="#1e3a8a")
    draw.text((550, 45), "膵腫瘤性病変 (Pancreatic Mass) 完全分類フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    # Root
    draw.rectangle([(330, 95), (770, 155)], fill="#f1f5f9", outline="#1e3a8a", width=3)
    draw.text((550, 125), "膵腫瘤性病変 (Pancreatic Mass)", fill="#1e293b", font=font_large, anchor="mm")
    
    # Lines
    draw.line([(550, 155), (550, 180)], fill="#64748b", width=3)
    draw.line([(280, 180), (820, 180)], fill="#64748b", width=3)
    draw.line([(280, 180), (280, 205)], fill="#64748b", width=3)
    draw.line([(820, 180), (820, 205)], fill="#64748b", width=3)
    
    # Category Headers
    draw.rectangle([(50, 205), (510, 265)], fill="#dbeafe", outline="#2563eb", width=3)
    draw.text((280, 235), "1. 固形腫瘤性病変 (Solid)", fill="#1e40af", font=font_large, anchor="mm")

    draw.rectangle([(590, 205), (1050, 265)], fill="#fce7f3", outline="#db2777", width=3)
    draw.text((820, 235), "2. 嚢胞性腫瘤性病変 (Cystic)", fill="#9d174d", font=font_large, anchor="mm")

    # Left Solid Section
    draw.rectangle([(30, 285), (530, 970)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((280, 315), "【 固形腫瘤 (Solid Lesions) 】", fill="#1e3a8a", font=font_large, anchor="mm")

    solid_items = [
        ("通常型膵がん (PDAC)", ["浸潤性管がん (全体の約90%)", "低血流 / 主膵管高度拡張 (>3mm)"]),
        ("膵神経内分泌腫瘍 (PanNET)", ["境界ナイフ様鮮明 / 多血性(Hyper)", "血流極めて豊富 / 主膵管拡張なし"]),
        ("Solid Pseudopapillary (SPN)", ["10〜30代若い女性に好発", "固形 ＋ 出血壊死性嚢胞の混在"]),
        ("自己免疫性膵炎 (AIP)", ["腫瘤形成性膵炎 (膵がん酷似)", "Capsule-like Rim / 主膵管狭小化"])
    ]

    y_start = 350
    for title, lines in solid_items:
        draw_textbox(draw, (50, y_start, 510, y_start + 135), "#ffffff", "#3b82f6", title, lines)
        y_start += 150

    # Right Cystic Section
    draw.rectangle([(570, 285), (1070, 970)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((820, 315), "【 嚢胞性腫瘤 (Cystic Lesions) 】", fill="#831843", font=font_large, anchor="mm")

    cystic_items = [
        ("IPMN (膵管内乳頭粘液性)", ["主膵管連通あり / 葡萄の房状", "壁結節 ≧ 5mm で即手術検討"]),
        ("MCN (粘液性嚢胞腫瘍)", ["中年女性・膵尾部 / 厚い被膜", "潜在的悪性 (原則全例手術)"]),
        ("SCN (漿液性嚢胞腫瘍)", ["ハニカム像 / 中央星状石灰化", "ほぼ100%良性 (経過観察)"]),
        ("仮性嚢胞 (Pseudocyst)", ["膵炎既往 / 単房性無エコー", "非腫瘍性嚢胞"])
    ]

    y_start = 350
    for title, lines in cystic_items:
        border_c = "#ec4899" if "IPMN" in title or "MCN" in title or "SCN" in title else "#6b7280"
        draw_textbox(draw, (590, y_start, 1050, y_start + 135), "#ffffff", border_c, title, lines)
        y_start += 150

    path = os.path.join(img_dir, "pancreatic_mass_classification.png")
    img.save(path, quality=95)
    print("Perfect Fit: pancreatic_mass_classification.png")

# 2. Cholecystitis Flow (Perfect Fit)
def make_chole_fit():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 75)], fill="#991b1b")
    draw.text((550, 45), "TG18/13 急性胆嚢炎 (Cholecystitis) 診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw_textbox(draw, (280, 95, 820, 155), "#fee2e2", "#991b1b", "右上腹部痛 ＋ 発熱 ＋ 炎症反応陽性", [], True)
    draw.rectangle([(280, 95), (820, 155)], fill="#fee2e2", outline="#991b1b", width=3)
    draw.text((550, 125), "右上腹部痛 ＋ 発熱 ＋ 炎症反応陽性", fill="#7f1d1d", font=font_large, anchor="mm")

    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw_textbox(draw, (80, 185, 1020, 285), "#f8fafc", "#dc2626", "【 Bモード4大サインの評価 】", [
        "1. 壁肥厚 >3mm | 2. 二重壁像 (浮腫状層) | 3. 胆嚢腫大 (短径≧4cm) | 4. 嵌頓結石"
    ])
    
    draw.line([(550, 285), (550, 315)], fill="#64748b", width=3)
    
    draw_textbox(draw, (150, 315, 950, 405), "#fef2f2", "#b91c1c", "直視下 探触子圧迫試行", [
        "超音波 Murphy 徴候 陽性 (胆嚢直上で痛覚最高潮 ＋ 吸気中断)"
    ])
    
    draw.line([(550, 405), (550, 435)], fill="#64748b", width=3)
    draw.line([(300, 435), (800, 435)], fill="#64748b", width=3)
    draw.line([(300, 435), (300, 465)], fill="#64748b", width=3)
    draw.line([(800, 435), (800, 465)], fill="#64748b", width=3)
    
    draw_textbox(draw, (50, 465, 520, 760), "#ffffff", "#dc2626", "★ 急性胆嚢炎 確診 (確定)", [
        "・早期腹腔鏡下胆嚢摘出術 (Lap-C) 検討",
        "・壊疽性サイン (壁連続性断裂/脱落膜)",
        "・気腫性サイン (Dirty shadow/Ring-down)"
    ])
    
    draw_textbox(draw, (580, 465, 1050, 760), "#ffffff", "#64748b", "慢性胆嚢炎 / 他疾患の考慮", [
        "・胆嚢壁全周性高度線維化肥厚",
        "・Porcelain GB (陶器様胆嚢石灰化)",
        "・肝炎 / 右心不全による二次性壁浮腫鑑別"
    ])
    
    path = os.path.join(img_dir, "cholecystitis_flowchart.png")
    img.save(path, quality=95)
    print("Perfect Fit: cholecystitis_flowchart.png")

# 3. Hydronephrosis (Perfect Fit)
def make_hydro_fit():
    w, h = 1100, 780
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 75)], fill="#4c1d95")
    draw.text((550, 45), "水腎症 (Hydronephrosis) SFU Grade 1～4 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    y = 105
    grades = [
        ("Grade 1 (軽度)", ["腎盂のみの分離・軽度拡張 (Pelvis Expansion Only)", "腎杯拡張なし / 腎実質厚正常"], "#f3e8ff", "#6b21a8"),
        ("Grade 2 (中等度)", ["腎盂拡張 ＋ 主要腎杯 (Major Calyces) の軽度拡張", "腎実質厚正常"], "#e9d5ff", "#6b21a8"),
        ("Grade 3 (高度)", ["腎盂 ＋ 全腎杯 (Minor Calyces) 水疱状・クラゲ様拡張", "腎実質厚は保たれる"], "#d8b4fe", "#581c87"),
        ("Grade 4 (重症)", ["全腎杯極度拡張 ＋ ★ 腎実質の菲薄化 (実質厚 < 10mm)", "腎機能不可逆的障害の危険信号"], "#fee2e2", "#991b1b")
    ]
    
    for title, lines, bg_c, text_c in grades:
        draw_textbox(draw, (50, y, 1050, y + 140), bg_c, text_c, title, lines)
        y += 160
        
    path = os.path.join(img_dir, "hydronephrosis_sfu_flowchart.png")
    img.save(path, quality=95)
    print("Perfect Fit: hydronephrosis_sfu_flowchart.png")

# 4. GB Polyps & ADM (Perfect Fit)
def make_gb_polyps_fit():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 75)], fill="#065f46")
    draw.text((550, 45), "胆嚢隆起性病変・ADM 超音波鑑別 10mm アルゴリズム", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(300, 95), (800, 155)], fill="#ecfdf5", outline="#065f46", width=3)
    draw.text((550, 125), "胆嚢腔内 隆起性病変 / 壁肥厚の検出", fill="#065f46", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    draw.line([(280, 185), (820, 185)], fill="#64748b", width=3)
    draw.line([(280, 185), (280, 215)], fill="#64748b", width=3)
    draw.line([(820, 185), (820, 215)], fill="#64748b", width=3)
    
    draw_textbox(draw, (50, 215, 510, 485), "#f0fdf4", "#16a34a", "【 病変径 < 10.0 mm (1cm未満) 】", [
        "・コレステロールポリープ (90%以上)",
        "  (桑実像 Mulberry / 有茎性 / 微小点状高エコー)",
        "・超音波経過観察 (6〜12ヶ月毎)",
        "・急増傾向がないかチェック"
    ])
    
    draw_textbox(draw, (590, 215, 1050, 485), "#fef2f2", "#dc2626", "【 病変径 ≧ 10.0 mm (1cm以上) 】", [
        "・胆嚢がん (Carcinoma) / 腺腫疑い",
        "・広基性 (Broad-based) / 茎が太い像",
        "・壁層構造の断裂・局所浸潤像",
        "★ EUS (超音波内視鏡) ＆ 手術検討"
    ])
    
    draw_textbox(draw, (50, 515, 1050, 765), "#eff6ff", "#2563eb", "【 胆嚢腺筋腫症 (ADM: Adenomyomatosis) の鑑別 】", [
        "・Comet-tail Artifact (RAS内コレステロール結晶による彗星の尾様多重反射)",
        "・壁内無エコー像 (Anechoic Microcysts: 1〜3mmの小嚢胞)",
        "・3形態分類: 1. 底部型 (Fundal) | 2. 節状型 (Segmental) | 3. びまん型 (Diffuse)"
    ])
    
    path = os.path.join(img_dir, "gb_polyps_adm_flowchart.png")
    img.save(path, quality=95)
    print("Perfect Fit: gb_polyps_adm_flowchart.png")

# 5. Fatty Liver (Perfect Fit)
def make_fatty_fit():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 75)], fill="#15803d")
    draw.text((550, 45), "脂肪肝 (Fatty Liver / MASLD) 重症度・局所性変化 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(280, 95), (820, 155)], fill="#f0fdf4", outline="#15803d", width=3)
    draw.text((550, 125), "上腹部走査: 肝腎長軸像 ＆ 右肋骨下斜断像", fill="#14532d", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw_textbox(draw, (80, 185, 1020, 285), "#f8fafc", "#16a34a", "【 4大サイン ＆ 減衰係数 ATI / UAP の評価 】", [
        "1. 肝腎コントラスト | 2. 深部減衰 | 3. 門脈壁消退 | 4. ATI > 0.63 dB/cm/MHz"
    ])
    
    draw.line([(550, 285), (550, 315)], fill="#64748b", width=3)
    draw.line([(300, 315), (800, 315)], fill="#64748b", width=3)
    draw.line([(300, 315), (300, 345)], fill="#64748b", width=3)
    draw.line([(800, 315), (800, 345)], fill="#64748b", width=3)
    
    draw_textbox(draw, (50, 345, 520, 765), "#ffffff", "#16a34a", "【 全般性脂肪肝 Grade 分類 】", [
        "・Grade 1 (軽度): 肝腎コントラスト軽度陽性",
        "・Grade 2 (中等度): 深部減衰・門脈壁不鮮明",
        "・Grade 3 (高度): 肝深部・横隔膜描出不能",
        "★ SWE線維化評価: F4(肝硬変) > 11 kPa"
    ])
    
    draw_textbox(draw, (580, 345, 1050, 765), "#ffffff", "#eab308", "【 局所性脂肪回避 (Focal Sparing) 】", [
        "・好発部位: 胆嚢床(S5) / 門脈臍部(S4)",
        "・非門脈系第三の血流流入による",
        "★ 腫瘍(Mass)との鑑別:",
        "   血管が病変内を直進貫通 (Mass effect無)"
    ])
    
    path = os.path.join(img_dir, "liver_fatty_flowchart.png")
    img.save(path, quality=95)
    print("Perfect Fit: liver_fatty_flowchart.png")

# 6. Appendicitis (Perfect Fit)
def make_app_fit():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 75)], fill="#c2410c")
    draw.text((550, 45), "急性虫垂炎 (Acute Appendicitis) 超音波診断・期別フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(280, 95), (820, 155)], fill="#fff7ed", outline="#c2410c", width=3)
    draw.text((550, 125), "右下腹部 段階的圧迫走査 (Graded Compression)", fill="#9a3412", font=font_large, anchor="mm")
    
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw_textbox(draw, (80, 185, 1020, 285), "#f8fafc", "#ea580c", "【 虫垂の描出 ＆ 圧迫消退性の確認 】", [
        "1. 虫垂外径 > 6.0 mm | 2. 圧迫非消退 (丸い断面のまま) | 3. Sonographic McBurney 陽性"
    ])
    
    draw.line([(550, 285), (550, 315)], fill="#64748b", width=3)
    
    draw.rectangle([(40, 315), (1060, 765)], fill="#ffffff", outline="#c2410c", width=3)
    draw.text((550, 345), "【 病理病態期別の観察基準 】", fill="#9a3412", font=font_large, anchor="mm")
    
    stages = [
        ("カタル性 (Catarrhal)", ["外径 6-8mm / 5層構造完全保持 / 軽度血流増加"], "#ffedd5", "#9a3412"),
        ("蜂窩織炎性 (Phlegmonous)", ["外径 8-12mm / 粘膜下層肥厚 / ★ 著明な壁内血流増加 (Hyperemia)"], "#fed7aa", "#9a3412"),
        ("壊疽性 (Gangrenous)", ["外径 > 10mm / 壁層構造断裂 / ★ 壁内血流の完全消失 (無血流/壊死)"], "#fee2e2", "#991b1b")
    ]
    
    y = 385
    for title, lines, bg_c, text_c in stages:
        draw_textbox(draw, (60, y, 1040, y + 110), bg_c, text_c, title, lines)
        y += 125
        
    path = os.path.join(img_dir, "appendicitis_flowchart.png")
    img.save(path, quality=95)
    print("Perfect Fit: appendicitis_flowchart.png")

make_panc_mass_fit()
make_chole_fit()
make_hydro_fit()
make_gb_polyps_fit()
make_fatty_fit()
make_app_fit()
