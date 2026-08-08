---
title: 局所壁運動異常 (RWMA) と WMSI の評価
tags: [壁運動評価, RWMA, WMSI, 壁厚増加率, 虚血性心疾患]
aliases: [RWMA, Wall Motion Score Index, WMSI]
date_created: 2026-07-31
last_modified: 2026-07-31
reference_guideline: ASE 2015 Chamber Quantification
---

# 局所壁運動異常 (RWMA) と WMSI の評価

虚血性心疾患（狭心症・心筋梗塞）の超音波診断において、心筋の局所的な動態と収縮期壁厚増加率を判定する **局所壁運動異常 (Regional Wall Motion Abnormality: RWMA)** の評価は最重要項目です。

---

## 1. 壁運動スコア (Wall Motion Score: WMS) の判定基準

評価は「心筋の内側への移動 (Inward displacement)」だけでなく、**「収縮期の心筋壁厚の増加 (Systolic Wall Thickening)」** を総合して判定します。


![02_局所壁運動異常_RWMA_とWMSIの評価 比較・診断判定表 (1)](../../images/auto_table_02_局所壁運動異常_RWMA_とWMSIの評価_1.png)


---

## 2. 壁運動スコア指標 (WMSI: Wall Motion Score Index) の算出

左室全体の壁運動異常の広がり（虚血・梗塞範囲）を定量化する指標です。

$$\text{WMSI} = \frac{\sum (\text{評価できた全セグメントの WMS スコア})}{\text{評価セグメント数 (16 または 17)}}$$

- **正常値**: **$\text{WMSI} = 1.0$** （全セグメントがスコア1）
- **軽度〜中等度異常**: $\text{WMSI} = 1.1 \sim 1.6$
- **高度広範障害**: **$\text{WMSI} > 1.7 \sim 2.0$** （予後不良、ポンプ不全・心不全リスク極大）

---

## 3. 虚血性心疾患と非虚血性疾患の鑑別ポイント

> [!IMPORTANT]
> **「冠動脈支配領域に一致しているか」が最大の鑑別点**です。

```mermaid
flowchart TD
    A["局所壁運動異常 RWMA を認めた"] --> B{"単一の冠動脈支配領域に一致するか?"}
    
    B -- 一致する (LAD/LCx/RCA領域) --> C["★ 虚血性心疾患: 急性心筋梗塞 / 狭心症"]
    B -- 一致しない (支配領域を無視) --> D{"パターンを確認"}
    
    D -- 心尖部無収縮 + 心基部過収縮 --> E["たこつぼ心筋症 (Takotsubo)"]
    D -- 心室中隔の奇異運動 (Septal Flash) --> F["左脚ブロック (LBBB) / ペースメーカー"]
    D -- 散在性・非典型的異常 --> G["心筋炎 / 心アミロイドーシス"]
```

### 1) たこつぼ心筋症 (Takotsubo Cardiomyopathy)
- **特徴**: ストレス等を契機に発症。単一冠動脈領域を超えて**心尖部〜中間部が広範に無運動 (Akinesis)** となり、**心基部のみが過収縮 (Hyperkinesis)** して「たこつぼ」状の形態を呈します。冠動脈造影で有意狭窄を認めないのが特徴。

### 2) 左脚ブロック (LBBB) および 右室ペースメーカー刺激
- **特徴**: 電気伝導の遅延により、心室中隔が収縮早期に右室側へペコッと落ち込む動作（**Septal Flash / 奇異性中隔運動**）を示します。これは虚血（RWMA）ではなく**非同期的収縮 (Dyssynchrony)** によるものです。

### 3) 急性心筋梗塞 (AMI) における壁運動の変化
- 虚血発症後**数秒**で Hypokinesis ➔ Akinesis へ移行します。
- 慢性期に壁厚が薄く輝度が高くなっている (Thinning & Bright) 場合は、透壁性の古い梗塞巣（瘢痕化）を意味します。
