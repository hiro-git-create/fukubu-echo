import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 32)
            font_large = ImageFont.truetype(fp, 26)
            font_mid = ImageFont.truetype(fp, 21)
            font_small = ImageFont.truetype(fp, 18)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

# Helper function for perfectly centered vertical & horizontal text in tight fitting boxes
def draw_tight_box(draw, box, fill_bg, outline_c, title, lines, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    
    t_color = title_color if title_color else outline_c
    
    if not lines:
        # Single title box
        draw.text(((x1 + x2) // 2, (y1 + y2) // 2), title, fill=t_color, font=font_large, anchor="mm")
    else:
        # Calculate total height of text block to perfectly center vertically inside the box
        title_h = 32
        lines_h = len(lines) * 30
        total_h = title_h + 12 + lines_h
        
        start_y = y1 + ((y2 - y1) - total_h) // 2 + 16
        
        # Title
        draw.text(((x1 + x2) // 2, start_y), title, fill=t_color, font=font_large, anchor="mm")
        
        # Lines
        cur_y = start_y + 32
        for line in lines:
            draw.text(((x1 + x2) // 2, cur_y), line, fill="#1e293b", font=font_mid, anchor="mm")
            cur_y += 30

# 1. GB Polyps & ADM (Golden Ratio Fit)
def make_gb_polyps_golden():
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Top Header
    draw.rectangle([(20, 15), (1080, 70)], fill="#065f46")
    draw.text((550, 42), "胆嚢隆起性病変・ADM 超音波鑑別 10mm アルゴリズム", fill="#ffffff", font=font_title, anchor="mm")
    
    # Level 1 Root
    draw_tight_box(draw, (280, 90, 820, 140), "#ecfdf5", "#065f46", "胆嚢腔内 隆起性病変 / 壁肥厚の検出", [])
    
    # Lines
    draw.line([(550, 140), (550, 165)], fill="#64748b", width=3)
    draw.line([(280, 165), (820, 165)], fill="#64748b", width=3)
    draw.line([(280, 165), (280, 190)], fill="#64748b", width=3)
    draw.line([(820, 165), (820, 190)], fill="#64748b", width=3)
    
    # Left & Right Boxes (Height: 250px)
    draw_tight_box(draw, (40, 190, 520, 440), "#f0fdf4", "#16a34a", "【 病変径 < 10.0 mm (1cm未満) 】", [
        "・コレステロールポリープ (90%以上)",
        "  (桑実像 Mulberry / 有茎性 / 微小点状高エコー)",
        "・超音波経過観察 (6〜12ヶ月毎)",
        "・急増傾向がないかチェック"
    ])
    
    draw_tight_box(draw, (580, 190, 1060, 440), "#fef2f2", "#dc2626", "【 病変径 ≧ 10.0 mm (1cm以上) 】", [
        "・胆嚢がん (Carcinoma) / 腺腫疑い",
        "・広基性 (Broad-based) / 茎が太い像",
        "・壁層構造の断裂・局所浸潤像",
        "★ EUS (超音波内視鏡) ＆ 手術検討"
    ], title_color="#991b1b")
    
    # Bottom Box (Height: 220px)
    draw_tight_box(draw, (40, 465, 1060, 695), "#eff6ff", "#2563eb", "【 胆嚢腺筋腫症 (ADM: Adenomyomatosis) の鑑別 】", [
        "・Comet-tail Artifact (RAS内コレステロール結晶による彗星の尾様多重反射)",
        "・壁内無エコー像 (Anechoic Microcysts: 1〜3mmの小嚢胞)",
        "・3形態分類: 1. 底部型 (Fundal) | 2. 節状型 (Segmental) | 3. びまん型 (Diffuse)"
    ], title_color="#1e40af")
    
    path = os.path.join(img_dir, "gb_polyps_adm_flowchart.png")
    img.save(path, quality=95)
    print("Golden ratio fit: gb_polyps_adm_flowchart.png")

# 2. Pancreatic Mass (Golden Ratio Fit)
def make_panc_mass_golden():
    w, h = 1100, 920
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 70)], fill="#1e3a8a")
    draw.text((550, 42), "膵腫瘤性病変 (Pancreatic Mass) 完全分類フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw_tight_box(draw, (320, 90, 780, 140), "#f1f5f9", "#1e3a8a", "膵腫瘤性病変 (Pancreatic Mass)", [])
    
    draw.line([(550, 140), (550, 165)], fill="#64748b", width=3)
    draw.line([(280, 165), (820, 165)], fill="#64748b", width=3)
    draw.line([(280, 165), (280, 190)], fill="#64748b", width=3)
    draw.line([(820, 165), (820, 190)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (40, 190, 520, 245), "#dbeafe", "#2563eb", "1. 固形腫瘤性病変 (Solid)", [], title_color="#1e40af")
    draw_tight_box(draw, (580, 190, 1060, 245), "#fce7f3", "#db2777", "2. 嚢胞性腫瘤性病変 (Cystic)", [], title_color="#9d174d")
    
    # Left Section
    draw.rectangle([(30, 260), (530, 895)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((280, 285), "【 固形腫瘤 (Solid Lesions) 】", fill="#1e3a8a", font=font_large, anchor="mm")

    solid_items = [
        ("通常型膵がん (PDAC)", ["浸潤性管がん (全体の約90%)", "低血流 / 主膵管高度拡張 (>3mm)"]),
        ("膵神経内分泌腫瘍 (PanNET)", ["境界ナイフ様鮮明 / 多血性(Hyper)", "血流極めて豊富 / 主膵管拡張なし"]),
        ("Solid Pseudopapillary (SPN)", ["10〜30代若い女性に好発", "固形 ＋ 出血壊死性嚢胞の混在"]),
        ("自己免疫性膵炎 (AIP)", ["腫瘤形成性膵炎 (膵がん酷似)", "Capsule-like Rim / 主膵管狭小化"])
    ]

    y_start = 315
    for title, lines in solid_items:
        draw_tight_box(draw, (50, y_start, 510, y_start + 130), "#ffffff", "#3b82f6", title, lines)
        y_start += 142

    # Right Section
    draw.rectangle([(570, 260), (1070, 895)], fill="#f8fafc", outline="#94a3b8", width=2)
    draw.text((820, 285), "【 嚢胞性腫瘤 (Cystic Lesions) 】", fill="#831843", font=font_large, anchor="mm")

    cystic_items = [
        ("IPMN (膵管内乳頭粘液性)", ["主膵管連通あり / 葡萄の房状", "壁結節 ≧ 5mm で即手術検討"]),
        ("MCN (粘液性嚢胞腫瘍)", ["中年女性・膵尾部 / 厚い被膜", "潜在的悪性 (原則全例手術)"]),
        ("SCN (漿液性嚢胞腫瘍)", ["ハニカム像 / 中央星状石灰化", "ほぼ100%良性 (経過観察)"]),
        ("仮性嚢胞 (Pseudocyst)", ["膵炎既往 / 単房性無エコー", "非腫瘍性嚢胞"])
    ]

    y_start = 315
    for title, lines in cystic_items:
        border_c = "#ec4899" if "IPMN" in title or "MCN" in title or "SCN" in title else "#6b7280"
        draw_tight_box(draw, (590, y_start, 1050, y_start + 130), "#ffffff", border_c, title, lines)
        y_start += 142

    path = os.path.join(img_dir, "pancreatic_mass_classification.png")
    img.save(path, quality=95)
    print("Golden ratio fit: pancreatic_mass_classification.png")

# 3. Cholecystitis (Golden Ratio Fit)
def make_chole_golden():
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 70)], fill="#991b1b")
    draw.text((550, 42), "TG18/13 急性胆嚢炎 (Cholecystitis) 診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw_tight_box(draw, (280, 88, 820, 138), "#fee2e2", "#991b1b", "右上腹部痛 ＋ 発熱 ＋ 炎症反応陽性", [], title_color="#7f1d1d")
    
    draw.line([(550, 138), (550, 160)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (80, 160, 1020, 260), "#f8fafc", "#dc2626", "【 Bモード4大サインの評価 】", [
        "1. 壁肥厚 >3mm | 2. 二重壁像 (浮腫状層) | 3. 胆嚢腫大 (短径≧4cm) | 4. 嵌頓結石"
    ])
    
    draw.line([(550, 260), (550, 285)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (150, 285, 950, 385), "#fef2f2", "#b91c1c", "直視下 探触子圧迫試行", [
        "超音波 Murphy 徴候 陽性 (胆嚢直上で痛覚最高潮 ＋ 吸気中断)"
    ])
    
    draw.line([(550, 385), (550, 410)], fill="#64748b", width=3)
    draw.line([(300, 410), (800, 410)], fill="#64748b", width=3)
    draw.line([(300, 410), (300, 435)], fill="#64748b", width=3)
    draw.line([(800, 410), (800, 435)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (40, 435, 520, 695), "#ffffff", "#dc2626", "★ 急性胆嚢炎 確診 (確定)", [
        "・早期腹腔鏡下胆嚢摘出術 (Lap-C) 検討",
        "・壊疽性サイン (壁連続性断裂/脱落膜)",
        "・気腫性サイン (Dirty shadow/Ring-down)"
    ])
    
    draw_tight_box(draw, (580, 435, 1060, 695), "#ffffff", "#64748b", "慢性胆嚢炎 / 他疾患の考慮", [
        "・胆嚢壁全周性高度線維化肥厚",
        "・Porcelain GB (陶器様胆嚢石灰化)",
        "・肝炎 / 右心不全による二次性壁浮腫鑑別"
    ], title_color="#334155")
    
    path = os.path.join(img_dir, "cholecystitis_flowchart.png")
    img.save(path, quality=95)
    print("Golden ratio fit: cholecystitis_flowchart.png")

# 4. Hydronephrosis (Golden Ratio Fit)
def make_hydro_golden():
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 70)], fill="#4c1d95")
    draw.text((550, 42), "水腎症 (Hydronephrosis) SFU Grade 1～4 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    y = 90
    grades = [
        ("Grade 1 (軽度)", ["腎盂のみの分離・軽度拡張 (Pelvis Expansion Only)", "腎杯拡張なし / 腎実質厚正常"], "#f3e8ff", "#6b21a8"),
        ("Grade 2 (中等度)", ["腎盂拡張 ＋ 主要腎杯 (Major Calyces) の軽度拡張", "腎実質厚正常"], "#e9d5ff", "#6b21a8"),
        ("Grade 3 (高度)", ["腎盂 ＋ 全腎杯 (Minor Calyces) 水疱状・クラゲ様拡張", "腎実質厚は保たれる"], "#d8b4fe", "#581c87"),
        ("Grade 4 (重症)", ["全腎杯極度拡張 ＋ ★ 腎実質の菲薄化 (実質厚 < 10mm)", "腎機能不可逆的障害の危険信号"], "#fee2e2", "#991b1b")
    ]
    
    for title, lines, bg_c, text_c in grades:
        draw_tight_box(draw, (40, y, 1060, y + 135), bg_c, text_c, title, lines)
        y += 150
        
    path = os.path.join(img_dir, "hydronephrosis_sfu_flowchart.png")
    img.save(path, quality=95)
    print("Golden ratio fit: hydronephrosis_sfu_flowchart.png")

# 5. Fatty Liver (Golden Ratio Fit)
def make_fatty_golden():
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 70)], fill="#15803d")
    draw.text((550, 42), "脂肪肝 (Fatty Liver / MASLD) 重症度・局所性変化 判定フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw_tight_box(draw, (280, 88, 820, 138), "#f0fdf4", "#15803d", "上腹部走査: 肝腎長軸像 ＆ 右肋骨下斜断像", [], title_color="#14532d")
    
    draw.line([(550, 138), (550, 160)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (80, 160, 1020, 260), "#f8fafc", "#16a34a", "【 4大サイン ＆ 減衰係数 ATI / UAP の評価 】", [
        "1. 肝腎コントラスト | 2. 深部減衰 | 3. 門脈壁消退 | 4. ATI > 0.63 dB/cm/MHz"
    ], title_color="#15803d")
    
    draw.line([(550, 260), (550, 285)], fill="#64748b", width=3)
    draw.line([(300, 285), (800, 285)], fill="#64748b", width=3)
    draw.line([(300, 285), (300, 410)], fill="#64748b", width=3)
    draw.line([(800, 285), (800, 410)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (40, 410, 520, 695), "#ffffff", "#16a34a", "【 全般性脂肪肝 Grade 分類 】", [
        "・Grade 1 (軽度): 肝腎コントラスト軽度陽性",
        "・Grade 2 (中等度): 深部減衰・門脈壁不鮮明",
        "・Grade 3 (高度): 肝深部・横隔膜描出不能",
        "★ SWE線維化評価: F4(肝硬変) > 11 kPa"
    ], title_color="#15803d")
    
    draw_tight_box(draw, (580, 410, 1060, 695), "#ffffff", "#eab308", "【 局所性脂肪回避 (Focal Sparing) 】", [
        "・好発部位: 胆嚢床(S5) / 門脈臍部(S4)",
        "・非門脈系第三の血流流入による",
        "★ 腫瘍(Mass)との鑑別:",
        "   血管が病変内を直進貫通 (Mass effect無)"
    ], title_color="#a16207")
    
    path = os.path.join(img_dir, "liver_fatty_flowchart.png")
    img.save(path, quality=95)
    print("Golden ratio fit: liver_fatty_flowchart.png")

# 6. Appendicitis (Golden Ratio Fit)
def make_app_golden():
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (1080, 70)], fill="#c2410c")
    draw.text((550, 42), "急性虫垂炎 (Acute Appendicitis) 超音波診断・期別フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw_tight_box(draw, (280, 88, 820, 138), "#fff7ed", "#c2410c", "右下腹部 段階的圧迫走査 (Graded Compression)", [], title_color="#9a3412")
    
    draw.line([(550, 138), (550, 160)], fill="#64748b", width=3)
    
    draw_tight_box(draw, (80, 160, 1020, 260), "#f8fafc", "#ea580c", "【 虫垂の描出 ＆ 圧迫消退性の確認 】", [
        "1. 虫垂外径 > 6.0 mm | 2. 圧迫非消退 (丸い断面のまま) | 3. Sonographic McBurney 陽性"
    ], title_color="#c2410c")
    
    draw.line([(550, 260), (550, 285)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 285), (1070, 695)], fill="#ffffff", outline="#c2410c", width=3)
    draw.text((550, 312), "【 病理病態期別の観察基準 】", fill="#9a3412", font=font_large, anchor="mm")
    
    stages = [
        ("カタル性 (Catarrhal)", ["外径 6-8mm / 5層構造完全保持 / 軽度血流増加"], "#ffedd5", "#9a3412"),
        ("蜂窩織炎性 (Phlegmonous)", ["外径 8-12mm / 粘膜下層肥厚 / ★ 著明な壁内血流増加 (Hyperemia)"], "#fed7aa", "#9a3412"),
        ("壊疽性 (Gangrenous)", ["外径 > 10mm / 壁層構造断裂 / ★ 壁内血流の完全消失 (無血流/壊死)"], "#fee2e2", "#991b1b")
    ]
    
    y = 345
    for title, lines, bg_c, text_c in stages:
        draw_tight_box(draw, (50, y, 1050, y + 100), bg_c, text_c, title, lines)
        y += 112
        
    path = os.path.join(img_dir, "appendicitis_flowchart.png")
    img.save(path, quality=95)
    print("Golden ratio fit: appendicitis_flowchart.png")

make_gb_polyps_golden()
make_panc_mass_golden()
make_chole_golden()
make_hydro_golden()
make_fatty_golden()
make_app_golden()
