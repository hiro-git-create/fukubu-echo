import os
import shutil

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Completely delete existing vault directory to wipe out garbage/garbled filenames
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)

os.makedirs(base_dir, exist_ok=True)

# Content Dictionary with Clean UTF-8 Strings
moc_content = """# 腹部超音波検査 教科書 (Obsidian Vault MOC)

> [!NOTE] 概要
> 本ドキュメントは腹部超音波検査（腹部エコー）の標準的な走査法、各臓器の解剖・描出法、主要疾患の超音波診断プロトコル、および実践的な計測値を網羅したインタラクティブ教科書です。

---

## 🗺️ コンテンツマップ (Map of Content)

### 1. 🔰 基本事項・走査法
* [[01_基本事項・走査法/基礎知識・プローブ選択|基礎知識・プローブ選択]]
* [[01_基本事項・走査法/腹部基本描出断面・走査手順|腹部基本描出断面・走査手順]]

### 2. 🫀 臓器別解剖と標準描出
* [[02_臓器別解剖と標準描出/肝臓_解剖と描出法|肝臓：解剖（Couinaud分類）と描出法]]
* [[02_臓器別解剖と標準描出/胆嚢・胆管_解剖と描出法|胆嚢・胆管：解剖と描出法]]
* [[02_臓器別解剖と標準描出/膵臓_解剖と描出法|膵臓：解剖と描出法]]
* [[02_臓器別解剖と標準描出/腎臓・副腎_解剖と描出法|腎臓・副腎：解剖と描出法]]
* [[02_臓器別解剖と標準描出/消化管_解剖と描出法|消化管：層構造と標準描出]]
* [[02_臓器別解剖と標準描出/腹部血管・後腹膜_解剖と描出法|腹部血管・後腹膜：解剖と描出法]]

### 3. 🩺 疾患別超音波診断プロトコル

#### 🟢 肝臓領域 (Liver Diseases)
* [[03_疾患別超音波所見/肝臓_脂肪肝|脂肪肝 (Fatty Liver)]]
* [[03_疾患別超音波所見/肝臓_肝硬変|肝硬変 (Liver Cirrhosis)]]
* [[03_疾患別超音波所見/肝臓_肝細胞がん|肝細胞がん (HCC)]]
* [[03_疾患別超音波所見/肝臓_肝血管腫|肝血管腫 (Hemangioma)]]
* [[03_疾患別超音波所見/肝臓_転移性肝がん|転移性肝がん (Metastatic Tumor)]]

#### 🟡 胆道領域 (Biliary Diseases)
* [[03_疾患別超音波所見/胆道_胆石症|胆石症 (Gallstones)]]
* [[03_疾患別超音波所見/胆道_急性・慢性胆嚢炎|急性・慢性胆嚢炎 (Cholecystitis)]]
* [[03_疾患別超音波所見/胆道_胆嚢ポリープ・腺筋腫症|胆嚢ポリープ・胆嚢腺筋腫症 (ADM)]]

#### 🔵 膵臓領域 (Pancreatic Diseases)
* [[03_疾患別超音波所見/膵臓_膵がん|膵がん (Pancreatic Carcinoma)]]
* [[03_疾患別超音波所見/膵臓_膵嚢胞性腫瘍|膵嚢胞性腫瘍 (IPMN)]]

#### 🟣 腎・泌尿器領域 (Renal & Urinary Diseases)
* [[03_疾患別超音波所見/腎臓_水腎症|水腎症 (Hydronephrosis)]]

#### 🟠 消化管・血管・その他 (GI & Vascular Diseases)
* [[03_疾患別超音波所見/消化管_急性虫垂炎|急性虫垂炎 (Acute Appendicitis)]]
* [[03_疾患別超音波所見/血管_腹部大動脈瘤|腹部大動脈瘤 (AAA)]]
* [[03_疾患別超音波所見/血管_ナットクラッカー症候群|ナットクラッカー症候群 (Nutcracker Syndrome)]]

### 4. 📐 実践スクリーニング・計測
* [[04_実践スクリーニング・計測/腹部超音波計測値一覧|腹部超音波標準計測値一覧]]
* [[04_実践スクリーニング・計測/スクリーニングチェックリスト|スクリーニング検査チェックリスト]]
"""

probe_content = """# 基礎知識・プローブ選択

> [!NOTE] 目的
> 腹部超音波検査を安全かつ的確に行うための、装置の基本設定・使用プローブ（探触子）の選択および画質調整のポイントについて解説します。

---

## 1. 使用プローブ（探触子）の特徴と使い分け

| プローブ種類 | 周波数帯域 | 形状・視野 | 主な用途・適応 | 特徴・長所・短所 |
| :--- | :--- | :--- | :--- | :--- |
| **コンベックス型** (Convex) | 3.5 ～ 5.0 MHz | 扇状 | 腹部全般（肝・胆・膵・脾・腎・大血管） | **腹部検査の第一選択**。広範囲の深部観察に適する。 |
| **リニア型** (Linear) | 7.5 ～ 12.0 MHz | 矩形 | 消化管（虫垂・憩室）、腹壁、浅部病変 | 高解剖学的分解能。深部の観察には不向き。 |
| **セクター型** (Sector) | 2.5 ～ 3.5 MHz | 扇状 | 肋間アプローチ（肝縦断・肝頂部） | 狭い音響窓からの観察に優れる。 |
"""

