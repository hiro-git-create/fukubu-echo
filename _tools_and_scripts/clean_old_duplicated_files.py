import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"
m_path = os.path.join(base_dir, "04_実践スクリーニング・計測")

# Target exact old files to delete
old_files_to_delete = [
    "スクリーニングチェックリスト.md",
    "腹部超音波計測値一覧.md",
    "超音波標準計測手技マニュアル.md"
]

for f in old_files_to_delete:
    fp = os.path.join(m_path, f)
    if os.path.exists(fp):
        os.remove(fp)
        print(f"Deleted old duplicated file: {f}")

# Make sure 01_超音波標準計測手技マニュアル.md exists
manual_old = os.path.join(m_path, "超音波標準計測手技マニュアル.md")
manual_new = os.path.join(m_path, "01_超音波標準計測手技マニュアル.md")

if os.path.exists(manual_old) and not os.path.exists(manual_new):
    os.rename(manual_old, manual_new)

print("Cleaned 04_実践スクリーニング・計測 directory successfully!")
