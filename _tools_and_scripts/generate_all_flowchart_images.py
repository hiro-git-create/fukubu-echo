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
            font_large = ImageFont.truetype(fp, 22)
            font_mid = ImageFont.truetype(fp, 16)
            font_small = ImageFont.truetype(fp, 13)
            break
        except Exception:
            continue

if font_large is None:
    font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"
os.makedirs(img_dir, exist_ok=True)

# 1. Cholecystitis TG18 Flowchart
def make_chole_flow():
    w, h = 900, 650
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (880, 65)], fill="#991b1b")
    draw.text((450, 40), "TG18/13 急性胆嚢炎 (Acute Cholecystitis) 超音波診断フロー", fill="#ffffff", font=font_large, anchor="mm")
    
    # Root
    draw.rectangle([(300, 85), (600, 130)], fill="#fee2e2", outline="#991b1b", width=2)
    draw.text((450, 107), "右上腹部痛 ＋ 発熱 ＋ 炎症反応陽性", fill="#7f1d1d", font=font_mid, anchor="mm")
    
    # Line
    draw.line([(450, 130), (450, 165)], fill="#64748b", width=2)
    
    # Step 1: US Signatures
    draw.rectangle([(150, 165), (750, 235)], fill="#f8fafc", outline="#dc2626", width=2)
    draw.text((450, 185), "【 Bモード4大サインの評価 】", fill="#991b1b", font=font_mid, anchor="mm")
    draw.text((450, 212), "1. 壁肥厚 >3mm | 2. 二重壁像 (浮腫) | 3. 胆嚢腫大 (短径≧4cm) | 4. 嵌頓結石", fill="#334155", font=font_small, anchor="mm")
    
    # Line
    draw.line([(450, 235), (450, 270)], fill="#64748b", width=2)
    
    # Step 2: Sonographic Murphy
    draw.rectangle([(200, 270), (700, 335)], fill="#fef2f2", outline="#b91c1c", width=2)
    draw.text((450, 290), "直視下 探触子圧迫試行", fill="#991b1b", font=font_mid, anchor="mm")
    draw.text((450, 315), "超音波 Murphy 徴候 陽性 (胆嚢直上で痛覚最高潮 ＋ 吸気中断)", fill="#b91c1c", font=font_small, anchor="mm")
    
    # Line split
    draw.line([(450, 335), (450, 370)], fill="#64748b", width=2)
    draw.line([(250, 370), (650, 370)], fill="#64748b", width=2)
    draw.line([(250, 370), (250, 400)], fill="#64748b", width=2)
    draw.line([(650, 370), (650, 400)], fill="#64748b", width=2)
    
    # Left: Acute Cholecystitis Confirmed
    draw.rectangle([(60, 400), (440, 600)], fill="#ffffff", outline="#dc2626", width=2)
    draw.text((250, 425), "★ 急性胆嚢炎 確診 (確実)", fill="#991b1b", font=font_mid, anchor="mm")
    draw.text((250, 470), "・早期腹腔鏡下胆嚢摘出術 (Lap-C) 検討\n・壊疽性サイン (壁連続性断裂/膜脱落) の有無検索\n・気腫性サイン (Dirty shadow/Ring-down) の確認", fill="#334155", font=font_small, anchor="mm")
    
    # Right: Chronic / Differential
    draw.rectangle([(460, 400), (840, 600)], fill="#ffffff", outline="#64748b", width=2)
    draw.text((650, 425), "慢性胆嚢炎 / 他疾患の考慮", fill="#334155", font=font_mid, anchor="mm")
    draw.text((650, 470), "・胆嚢壁全周性高度線維化肥厚\n・Porcelain Gallbladder (陶器様石灰化胆嚢)\n・急性肝炎 / 右心不全に伴う二次性胆嚢壁浮腫の鑑別", fill="#475569", font=font_small, anchor="mm")
    
    path = os.path.join(img_dir, "cholecystitis_flowchart.png")
    img.save(path, quality=95)
    print("Saved cholecystitis_flowchart.png")