scan_content = """# 腹部基本描出断面・走査手順

> [!NOTE] 概要
> 腹部超音波スクリーニング検査における標準的な走査手順と代表的描出断面について解説します。

---

## 1. 代表的描出断面
1. **上腹部正中縦断像**: 腹部大動脈 (Aorta)、SMA、左肝葉
2. **上腹部横断像**: 膵臓、脾静脈 (SV)
3. **右肋骨下斜断像**: 肝静脈3本描出像 (Couinaud分類)
4. **右肋間走査**: 胆嚢・胆管長軸像、肝腎コントラスト
"""

liver_content = """# 肝臓：解剖（Couinaud分類）と描出法

> [!NOTE] 概要
> 肝臓の解剖学的区域分類（Couinaud分類）と各区域を同定・描出するための血管ランドマークについて解説します。

---

## 1. 肝解剖とCouinaudの区域分類 (S1 ～ S8)
- **中肝静脈 (MHV)**: 肝臓を「左葉」と「右葉」に分ける。
- **左肝静脈 (LHV)**: 左葉を「外側区 (S2/S3)」と「内側区 (S4)」に分ける。
- **右肝静脈 (RHV)**: 右葉を「前区 (S5/S8)」と「後区 (S6/S7)」に分ける。
"""

gb_content = """# 胆嚢・胆管：解剖と描出法

> [!NOTE] 概要
> 胆嚢・胆管の立体構造解剖、標準的計測方法および描出テクニックを解説します。

---

## 1. 標準計測値
- **胆嚢壁厚**: 3.0 mm 以下
- **総胆管径**: 6.0 mm 以下
"""

pancreas_content = """# 膵臓：解剖と描出法

> [!NOTE] 概要
> 膵臓のエコー描出における血管ランドマーク（SMA, SV）と描出困難例への対応テクニックを解説します。

---

## 1. 主膵管 (MPD) の計測
- **正常径**: 2.0 mm 以下
"""

kidney_content = """# 腎臓・副腎：解剖と描出法

> [!NOTE] 概要
> 腎臓の解剖構造（CEC・皮質・髄質）と標準計測値について解説します。

---

## 1. 腎計測
- **長径**: 9.0 ～ 11.5 cm
- **実質厚**: 1.5 ～ 2.0 cm
"""

gi_content = """# 消化管：層構造と標準描出

> [!NOTE] 概要
> 消化管の超音波5層構造と壁厚評価について解説します。

---

## 1. 5層構造
- 第1層 (高エコー): 粘膜境界
- 第2層 (低エコー): 粘膜層
- 第3層 (高エコー): 粘膜下層 (SM)
- 第4層 (低エコー): 固有筋層 (MP)
- 第5層 (高エコー): 漿膜層 (Serosa)
"""

vessels_content = """# 腹部血管・後腹膜：解剖と描出法

> [!NOTE] 概要
> 腹部大動脈 (Aorta)、下大静脈 (IVC)、門脈の計測と評価について解説します。
"""

fatty_content = """# 脂肪肝 (Fatty Liver) 診断プロトコル

> [!NOTE] 概要
> 脂肪肝の診断基準、Grade分類、および局所性脂肪回避 (Focal Sparing) の鑑別法について解説します。

---

## 1. 重症度分類
- **Mild**: 肝腎コントラスト軽度陽性
- **Moderate**: 肝深部減衰あり、門脈壁エコー不鮮明
- **Severe**: 肝深部描出不能、横隔膜遮蔽
"""

lc_content = """# 肝硬変 (Liver Cirrhosis) 診断プロトコル

> [!NOTE] 概要
> 肝表面凹凸、尾状葉/右葉比 (C/RL > 0.65)、門脈高血圧症所見（脾腫 ≧ 10cm）について解説します。
"""

hcc_content = """# 肝細胞がん (Hepatocellular Carcinoma: HCC) 診断プロトコル

> [!NOTE] 概要
> 結節型HCCのHalo sign、モザイクパターン、造影エコー所見について解説します。
"""

hem_content = """# 肝血管腫 (Hepatic Hemangioma) 診断プロトコル

> [!NOTE] 概要
> 境界明瞭な高エコー結節、Marginal strong echo sign、後方エコー増強について解説します。
"""

meta_content = """# 転移性肝がん (Metastatic Liver Tumor) 診断プロトコル

> [!NOTE] 概要
> Target sign / Bull's eye sign、多発性結節の特徴について解説します。
"""

stone_content = """# 胆石症 (Gallstones) 診断プロトコル

> [!NOTE] 概要
> 超音波三徴（高エコー、音響陰影、移動性）、WES sign、胆泥との鑑別について解説します。
"""

chole_content = """# 急性・慢性胆嚢炎 (Cholecystitis) 診断プロトコル

> [!NOTE] 概要
> 胆嚢壁肥厚 (> 3mm)、二重壁像 (Double Wall Sign)、超音波 Murphy 徴候について解説します。
"""

