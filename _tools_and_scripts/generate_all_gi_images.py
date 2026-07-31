import os
from PIL import Image, ImageDraw, ImageFont

font_title = font_large = font_mid = font_small = None
font_paths = ["C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc", "C:/Windows/Fonts/arial.ttf"]

for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_title = ImageFont.truetype(fp, 30)
            font_large = ImageFont.truetype(fp, 24)
            font_mid = ImageFont.truetype(fp, 21)
            font_small = ImageFont.truetype(fp, 18)
            break
        except Exception:
            continue

if font_title is None:
    font_title = font_large = font_mid = font_small = ImageFont.load_default()

img_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見\images"

def draw_two_line_box(draw, box, fill_bg, outline_c, title, desc_text, title_color=None):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=fill_bg, outline=outline_c, width=3)
    t_c = title_color if title_color else outline_c
    cx = (x1 + x2) // 2
    draw.text((cx, y1 + 30), title, fill=t_c, font=font_large, anchor="mm")
    draw.text((cx, y1 + 72), desc_text, fill="#1e293b", font=font_mid, anchor="mm")

# 2. Colorectal Cancer Images
def make_colorectal_images():
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#b91c1c")
    draw.text((550, 45), "大腸がん (Colorectal Cancer) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#fee2e2", outline="#b91c1c", width=3)
    draw.text((550, 125), "便潜血陽性・下血・便通異常・腹部腫瘤触知", fill="#991b1b", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#b91c1c", width=3)
    draw.text((550, 215), "【 4大超音波サイン ＆ 進行期判定 】", fill="#991b1b", font=font_large, anchor="mm")
    
    steps = [
        ("1. Apple-core Sign (リンゴの芯像)", "全周性不整低エコー壁肥厚 (> 5.0mm) による管腔狭窄", "#fee2e2", "#991b1b"),
        ("2. 大腸5層構造の層壊絶・破壊", "正常な層構造が消失し、不均一な腫瘤像 (Mass) を形成", "#ffedd5", "#c2410c"),
        ("3. Tumor Vascularity (腫瘍内豊富血流)", "カラードプラ/CEUSにて肥厚壁内に屈曲・拡張した豊富血流描出", "#dbeafe", "#1e40af"),
        ("4. 所属リンパ節腫大 ＆ 局所浸潤", "腸管外周・腸間膜根部に短径 > 8〜10mm の円形低エコーリンパ節", "#dcfce7", "#15803d")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "colorectal_cancer_flowchart.png"), quality=95)

    # Matrix Table
    w, h = 1400, 600
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1380, 75)], fill="#b91c1c")
    draw.text((700, 45), "大腸がん vs 悪性リンパ腫 vs 大腸ポリープ 比較鑑別表", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [("疾患名", 20, 300), ("壁肥厚・層構造", 300, 660), ("内部エコー・血流", 660, 1020), ("超音波鑑別の決定打", 1020, 1380)]
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#991b1b")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("大腸がん\n(Adenocarcinoma)", "全周性不整壁肥厚 (>5mm)\n5層構造の完全断裂破壊", "不均一低エコー\n腫瘍内豊富血流 (Hyper)", "Apple-core Sign ＋ 狭窄\n所属リンパ節腫大"),
        ("悪性リンパ腫\n(Malignant Lymphoma)", "著明な全周性壁肥厚 (>15mm)\n層構造完全消失", "極めて均一な低エコー\n(無エコー様) / 腔拡張", "壁は極めて厚いが管腔閉塞を\n伴いにくい (Aneurysmal)"),
        ("大腸ポリープ\n(Adenoma/Polyp)", "壁全体の肥厚なし\n有茎性/無茎性腫瘤", "均一等～高エコー\n茎部に血流入流線", "10mm未満は管腔内突起\n層構造保持")
    ]
    cur_y = 145
    row_h = 135
    for i, (dis, wall, dopp, pnt) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#fff5f5"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        draw.rectangle([(20, cur_y), (300, cur_y + row_h)], outline="#cbd5e1", width=2)
        d_lines = dis.split('\n')
        draw.text((160, cur_y + 45), d_lines[0], fill="#b91c1c", font=font_large, anchor="mm")
        draw.text((160, cur_y + 90), d_lines[1], fill="#b91c1c", font=font_mid, anchor="mm")
        
        draw.rectangle([(300, cur_y), (660, cur_y + row_h)], outline="#cbd5e1", width=2)
        w_lines = wall.split('\n')
        draw.text((480, cur_y + 45), w_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((480, cur_y + 90), w_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(660, cur_y), (1020, cur_y + row_h)], outline="#cbd5e1", width=2)
        dp_lines = dopp.split('\n')
        draw.text((840, cur_y + 45), dp_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((840, cur_y + 90), dp_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(1020, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        p_lines = pnt.split('\n')
        draw.text((1200, cur_y + 45), p_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((1200, cur_y + 90), p_lines[1], fill="#334155", font=font_mid, anchor="mm")
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#b91c1c", width=3)
    img.save(os.path.join(img_dir, "colorectal_cancer_matrix_table.png"), quality=95)

# 3. IBD Images
def make_ibd_images():
    # Flowchart
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#047857")
    draw.text((550, 45), "炎症性腸疾患 (IBD: UC vs CD) 超音波鑑別フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#d1fae5", outline="#047857", width=3)
    draw.text((550, 125), "慢性腹痛・粘血便・下痢・若年者発症", fill="#065f46", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#047857", width=3)
    draw.text((550, 215), "【 4大超音波鑑別サイン 】", fill="#065f46", font=font_large, anchor="mm")
    
    steps = [
        ("1. 病変の分布パターン", "UC: 直腸からの連続性病変  /  CD: 回盲部中心の非連続性跳躍病変", "#d1fae5", "#065f46"),
        ("2. 壁肥厚の主座層", "UC: 粘膜～粘膜下層 (第1～3層) 中心 /  CD: 全層性 (第1～5層) 極厚", "#dbeafe", "#1e40af"),
        ("3. Comb Sign (歯梳きサイン)", "CD特有: 腸間膜穿通血管が櫛の歯状に平行拡張・活動性血管怒張", "#fef3c7", "#b45309"),
        ("4. Fat Wrapping ( Creeping Fat )", "CD特有: 炎症腸管周囲を肥厚高エコー脂肪織が包み込む像", "#fee2e2", "#b91c1c")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "ibd_flowchart.png"), quality=95)

    # Matrix Table
    w, h = 1400, 720
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1380, 75)], fill="#047857")
    draw.text((700, 45), "潰瘍性大腸炎 (UC) vs クローン病 (CD) 4大比較マトリックス", fill="#ffffff", font=font_title, anchor="mm")
    
    cols = [("評価項目", 20, 300), ("潰瘍性大腸炎 (UC)", 300, 660), ("クローン病 (Crohn's: CD)", 660, 1020), ("超音波鑑別のポイント", 1020, 1380)]
    y = 90
    draw.rectangle([(20, y), (1380, y + 55)], fill="#065f46")
    for name, x1, x2 in cols:
        draw.rectangle([(x1, y), (x2, y + 55)], outline="#ffffff", width=2)
        draw.text(((x1 + x2) // 2, y + 28), name, fill="#ffffff", font=font_large, anchor="mm")
        
    data = [
        ("病変の連続性・部位", "直腸から口側へ連続的\n大腸全域に及ぶ", "回盲部好発・非連続的\n跳躍病変 (Skip Lesions)", "病変の分布パターンが決定打"),
        ("壁肥厚の主座層", "粘膜～粘膜下層 (第1～3層)\n中心の肥厚", "全層性肥厚 (第1～5層)\n壁厚 > 5.0～10.0 mm", "CDは全層が極厚に肥厚する"),
        ("腸管外・血管サイン", "腸管外変化は乏しい\n鉛管像 (Lead-pipe)", "Comb Sign (血管怒張) ＋\nFat Wrapping (脂肪被覆)", "CD特有の腸管外サイン"),
        ("合併症 (瘻孔・膿瘍)", "合併しにくい\n(中毒性巨大結腸症)", "瘻孔 (Fistula)・狭窄 ＋\n腹腔内膿瘍形成率が高い", "CDは穿孔・瘻孔を頻発する")
    ]
    cur_y = 145
    row_h = 125
    for i, (item, uc, cd, pnt) in enumerate(data):
        bg_c = "#ffffff" if i % 2 == 0 else "#f0fdf4"
        draw.rectangle([(20, cur_y), (1380, cur_y + row_h)], fill=bg_c)
        draw.rectangle([(20, cur_y), (300, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((160, cur_y + row_h // 2), item, fill="#047857", font=font_large, anchor="mm")
        
        draw.rectangle([(300, cur_y), (660, cur_y + row_h)], outline="#cbd5e1", width=2)
        u_lines = uc.split('\n')
        draw.text((480, cur_y + 40), u_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((480, cur_y + 85), u_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(660, cur_y), (1020, cur_y + row_h)], outline="#cbd5e1", width=2)
        c_lines = cd.split('\n')
        draw.text((840, cur_y + 40), c_lines[0], fill="#334155", font=font_mid, anchor="mm")
        draw.text((840, cur_y + 85), c_lines[1], fill="#334155", font=font_mid, anchor="mm")
        
        draw.rectangle([(1020, cur_y), (1380, cur_y + row_h)], outline="#cbd5e1", width=2)
        draw.text((1200, cur_y + row_h // 2), pnt, fill="#334155", font=font_mid, anchor="mm")
        cur_y += row_h

    draw.rectangle([(20, 90), (1380, cur_y)], outline="#047857", width=3)
    img.save(os.path.join(img_dir, "ibd_matrix_table.png"), quality=95)

# 4. Intussusception, Ischemic Colitis, Diverticulitis Flowcharts
def make_remaining_flowcharts():
    # Intussusception
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#c2410c")
    draw.text((550, 45), "腸重積症 (Intussusception) 小児急腹症 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#ffedd5", outline="#c2410c", width=3)
    draw.text((550, 125), "乳幼児 突然の激痛間欠痛 ＋ イチゴジャム状便", fill="#9a3412", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#c2410c", width=3)
    draw.text((550, 215), "【 3大決定超音波サイン ＆ 虚血判定 】", fill="#9a3412", font=font_large, anchor="mm")
    
    steps = [
        ("1. 短軸像: Target Sign (多重同心円像)", "重なる腸管壁がドーナツ状の同心円リング像を呈する", "#ffedd5", "#9a3412"),
        ("2. 長軸像: Pseudokidney Sign (偽腎像)", "重なる多層腸管壁が長軸描出で腎臓類似像を呈する", "#fed7aa", "#9a3412"),
        ("3. カラードプラ血流判定 (Ischemia)", "壁内血流あり ➔ 高圧灌腸復元可能  /  無血流 ➔ 絞扼壊死疑い", "#fee2e2", "#991b1b"),
        ("4. 先頭病変 (Leading Point) の確認", "年長児・成人例では Meckel憩室 / ポリープ / 腫瘍の有無を確認", "#dcfce7", "#15803d")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "intussusception_flowchart.png"), quality=95)

    # Ischemic Colitis
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#7c2d12")
    draw.text((550, 45), "虚血性大腸炎 (Ischemic Colitis) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#ffedd5", outline="#7c2d12", width=3)
    draw.text((550, 125), "突然の左下腹部痛 ＋ 水様下痢 ＋ 新鮮下血", fill="#7c2d12", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#7c2d12", width=3)
    draw.text((550, 215), "【 4大特徴超音波サイン 】", fill="#7c2d12", font=font_large, anchor="mm")
    
    steps = [
        ("1. 左半大腸の長状壁肥厚 (Segmental Thickening)", "降状～S状結腸に 10～20cm以上の連続性壁肥厚 (>5.0mm)", "#ffedd5", "#7c2d12"),
        ("2. Thumb-printing Sign (親指圧痕像)", "粘膜下層の高度浮腫・出血による親指で押したような波状壁膨隆", "#fed7aa", "#7c2d12"),
        ("3. 壁内血流動態変化 (Doppler Shift)", "初期: 血流減少・消失  ➔  再灌流期: 著明な充血 (Hyperemia)", "#fee2e2", "#991b1b"),
        ("4. 壊死型 (Gangrenous Form) の鑑別", "壁内ガス像 (Pneumatosis) ＋ 門脈ガス (PV Gas) 陽性は超緊急", "#fee2e2", "#991b1b")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "ischemic_colitis_flowchart.png"), quality=95)

    # Diverticulitis
    w, h = 1100, 800
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 15), (1080, 75)], fill="#b45309")
    draw.text((550, 45), "大腸憩室炎 (Colonic Diverticulitis) 超音波診断フロー", fill="#ffffff", font=font_title, anchor="mm")
    
    draw.rectangle([(250, 95), (850, 155)], fill="#fef3c7", outline="#b45309", width=3)
    draw.text((550, 125), "右下腹部/左下腹部 局所痛 ＋ CRP・白血球高値", fill="#b45309", font=font_large, anchor="mm")
    draw.line([(550, 155), (550, 185)], fill="#64748b", width=3)
    
    draw.rectangle([(30, 185), (1070, 765)], fill="#ffffff", outline="#b45309", width=3)
    draw.text((550, 215), "【 4大決定超音波サイン 】", fill="#b45309", font=font_large, anchor="mm")
    
    steps = [
        ("1. 腸管壁外へ突出する憩室 (Outpouching)", "壁外へ突起する 5～10mm の嚢状構造 (糞石高エコー伴う)", "#fef3c7", "#b45309"),
        ("2. Inflamed Fat Sign (周囲脂肪織高エコー化)", "憩室周囲脂肪織が強い炎症で高輝度化 ＋ 限局性探触子圧痛", "#fde68a", "#b45309"),
        ("3. 局所的腸管壁肥厚 (Segmental Wall Thickening)", "憩室直近の大腸壁が局所的に > 4.0mm 肥厚", "#fed7aa", "#9a3412"),
        ("4. 穿孔・腹腔内膿瘍 (Abscess) の確認", "憩室周囲の遊離エアー (Free Air) ＋ 液体貯留・膿瘍形成", "#fee2e2", "#991b1b")
    ]
    y = 250
    for title, desc, bg_c, text_c in steps:
        draw_two_line_box(draw, (60, y, 1040, y + 110), bg_c, text_c, title, desc, title_color=text_c)
        y += 125
    img.save(os.path.join(img_dir, "diverticulitis_flowchart.png"), quality=95)
    print("Generated all GI PNG Images Successfully!")

make_colorectal_images()
make_ibd_images()
make_remaining_flowcharts()
