import os
import shutil
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Merge & Rename directories safely
def merge_dirs(src_name, dst_name):
    src = os.path.join(base_dir, src_name)
    dst = os.path.join(base_dir, dst_name)
    if os.path.exists(src):
        os.makedirs(dst, exist_ok=True)
        for item in os.listdir(src):
            s_item = os.path.join(src, item)
            d_item = os.path.join(dst, item)
            if os.path.isdir(s_item):
                if os.path.exists(d_item):
                    for sub in os.listdir(s_item):
                        shutil.move(os.path.join(s_item, sub), os.path.join(d_item, sub))
                    os.rmdir(s_item)
                else:
                    shutil.move(s_item, d_item)
            else:
                shutil.move(s_item, d_item)
        os.rmdir(src)
        print(f"Merged {src_name} into {dst_name}")

merge_dirs("01_basics", "01_基本事項・走査法")
merge_dirs("02_anatomy", "02_臓器別解剖と標準描出")
merge_dirs("03_diseases", "03_疾患別超音波所見")
merge_dirs("04_measurements", "04_実践スクリーニング・計測")

# Rename internal files in 01
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

# Rename internal files in 04
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

print("All directories and files merged into clean Japanese structure!")