poly_content = """# 胆嚢ポリープ・胆嚢腺筋腫症 (ADM) 診断プロトコル

> [!NOTE] 概要
> 10mm以上の手術検討基準、ADMのComet-tail artifactについて解説します。
"""

panc_ca_content = """# 膵がん (Pancreatic Carcinoma) 診断プロトコル

> [!NOTE] 概要
> 直接腫瘤像、主膵管拡張 (> 2mm)、ダブルダクトサイン (Double Duct Sign) について解説します。
"""

ipmn_content = """# 膵嚢胞性腫瘍 (IPMN) 診断プロトコル

> [!NOTE] 概要
> 分枝型・主膵管型IPMN、壁結節 (≧ 5mm) などのハイリスク所見について解説します。
"""

hydro_content = """# 水腎症 (Hydronephrosis) 診断プロトコル

> [!NOTE] 概要
> SFU Grade 1 ～ 4 分類、尿管閉塞部位同定ステップについて解説します。
"""

app_content = """# 急性虫垂炎 (Acute Appendicitis) 診断プロトコル

> [!NOTE] 概要
> 虫垂外径 (> 6mm)、圧迫非消退、期別鑑別（カタル性/蜂窩織炎性/壊疽性）について解説します。
"""

aaa_content = """# 腹部大動脈瘤 (AAA) 診断プロトコル

> [!NOTE] 概要
> 外径 3.0cm以上の定義、破裂リスク (≧ 5.0cm)、真性/偽性/解離の鑑別について解説します。
"""

nut_content = """# ナットクラッカー症候群 (Nutcracker Syndrome) 診断プロトコル

> [!NOTE] 概要
> SMA分岐角 (< 35°)、径比 Dh/De (> 4.0)、流速比 Ve/Vh (> 4.0) について解説します。
"""

meas_content = """# 腹部超音波標準計測値一覧

| 対象 | カットオフ値 |
| :--- | :--- |
| **胆嚢壁厚** | ≦ 3.0 mm |
| **総胆管径** | ≦ 6.0 mm |
| **主膵管径** | ≦ 2.0 mm |
| **腎長径** | 9.0 ～ 11.5 cm |
| **腹部大動脈** | < 2.0 cm |
| **虫垂径** | ≦ 6.0 mm |
"""

chk_content = """# スクリーニング検査チェックリスト

- [ ] **肝臓**: 表面、輝度、S1～S8全域
- [ ] **胆嚢**: 結石、壁厚 (3mm以下)
- [ ] **膵臓**: 主膵管 (2mm以下)
- [ ] **腎臓**: 水腎症の有無
"""

files_map = {
    "00_MOC_目次.md": moc_content,
    "01_基本事項・走査法/基礎知識・プローブ選択.md": probe_content,
    "01_基本事項・走査法/腹部基本描出断面・走査手順.md": scan_content,
    "02_臓器別解剖と標準描出/肝臓_解剖と描出法.md": liver_content,
    "02_臓器別解剖と標準描出/胆嚢・胆管_解剖と描出法.md": gb_content,
    "02_臓器別解剖と標準描出/膵臓_解剖と描出法.md": pancreas_content,
    "02_臓器別解剖と標準描出/腎臓・副腎_解剖と描出法.md": kidney_content,
    "02_臓器別解剖と標準描出/消化管_解剖と描出法.md": gi_content,
    "02_臓器別解剖と標準描出/腹部血管・後腹膜_解剖と描出法.md": vessels_content,
    "03_疾患別超音波所見/肝臓_脂肪肝.md": fatty_content,
    "03_疾患別超音波所見/肝臓_肝硬変.md": lc_content,
    "03_疾患別超音波所見/肝臓_肝細胞がん.md": hcc_content,
    "03_疾患別超音波所見/肝臓_肝血管腫.md": hem_content,
    "03_疾患別超音波所見/肝臓_転移性肝がん.md": meta_content,
    "03_疾患別超音波所見/胆道_胆石症.md": stone_content,
    "03_疾患別超音波所見/胆道_急性・慢性胆嚢炎.md": chole_content,
    "03_疾患別超音波所見/胆道_胆嚢ポリープ・腺筋腫症.md": poly_content,
    "03_疾患別超音波所見/膵臓_膵がん.md": panc_ca_content,
    "03_疾患別超音波所見/膵臓_膵嚢胞性腫瘍.md": ipmn_content,
    "03_疾患別超音波所見/腎臓_水腎症.md": hydro_content,
    "03_疾患別超音波所見/消化管_急性虫垂炎.md": app_content,
    "03_疾患別超音波所見/血管_腹部大動脈瘤.md": aaa_content,
    "03_疾患別超音波所見/血管_ナットクラッカー症候群.md": nut_content,
    "04_実践スクリーニング・計測/腹部超音波計測値一覧.md": meas_content,
    "04_実践スクリーニング・計測/スクリーニングチェックリスト.md": chk_content,
}

for rel_path, content in files_map.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    # Save using UTF-8 encoding
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

print("Pristine vault creation SUCCESSFUL!")
