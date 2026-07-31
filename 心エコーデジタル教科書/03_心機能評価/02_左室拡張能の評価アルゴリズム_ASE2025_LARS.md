---
title: 左室拡張能の評価アルゴリズム (ASE 2025 LARS対応)
tags: [心機能評価, 拡張能, E/e', LARS, LAVI, HFpEF, カスケードフロー]
aliases: [Diastolic Function, LARS, E/e', LAP]
date_created: 2026-07-31
last_modified: 2026-07-31
reference_guideline: ASE 2025 Diastolic Function Guidelines Update
---

# 左室拡張能の評価アルゴリズム (ASE 2025 LARS対応)

本ページでは、臨床現場で迷わず数秒で左室拡張能障害（Diastolic Dysfunction）および左房圧（LAP）上昇を判定できるよう、**ASE 2025年最新ガイドラインに準拠した「カスケード式（段階的分岐）フロー」** で整理しています。

---

## 1. 判定に用いる指標とカットオフ値

まず以下の計測項目を確認します。

| 指標 | カットオフ値 | 意味 |
| :--- | :--- | :--- |
| **中隔側 e'** | $< 7$ cm/s | 心筋弛緩障害 |
| **側壁側 e'** | $< 10$ cm/s | 心筋弛緩障害 |
| **平均 E/e' 比** | $> 14.0$ | 左房圧上昇 |
| **★ LARS** (ASE 2025新導入) | $\le 18.0$ % | 左房機能低下 |
| **LAVI** | $> 34$ mL/m² | 慢性左房圧負荷 |
| **TR Vmax** | $> 2.8$ m/s | 肺動脈圧上昇 |
| **E/A 比** | $\le 0.8$ または $\ge 2.0$ | 充満パターン異常 |

---

## 2. ■ LVEF が正常の場合の左室拡張不全の診断 (カスケード A)

```mermaid
graph TD
    CRIT["【判定に用いる4指標】
    ① E/e'（平均e'）> 14
    ② 中隔側 e' < 7 cm/s あるいは
       側壁側 e' < 10 cm/s
    ③ TR 血流速度 > 2.8 m/s
    ④ LAVI > 34 mL/m²
    ★ LARS ≤ 18%（ASE2025追加）"]

    CRIT --> R0["0〜1つ陽性"]
    CRIT --> R2["2〜3つ陽性"]
    CRIT --> R4["4〜5つ陽性"]

    R0 --> N["✅ 左室拡張能正常"]
    R2 --> I["⚠️ 判定不能<br>（追加検査を考慮）"]
    R4 --> D["❌ 左室拡張不全"]

    style CRIT fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style R0 fill:#f5f5f5,stroke:#999
    style R2 fill:#f5f5f5,stroke:#999
    style R4 fill:#f5f5f5,stroke:#999
    style N fill:#d4edda,stroke:#28a745,stroke-width:2px
    style I fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style D fill:#f8d7da,stroke:#dc3545,stroke-width:2px
```

> [!IMPORTANT]
> **★ ASE 2025年改訂のポイント**
> ASE 2016では4指標だったが、**LARS ($\le 18\%$) が第5の指標として追加** された。
> LARS陽性が加わることで、従来「判定不能」だった症例の多くが「拡張不全」と確定診断できるようになった。

---

## 3. ■ LVEF 低下例と LVEF 正常の拡張不全例における左房圧と重症度の評価 (カスケード B)

```mermaid
graph TD
    TOP["僧帽弁口血流速度波形<br>（E/A 比 と E波速度を確認）"]

    TOP --> EA_LOW["E/A ≤ 0.8<br>かつ E ≤ 50 cm/s"]
    TOP --> EA_MID["E/A ≤ 0.8 かつ E > 50 cm/s<br>あるいは E/A 0.8 〜 2"]
    TOP --> EA_HIGH["E/A ≥ 2"]

    EA_LOW --> G1A["✅ 左房圧正常<br>Grade Ⅰ の拡張不全"]

    EA_MID --> CRIT2["【3指標を確認】
    ① E/e'（平均e'）> 14
    ② TR 血流速度 > 2.8 m/s
    ③ LAVI > 34 mL/m²
    ★ LARS ≤ 18%（ASE2025追加）"]

    CRIT2 --> C_NO["2〜3つ陰性"]
    CRIT2 --> C_UNABLE["2項目しか評価<br>できないとき<br>→ 1陽性1陰性"]
    CRIT2 --> C_YES["2〜3つ陽性"]

    C_NO --> G1B["✅ 左房圧正常<br>Grade Ⅰ の拡張不全"]
    C_UNABLE --> GX["🔲 左房圧と<br>拡張能は評価不能"]
    C_YES --> G2["⚠️ 左房圧上昇<br>Grade Ⅱ の拡張不全"]

    EA_HIGH --> G3["❌ 左房圧上昇<br>Grade Ⅲ の拡張不全"]

    G1A --> NOTE["有症状であれば<br>冠動脈疾患を考慮<br>拡張期負荷試験を行う"]

    style TOP fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style EA_LOW fill:#f5f5f5,stroke:#999
    style EA_MID fill:#f5f5f5,stroke:#999
    style EA_HIGH fill:#f5f5f5,stroke:#999
    style CRIT2 fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style C_NO fill:#f5f5f5,stroke:#999
    style C_UNABLE fill:#f5f5f5,stroke:#999
    style C_YES fill:#f5f5f5,stroke:#999
    style G1A fill:#cce5ff,stroke:#004085,stroke-width:2px
    style G1B fill:#cce5ff,stroke:#004085,stroke-width:2px
    style GX fill:#e2e3e5,stroke:#6c757d,stroke-width:2px
    style G2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style G3 fill:#f8d7da,stroke:#dc3545,stroke-width:2px
    style NOTE fill:#d4edda,stroke:#28a745
```

---

## 4. 判定指標のポイントまとめ

> [!TIP]
> **LARS (左房リザーバーストレイン) とは？**
> 左房が収縮期に伸びる最大の割合（%）を 2D Speckle Tracking で計測したもの。
> 正常は **$> 18\%$**。$\le 18\%$ は左房コンプライアンスの低下＝左房圧上昇を強く示唆。
> E/e' が「中間値」で判断に迷うとき、LARSが最も鋭敏に左房圧を反映する。

> [!WARNING]
> **特殊病態での注意点**
> - **心房細動 (Af)**: A波が消失するため E/A 評価不可。E/e'・LARS・TR Vmax の3指標で判断。
> - **重症 MR**: E波が偽高値になりE/e'が過大評価されるため、**LARS** を優先して評価する。
> - **僧帽弁輪石灰化 (MAC)**: 弁輪の機械的拘束でe'が低下するため、E/e'が過大評価されやすい。
