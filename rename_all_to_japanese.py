import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Rename 01_basics to Japanese
b_dir = os.path.join(base_dir, "01_basics")
if os.path.exists(b_dir):
    new_b_dir = os.path.join(base_dir, "01_基本事項・走査法")
    os.rename(b_dir, new_b_dir)

# Rename 02_anatomy to Japanese
a_dir = os.path.join(base_dir, "02_anatomy")
if os.path.exists(a_dir):
    new_a_dir = os.path.join(base_dir, "02_臓器別解剖と標準描出")
    os.rename(a_dir, new_a_dir)

# Rename 03_diseases to Japanese
d_dir = os.path.join(base_dir, "03_diseases")
if os.path.exists(d_dir):
    new_d_dir = os.path.join(base_dir, "03_疾患別超音波所見")
    os.rename(d_dir, new_d_dir)

# Rename 04_measurements to Japanese
m_dir = os.path.join(base_dir, "04_measurements")
if os.path.exists(m_dir):
    new_m_dir = os.path.join(base_dir, "04_実践スクリーニング・計測")
    os.rename(m_dir, new_m_dir)

print("Renamed all main folders to full Japanese!")

# Now rename files inside 01_基本事項・走査法
b_path = os.path.join(base_dir, "01_基本事項・走査法")
if os.path.exists(b_path):
    b_map = {
        "probe_selection.md": "01_基礎知識・プローブ選択.md",
        "scanning_protocol.md": "02_腹部基本描出断面・走査手順.md",
        "artifacts.md": "03_アーチファクトと対処法.md"
    }
    for old, new in b_map.items():
        op = os.path.join(b_path, old)
        if os.path.exists(op):
            os.rename(op, os.path.join(b_path, new))

# Rename files inside 04_実践スクリーニング・計測
m_path = os.path.join(base_dir, "04_実践スクリーニング・計測")
if os.path.exists(m_path):
    m_map = {
        "measurement_manual.md": "01_超音波標準計測手技マニュアル.md",
        "reference_values.md": "02_腹部超音波標準計測値一覧.md",
        "screening_checklist.md": "03_スクリーニング・死角克服ハンドブック.md"
    }
    for old, new in m_map.items():
        op = os.path.join(m_path, old)
        if os.path.exists(op):
            os.rename(op, os.path.join(m_path, new))

# Clean up Japanese filenames in 03_疾患別超音波所見
d_path = os.path.join(base_dir, "03_疾患別超音波所見")
if os.path.exists(d_path):
    for f in os.listdir(d_path):
        if f.endswith(".md") and "IgG4" in f:
            os.rename(os.path.join(d_path, f), os.path.join(d_path, "19_その他_IgG4関連疾患.md"))

print("Renamed internal files to Japanese successfully!")
