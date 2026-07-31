import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"
d_path = os.path.join(base_dir, "03_疾患別超音波所見")

# Correct numeric order: Vessels group together, Others at the very end
renames = [
    # Vessels Group (16 ~ 19)
    ("20_血管_SMA症候群.md", "19_血管_SMA症候群.md"),
    
    # Others Group at the very bottom (20)
    ("19_others_igg4_rd.md", "20_その他_IgG4関連疾患.md"),
    ("19_その他_IgG4関連疾患.md", "20_その他_IgG4関連疾患.md")
]

for old_f, new_f in renames:
    op = os.path.join(d_path, old_f)
    np = os.path.join(d_path, new_f)
    if os.path.exists(op):
        os.rename(op, np)
        print(f"Renamed: {old_f} -> {new_f}")

print("Fixed sorting order perfectly: Vessels (16-19) -> Others (20)")
