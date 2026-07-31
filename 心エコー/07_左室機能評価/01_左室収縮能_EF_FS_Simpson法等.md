---
title: 左室収縮能の評価 (EF, FS, SV)
tags: [収縮能, LVEF, Simpson法, FS]
aliases: [Systolic Function, Ejection Fraction]
date_created: 2026-07-19
last_modified: 2026-07-19
reference_guideline: ASE 2015 Chamber Quantification
---

# 左室収縮能の評価 (LV Systolic Function)

左室の「血液を全身に送り出す力」を評価する指標です。最も代表的な指標が **左室駆出率 (LVEF)** です。

## 1. 左室駆出率 (LVEF: Left Ventricular Ejection Fraction)
左室に拡張期に溜まった血液のうち、何％が収縮期に駆出されたかを示す割合。

- **正常値**: 男性 **≥ 52%**, 女性 **≥ 54%**
- 算出式: `LVEF = (LVEDV - LVESV) / LVEDV × 100`

### 1-1. Simpson法 (Biplane method of disks)
> [!IMPORTANT]
> ガイドラインで推奨されるLVEF計測の第一選択（標準）です。左室の形状変化（局所壁運動異常など）の影響を受けにくい特徴があります。

- **方法**: 
  - 心尖部4腔断面 (AP4) と 2腔断面 (AP2) の両方から、拡張末期 (ED) と収縮末期 (ES) の左室心内膜をトレースして容積 (Volume) を算出する。
- **ピットフォール**:
  - 心尖部の短縮 (Foreshortening): プローブの位置が高すぎると、真の心尖部が描出されず、左室が丸く短く見え容積を過小評価する。
  - 心内膜のトレース時、乳頭筋や肉柱は「内腔」に含めてトレースする（除外しない）。

### 1-2. Teichholz法 (Mモード/2D 径計測からの推定)
- **方法**: PLAXでのLVDdとLVDsの値から、特定の計算式（Teichholz式）を用いて容積とLVEFを「推定」する。
- **ピットフォール**:
  - 局所壁運動異常（虚血性心疾患など）がある場合、計測ライン上の壁運動のみで左室全体の容積を推定するため、実際のLVEFと大きく解離する。現在はあくまでスクリーニングや参考値として用いられる。

## 2. 内径短縮率 (FS: Fractional Shortening)
左室が収縮期に内径を何％縮めたかを示す指標。

- **正常値**: **25 - 43%**
- 算出式: `FS = (LVDd - LVDs) / LVDd × 100`
- **特徴**: 計測が簡便であるが、Teichholz法同様、局所壁運動異常がある場合は全体を反映しない。

## 3. 一回拍出量 (SV: Stroke Volume) と 心拍出量 (CO: Cardiac Output)
左室から大動脈へ実際に駆出された血液の「量」をドプラ法から算出する。

### ドプラ法によるSV算出
- **推奨断面**: 傍胸骨左室長軸断面 (LVOT径)、心尖部5腔断面 (LVOT血流)
- 算出式: `SV = (LVOTd/2)² × π × LVOT-VTI`
  - LVOTd: 左室流出路径 [cm]
  - LVOT-VTI: 左室流出路血流速積分値 [cm]（PWドプラ）
- **正常値**: SV **50 - 100 ml**

### 心拍出量 (CO) の算出
- 算出式: `CO = SV × HR (心拍数) / 1000`
- **正常値**: CO **4.0 - 8.0 L/min**

> [!TIP]
> 弁膜症の評価（大動脈弁狭窄症の連続の式など）では、この LVOT-VTI を用いたSVの正確な計測が極めて重要になります。LVOT径のわずかな誤差が二乗されて影響するため、2D画像のゲイン設定と正確な内径計測が求められます。