# 2. GB Polyps & ADM 10mm Flowchart
def make_gb_polyps_flow():
    w, h = 900, 650
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (880, 65)], fill="#065f46")
    draw.text((450, 40), "胆嚢隆起性病変・ADM 超音波鑑別 10mm アルゴリズム", fill="#ffffff", font=font_large, anchor="mm")
    
    # Root
    draw.rectangle([(300, 85), (600, 130)], fill="#ecfdf5", outline="#065f46", width=2)
    draw.text((450, 107), "胆嚢腔内 隆起性病変 / 壁肥厚の検出", fill="#065f46", font=font_mid, anchor="mm")
    
    # Line split
    draw.line([(450, 130), (450, 155)], fill="#64748b", width=2)
    draw.line([(250, 155), (650, 155)], fill="#64748b", width=2)
    draw.line([(250, 155), (250, 180)], fill="#64748b", width=2)
    draw.line([(650, 155), (650, 180)], fill="#64748b", width=2)
    
    # Branch 1: Polyps < 10mm
    draw.rectangle([(50, 180), (430, 390)], fill="#f0fdf4", outline="#16a34a", width=2)
    draw.text((240, 205), "【 病変径 < 10.0 mm (1cm未満) 】", fill="#15803d", font=font_mid, anchor="mm")
    draw.text((240, 290), "・コレステロールポリープ (90%以上)\n  (桑実像 Mulberry / 有茎性 / 微小点状高エコー)\n・超音波経過観察 (6〜12ヶ月毎)\n・急激な増大傾斜がないか経過観察", fill="#166534", font=font_small, anchor="mm")
    
    # Branch 2: Polyps >= 10mm
    draw.rectangle([(470, 180), (850, 390)], fill="#fef2f2", outline="#dc2626", width=2)
    draw.text((660, 205), "【 病変径 ≧ 10.0 mm (1cm以上) 】", fill="#991b1b", font=font_mid, anchor="mm")
    draw.text((660, 290), "・胆嚢がん (Carcinoma) / 胆嚢腺腫の疑い\n・広基性 (Broad-based) / 茎が太い像\n・壁層構造の断裂・局所浸潤像\n★ EUS (超音波内視鏡) 精査 ＆ 胆嚢摘出術検討", fill="#991b1b", font=font_small, anchor="mm")
    
    # ADM Section below
    draw.rectangle([(50, 420), (850, 610)], fill="#eff6ff", outline="#2563eb", width=2)
    draw.text((450, 445), "【 胆嚢腺筋腫症 (ADM: Adenomyomatosis) の鑑別 】", fill="#1e40af", font=font_mid, anchor="mm")
    draw.text((450, 525), "・Comet-tail Artifact (RAS内コレステロール結晶による彗星の尾様多重反射)\n・壁内無エコー像 (Anechoic Microcysts: 1〜3mmの小嚢胞)\n・3形態分類: 1. 底部型 (Fundal) | 2. 節状型 (Segmental) | 3. びまん型 (Diffuse)", fill="#1e3a8a", font=font_small, anchor="mm")
    
    path = os.path.join(img_dir, "gb_polyps_adm_flowchart.png")
    img.save(path, quality=95)
    print("Saved gb_polyps_adm_flowchart.png")

# 3. Hydronephrosis SFU Grade Flowchart
def make_hydro_flow():
    w, h = 900, 620
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(20, 15), (880, 65)], fill="#4c1d95")
    draw.text((450, 40), "水腎症 (Hydronephrosis) SFU Grade 1～4 判定フロー", fill="#ffffff", font=font_large, anchor="mm")
    
    y = 90
    grades = [
        ("Grade 1 (軽度)", "腎盂のみの分離・軽度拡張 (Pelvis Expansion Only)\n腎杯の拡張なし / 腎実質厚正常", "#f3e8ff", "#6b21a8"),
        ("Grade 2 (中等度)", "腎盂の拡張 ＋ 主要腎杯 (Major Calyces) の軽度拡張\n腎実質厚正常", "#e9d5ff", "#6b21a8"),
        ("Grade 3 (高度)", "腎盂 ＋ 全腎杯 (Minor Calyces) の著明な水疱状・クラゲ様拡張\n腎実質厚は保たれる", "#d8b4fe", "#581c87"),
        ("Grade 4 (極度・重症)", "全腎杯の極度拡張 ＋ ★ 腎実質の菲薄化 (Parenchymal Thinning < 10mm)\n腎機能不可逆的障害の危険信号", "#fee2e2", "#991b1b")
    ]
    
    for title, desc, bg_c, text_c in grades:
        draw.rectangle([(60, y), (840, y + 105)], fill=bg_c, outline=text_c, width=2)
        draw.text((200, y + 52), title, fill=text_c, font=font_mid, anchor="mm")
        draw.text((540, y + 52), desc, fill="#1e293b" if text_c != "#991b1b" else "#7f1d1d", font=font_small, anchor="mm")
        y += 120
        
    path = os.path.join(img_dir, "hydronephrosis_sfu_flowchart.png")
    img.save(path, quality=95)
    print("Saved hydronephrosis_sfu_flowchart.png")

make_chole_flow()
make_gb_polyps_flow()
make_hydro_flow()
