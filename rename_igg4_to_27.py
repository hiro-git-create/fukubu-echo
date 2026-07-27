import os

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書\03_疾患別超音波所見"

old_f = os.path.join(base_dir, "20_その他_IgG4関連疾患.md")
new_f = os.path.join(base_dir, "27_その他_IgG4関連疾患.md")

if os.path.exists(old_f):
    os.rename(old_f, new_f)
    print("Renamed 20_その他_IgG4関連疾患.md -> 27_その他_IgG4関連疾患.md successfully!")
