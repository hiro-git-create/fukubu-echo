import os
from PIL import Image, ImageDraw, ImageFont

# Set up font loading
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

# 1. Pancreatic Mass Classification (Large Text Version)
def make_panc_mass_large():
    w, h = 1000, 950
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(20, 15), (980, 75)], fill="#1e3a8a")
    draw.text((500, 45), "膵腫瘤性病変 (Pancreatic Mass) 完全分類フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    # Root
    draw.rectangle([(300, 95), (700, 150)], fill="#f1f5f9", outline="#1e3a8a", width=3)
    draw.text((500, 122), "膵腫瘤性病変 (Pancreatic Mass)", fill="#1e293b", font=font_large, anchor="mm")
    
    # Connectors
    draw.line([(500, 150), (500, 175)], fill="#64748b", width=3)
    draw.line([(260, 175), (740, 175)], fill="#64748b", width=3)
    draw.line([(260, 175), (260, 200)], fill="#64748b", width=3)
    draw.line([(740, 175), (740, 200)], fill="#64748b", width=3)
    
    # Category Headers
    draw.rectangle([(50, 200), (470, 255)], fill="#dbeafe", outline="#2563eb", width=3)
    draw.text((260, 227), "1. 固形腫瘤性病変 (Solid)", fill="#1e40af", font=font_large, anchor="mm")

    draw.rectangle([(530, 200), (950, 255)], fill="#fce7f3", outline="#db2777", width=3)
    draw.text((740, 227), "2. 嚢胞性腫瘤性病変 (Cystic)", fill="#9d174d", font=font_large, anchor="mm")

    # Left Solid Section
    draw.rectangle([(40, 275), (480, 920)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((260, 305), "【 固形腫瘤 (Solid Lesions) 】", fill="#1e3a8a", font=font_large, anchor="mm")

    solid_items = [
        ("通常型膵がん (PDAC)", "浸潤性管がん (全体の約90%)\n低血流 / 主膵管高度拡張 (>3mm)"),
        ("膵神経内分泌腫瘍 (PanNET)", "境界ナイフ様鮮明 / 多血性 (Hyper)\n血流極めて豊富 / 主膵管拡張なし"),
        ("Solid Pseudopapillary (SPN)", "10〜30代若い女性に好発\n固形 ＋ 出血壊死性嚢胞の混在"),
        ("自己免疫性膵炎 (AIP)", "腫瘤形成性膵炎 (膵がん酷似)\nCapsule-like Rim / 主膵管狭小化")
    ]

    y_start = 340
    for title, desc in solid_items:
        draw.rectangle([(60, y_start), (460, y_start + 125)], fill="#ffffff", outline="#3b82f6", width=2)
        draw.text((260, y_start + 30), title, fill="#1e3a8a", font=font_large, anchor="mm")
        draw.text((260, y_start + 80), desc, fill="#334155", font=font_small, anchor="mm")
        y_start += 140

    # Right Cystic Section
    draw.rectangle([(520, 275), (960, 920)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((740, 305), "【 嚢胞性腫瘤 (Cystic Lesions) 】", fill="#831843", font=font_large, anchor="mm")

    cystic_items = [
        ("IPMN (膵管内乳頭粘液性)", "主膵管連通あり / 葡萄の房状\n壁結節 ≧ 5mm で即手術検討"),
        ("MCN (粘液性嚢胞腫瘍)", "中年女性・膵尾部 / 厚い被膜\n潜在的悪性 (原則全例手術)"),
        ("SCN (漿液性嚢胞腫瘍)", "ハニカム像 / 中央星状石灰化\nほぼ100%良性 (経過観察)"),
        ("仮性嚢胞 (Pseudocyst)", "膵炎既往 / 単房性無エコー\n非腫瘍性嚢胞")
    ]

    y_start = 340
    for title, desc in cystic_items:
        fill_bg = "#ffffff"
        border_c = "#ec4899" if "IPMN" in title or "MCN" in title or "SCN" in title else "#6b7280"
        draw.rectangle([(540, y_start), (940, y_start + 125)], fill=fill_bg, outline=border_c, width=2)
        draw.text((740, y_start + 30), title, fill="#831843" if border_c != "#6b7280" else "#1f2937", font=font_large, anchor="mm")
        draw.text((740, y_start + 80), desc, fill="#334155", font=font_small, anchor="mm")
        y_start += 140

    path = os.path.join(img_dir, "pancreatic_mass_classification.png")
    img.save(path, quality=95)
    print("Updated pancreatic_mass_classification.png (Large Font)")

# 2. Cholecystitis TG18 Flow (Large Text)
def make_chole_large():
    w, h = 1000, 750
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (980, 75)], fill="#991b1b")
    draw.text((500, 45), "TG18/13 急性胆嚢炎 (Cholecystitis) 診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (750, 150)], fill="#fee2e2", outline="#991b1b", width=3)
    draw.text((500, 122), "右上腹部痛 ＋ 発熱 ＋ 炎症反応陽性", fill="#7f1d1d", font=font_large, anchor="mm")
    
    draw.line([(500, 150), (500, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(100, 185), (900, 275)], fill="#f8fafc", outline="#dc2626", width=3)
    draw.text((500, 212), "【 Bモード4大サインの評価 】", fill="#991b1b", font=font_large, anchor="mm")
    draw.text((500, 248), "1. 壁肥厚 >3mm | 2. 二重壁像 (浮腫) | 3. 胆嚢腫大 (短径≧4cm) | 4. 嵌頓結石", fill="#1e293b", font=font_mid, anchor="mm")
    
    draw.line([(500, 275), (500, 310)], fill="#64748b", width=3)
    
    draw.rectangle([(150, 310), (850, 390)], fill="#fef2f2", outline="#b91c1c", width=3)
    draw.text((500, 335), "直視下 探触子圧迫試行", fill="#991b1b", font=font_large, anchor="mm")
    draw.text((500, 368), "超音波 Murphy 徴候 陽性 (胆嚢直上で痛覚最高潮 ＋ 吸気中断)", fill="#b91c1c", font=font_mid, anchor="mm")
    
    draw.line([(500, 390), (500, 425)], fill="#64748b", width=3)
    draw.line([(280, 425), (720, 425)], fill="#64748b", width=3)
    draw.line([(280, 425), (280, 455)], fill="#64748b", width=3)
    draw.line([(720, 425), (720, 455)], fill="#64748b", width=3)
    
    draw.rectangle([(50, 455), (470, 710)], fill="#ffffff", outline="#dc2626", width=3)
    draw.text((260, 485), "★ 急性胆嚢炎 確診 (確定)", fill="#991b1b", font=font_large, anchor="mm")
    draw.text((260, 580), "・早期腹腔鏡下胆嚢摘出術 (Lap-C)\n・壊疽性サイン (壁断裂/脱落膜)\n・気腫性サイン (Dirty shadow)", fill="#1e293b", font=font_mid, anchor="mm")
    
    draw.rectangle([(530, 455), (950, 710)], fill="#ffffff", outline="#64748b", width=3)
    draw.text((740, 485), "慢性胆嚢炎 / 他疾患の考慮", fill="#334155", font=font_large, anchor="mm")
    draw.text((740, 580), "・胆嚢壁全周性高度線維化肥厚\n・Porcelain GB (陶器様胆嚢)\n・肝炎/右心不全の二次性浮腫鑑別", fill="#334155", font=font_mid, anchor="mm")
    
    path = os.path.join(img_dir, "cholecystitis_flowchart.png")
    img.save(path, quality=95)
    print("Updated cholecystitis_flowchart.png (Large Font)")

# 3. Hydronephrosis SFU Flow (Large Text)
def make_hydro_large():
    w, h = 1000, 750
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (980, 75)], fill="#4c1d95")
    draw.text((500, 45), "水腎症 (Hydronephrosis) SFU Grade 1～4 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    y = 100
    grades = [
        ("Grade 1 (軽度)", "腎盂のみの分離・軽度拡張 (Pelvis Expansion)\n腎杯拡張なし / 実質厚正常", "#f3e8ff", "#6b21a8"),
        ("Grade 2 (中等度)", "腎盂拡張 ＋ 主要腎杯 (Major Calyces) 軽度拡張\n腎実質厚正常", "#e9d5ff", "#6b21a8"),
        ("Grade 3 (高度)", "腎盂 ＋ 全腎杯 (Minor Calyces) 水疱状・クラゲ様拡張\n腎実質厚は保たれる", "#d8b4fe", "#581c87"),
        ("Grade 4 (重症)", "全腎杯極度拡張 ＋ ★ 腎実質の菲薄化 (実質厚 < 10mm)\n腎機能不可逆的障害の危険信号", "#fee2e2", "#991b1b")
    ]
    
    for title, desc, bg_c, text_c in grades:
        draw.rectangle([(50, y), (950, y + 130)], fill=bg_c, outline=text_c, width=3)
        draw.text((230, y + 65), title, fill=text_c, font=font_large, anchor="mm")
        draw.text((610, y + 65), desc, fill="#1e293b" if text_c != "#991b1b" else "#7f1d1d", font=font_mid, anchor="mm")
        y += 150
        
    path = os.path.join(img_dir, "hydronephrosis_sfu_flowchart.png")
    img.save(path, quality=95)
    print("Updated hydronephrosis_sfu_flowchart.png (Large Font)")

# 4. GB Polyps 10mm Flow (Large Text)
def make_gb_polyps_large():
    w, h = 1000, 750
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (980, 75)], fill="#065f46")
    draw.text((500, 45), "胆嚢隆起性病変・ADM 超音波鑑別 10mm アルゴリズム", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(280, 95), (720, 150)], fill="#ecfdf5", outline="#065f46", width=3)
    draw.text((500, 122), "胆嚢腔内 隆起性病変 / 壁肥厚の検出", fill="#065f46", font=font_large, anchor="mm")
    
    draw.line([(500, 150), (500, 175)], fill="#64748b", width=3)
    draw.line([(270, 175), (730, 175)], fill="#64748b", width=3)
    draw.line([(270, 175), (270, 205)], fill="#64748b", width=3)
    draw.line([(730, 175), (730, 205)], fill="#64748b", width=3)
    
    draw.rectangle([(50, 205), (470, 455)], fill="#f0fdf4", outline="#16a34a", width=3)
    draw.text((260, 235), "【 病変径 < 10.0 mm (1cm未満) 】", fill="#15803d", font=font_large, anchor="mm")
    draw.text((260, 340), "・コレステロールポリープ (90%以上)\n  (桑実像 Mulberry / 有茎性 / 微小点状高エコー)\n・超音波経過観察 (6〜12ヶ月毎)\n・急増傾向がないかチェック", fill="#166534", font=font_mid, anchor="mm")
    
    draw.rectangle([(530, 205), (950, 455)], fill="#fef2f2", outline="#dc2626", width=3)
    draw.text((740, 235), "【 病変径 ≧ 10.0 mm (1cm以上) 】", fill="#991b1b", font=font_large, anchor="mm")
    draw.text((740, 340), "・胆嚢がん (Carcinoma) / 腺腫疑い\n・広基性 (Broad-based) / 茎が太い像\n・壁層構造の断裂・局所浸潤像\n★ EUS (超音波内視鏡) ＆ 手術検討", fill="#991b1b", font=font_mid, anchor="mm")
    
    draw.rectangle([(50, 485), (950, 715)], fill="#eff6ff", outline="#2563eb", width=3)
    draw.text((500, 515), "【 胆嚢腺筋腫症 (ADM: Adenomyomatosis) の鑑別 】", fill="#1e40af", font=font_large, anchor="mm")
    draw.text((500, 615), "・Comet-tail Artifact (RAS内コレステロール結晶による彗星の尾様多重反射)\n・壁内無エコー像 (Anechoic Microcysts: 1〜3mmの小嚢胞)\n・3形態分類: 1. 底部型 (Fundal) | 2. 節状型 (Segmental) | 3. びまん型 (Diffuse)", fill="#1e3a8a", font=font_mid, anchor="mm")
    
    path = os.path.join(img_dir, "gb_polyps_adm_flowchart.png")
    img.save(path, quality=95)
    print("Updated gb_polyps_adm_flowchart.png (Large Font)")

make_panc_mass_large()
make_chole_large()
make_hydro_large()
make_gb_polyps_large()
