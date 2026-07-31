---
title: 左室拡張能の評価アルゴリズム (ASE 2025 LARS対応)
tags: [心機能評価, 拡張能, E/e', LARS, LAVI, HFpEF, カスケードフロー]
aliases: [Diastolic Function, LARS, E/e', LAP]
date_created: 2026-07-31
last_modified: 2026-07-31
reference_guideline: ASE 2025 Diastolic Function Guidelines Update
---

# 左室拡張能の評価アルゴリズム (ASE 2025 LARS対応)

臨床現場で迷わず数秒で判定できるよう、**ASE 2025年最新ガイドライン準拠のカスケード式フロー**で整理しています。

---

## 判定に用いる指標とカットオフ値

| 指標 | カットオフ | 意味 |
| :--- | :--- | :--- |
| 中隔側 e' | < 7 cm/s | 心筋弛緩障害 |
| 側壁側 e' | < 10 cm/s | 心筋弛緩障害 |
| 平均 E/e' 比 | > 14.0 | 左房圧上昇 |
| **LARS** (ASE2025新導入) | **≤ 18.0 %** | 左房機能低下 |
| LAVI | > 34 mL/m² | 慢性左房圧負荷 |
| TR Vmax | > 2.8 m/s | 肺動脈圧上昇 |

---

## カスケード A ── LVEF が正常の場合の左室拡張不全の診断

```mermaid
graph TD
    CRIT["① E/e'（平均 e'）> 14<br/>② 中隔側 e' < 7 cm/s または 側壁側 e' < 10 cm/s<br/>③ TR 血流速度 > 2.8 m/s<br/>④ LAVI > 34 mL/m²<br/>⑤ LARS ≤ 18%（ASE 2025 追加）"]
    CRIT --> R01["0〜1つ陽性"]
    CRIT --> R23["2〜3つ陽性"]
    CRIT --> R45["4〜5つ陽性"]
    R01 --> NORM["左室拡張能 正常"]
    R23 --> UNDET["判定不能"]
    R45 --> DD["左室拡張不全"]
    style CRIT fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style NORM fill:#d4edda,stroke:#28a745,stroke-width:2px
    style UNDET fill:#f5f5f5,stroke:#aaa,stroke-width:2px
    style DD fill:#f8d7da,stroke:#dc3545,stroke-width:2px
```

> [!IMPORTANT]
> **ASE 2025 改訂ポイント**
> LARS（≤ 18%）が第5の指標として追加された。これにより従来「判定不能」だった症例の多くが確定診断できるようになった。

---

## カスケード B ── LVEF 低下例 と 拡張不全確定例における左房圧・重症度の評価

```mermaid
graph TD
    TOP["僧帽弁口血流速度波形"]
    TOP --> EA_LOW["E/A ≤ 0.8 かつ E ≤ 50 cm/s"]
    TOP --> EA_MID["E/A ≤ 0.8 かつ E > 50 cm/s<br/>あるいは E/A 0.8〜2"]
    TOP --> EA_HIGH["E/A ≥ 2"]
    EA_LOW --> G1A["左房圧正常<br/>Grade I の拡張不全"]
    EA_HIGH --> G3["左房圧上昇<br/>Grade III の拡張不全"]
    EA_MID --> CRIT2["① E/e'（平均 e'）> 14<br/>② TR 血流速度 > 2.8 m/s<br/>③ LAVI > 34 mL/m²<br/>④ LARS ≤ 18%（ASE 2025 追加）"]
    CRIT2 --> CN["2〜3つ 陰性"]
    CRIT2 --> CU["2項目しか評価できないとき<br/>1陽性・1陰性"]
    CRIT2 --> CP["2〜3つ 陽性"]
    CN --> G1B["左房圧正常<br/>Grade I の拡張不全"]
    CU --> GX["左房圧と<br/>拡張能は評価不能"]
    CP --> G2["左房圧上昇<br/>Grade II の拡張不全"]
    G1A --> NOTE["有症状であれば<br/>冠動脈疾患を考慮<br/>拡張期負荷試験を行う"]
    style TOP fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style CRIT2 fill:#fff3cd,stroke:#f0ad4e,stroke-width:2px
    style G1A fill:#cce5ff,stroke:#004085,stroke-width:2px
    style G1B fill:#cce5ff,stroke:#004085,stroke-width:2px
    style GX fill:#e2e3e5,stroke:#6c757d,stroke-width:2px
    style G2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style G3 fill:#f8d7da,stroke:#dc3545,stroke-width:2px
    style NOTE fill:#d4edda,stroke:#28a745,stroke-width:2px
```

---

## 臨床で3秒で判断するまとめ

| 患者パターン | 使うカスケード | 結論の出し方 |
| :--- | :--- | :--- |
| LVEF正常・呼吸困難（HFpEF疑い） | カスケード A | 5指標中4〜5個陽性 → 拡張不全確定 |
| LVEF低下の心不全（HFrEF） | カスケード B | E/A ≥ 2 → 即 Grade III。中間なら3〜4指標中2個以上陽性 → Grade II |

> [!WARNING]
> **特殊病態での注意点**
> - **心房細動（Af）**: A波がないためE/A評価不可。E/e' > 14・LARS ≤ 18%・TR Vmax > 2.8 m/s の3指標で判断。
> - **重症 MR**: E波が偽高値となりE/e'が過大評価されるため、**LARS** を優先して評価する。
> - **僧帽弁輪石灰化（MAC）**: 弁輪の機械的拘束でe'が低下するため、E/e'は過大評価されやすい。
