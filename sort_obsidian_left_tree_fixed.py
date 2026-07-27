import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# 1. Sort Anatomy Directory
anatomy_dirs = glob.glob(os.path.join(base_dir, "*解剖*")) + [os.path.join(base_dir, "02_anatomy")]
for adir in anatomy_dirs:
    if os.path.exists(adir):
        for f in os.listdir(adir):
            if f.endswith(".md"):
                full_f = os.path.join(adir, f)
                new_prefix = ""
                if "肝" in f: new_prefix = "01_"
                elif "胆" in f: new_prefix = "02_"
                elif "膵" in f: new_prefix = "03_"
                elif "腎" in f: new_prefix = "04_"
                elif "消化管" in f: new_prefix = "05_"
                elif "血管" in f: new_prefix = "06_"
                
                if new_prefix and not re.match(r'^\d\d_', f):
                    new_full = os.path.join(adir, new_prefix + f)
                    os.rename(full_f, new_full)
                    print(f"Anatomy renamed: {f} -> {new_prefix + f}")

# 2. Sort Disease Directory
disease_dirs = glob.glob(os.path.join(base_dir, "*疾患*")) + [os.path.join(base_dir, "03_diseases")]
for ddir in disease_dirs:
    if os.path.exists(ddir):
        for f in os.listdir(ddir):
            if f.endswith(".md"):
                full_f = os.path.join(ddir, f)
                new_prefix = ""
                if "肝臓_脂肪" in f: new_prefix = "01_"
                elif "肝臓_肝硬変" in f: new_prefix = "02_"
                elif "肝臓_肝細胞" in f: new_prefix = "03_"
                elif "肝臓_肝血管腫" in f: new_prefix = "04_"
                elif "肝臓_転移" in f: new_prefix = "05_"
                elif "胆道_胆石" in f: new_prefix = "06_"
                elif "胆道_急性" in f: new_prefix = "07_"
                elif "胆道_胆嚢" in f: new_prefix = "08_"
                elif "膵臓_膵腫瘤" in f: new_prefix = "09_"
                elif "膵臓_膵がん" in f: new_prefix = "10_"
                elif "膵臓_膵嚢胞" in f: new_prefix = "11_"
                elif "膵臓_急性" in f: new_prefix = "12_"
                elif "腎臓_水腎" in f: new_prefix = "13_"
                elif "消化管_急性" in f: new_prefix = "14_"
                elif "消化管_腸閉塞" in f: new_prefix = "15_"
                elif "血管_腹部大動脈" in f: new_prefix = "16_"
                elif "血管_ナットクラッカー" in f: new_prefix = "17_"
                elif "血管_正中" in f: new_prefix = "18_"
                elif "IgG4" in f or "その他" in f: new_prefix = "19_"
                
                if new_prefix and not re.match(r'^\d\d_', f):
                    new_full = os.path.join(ddir, new_prefix + f)
                    os.rename(full_f, new_full)
                    print(f"Disease renamed: {f} -> {new_prefix + f}")

print("File tree sorting completed perfectly!")
