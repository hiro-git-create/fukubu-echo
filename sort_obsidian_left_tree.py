import os
import glob

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# 1. Sort Anatomy Directory (02_臓器別解剖と標準描出 or 02_anatomy)
anatomy_dirs = glob.glob(os.path.join(base_dir, "*解剖*")) + [os.path.join(base_dir, "02_anatomy")]
for adir in anatomy_dirs:
    if os.path.exists(adir):
        anat_map = {
            "肝臓": "01_肝臓_解剖と描出法.md",
            "胆": "02_胆嚢・胆管_解剖と描出法.md",
            "膵": "03_膵臓_解剖と描出法.md",
            "腎": "04_腎臓・副腎_解剖と描出法.md",
            "消化管": "05_消化管_解剖と描出法.md",
            "血管": "06_腹部血管・後腹膜_解剖と描出法.md"
        }
        for f in os.listdir(adir):
            if f.endswith(".md"):
                full_f = os.path.join(adir, f)
                for key, new_name in anat_map.items():
                    if key in f and not f.startswith("0"):
                        new_full = os.path.join(adir, new_name)
                        os.rename(full_f, new_full)
                        print(f"Anatomy renamed: {f} -> {new_name}")

# 2. Sort Disease Directory (03_疾患別超音波所見 or 03_diseases)
disease_dirs = glob.glob(os.path.join(base_dir, "*疾患*")) + [os.path.join(base_dir, "03_diseases")]
for ddir in disease_dirs:
    if os.path.exists(ddir):
        dis_map = [
            ("肝臓_脂肪肝", "01_肝臓_脂肪肝.md"),
            ("肝臓_肝硬変", "02_肝臓_肝硬変.md"),
            ("肝臓_肝細胞", "03_肝臓_肝細胞がん.md"),
            ("肝臓_肝血管腫", "04_肝臓_肝血管腫.md"),
            ("肝臓_転移", "05_肝臓_転移性肝がん.md"),
            ("胆道_胆石", "06_胆道_胆石症.md"),
            ("胆道_急性", "07_胆道_急性・慢性胆嚢炎.md"),
            ("胆道_胆嚢ポリ", "08_胆道_胆嚢ポリープ・腺筋腫症.md"),
            ("膵臓_膵腫瘤", "09_膵臓_膵腫瘤性病変_固形および嚢胞性分類.md"),
            ("膵臓_膵がん", "10_膵臓_膵がん.md"),
            ("膵臓_膵嚢胞", "11_膵臓_膵嚢胞性腫瘍.md"),
            ("膵臓_急性", "12_膵臓_急性・慢性膵炎.md"),
            ("腎臓_水腎", "13_腎臓_水腎症.md"),
            ("消化管_急性", "14_消化管_急性虫垂炎.md"),
            ("消化管_腸閉塞", "15_消化管_腸閉塞・イレウス.md"),
            ("血管_腹部大動脈", "16_血管_腹部大動脈瘤.md"),
            ("血管_ナットクラッカー", "17_血管_ナットクラッカー症候群.md"),
            ("血管_正中", "18_血管_正中弓状靭帯圧迫症候群_MALS.md"),
            ("IgG4", "19_その他_IgG4関連疾患_IgG4_RD.md"),
            ("igg4", "19_その他_IgG4関連疾患_IgG4_RD.md")
        ]
        for f in os.listdir(ddir):
            if f.endswith(".md"):
                full_f = os.path.join(ddir, f)
                for key, new_name in dis_map:
                    if key in f and not re.match(r'^\d\d_', f):
                        new_full = os.path.join(ddir, new_name)
                        os.rename(full_f, new_full)
                        print(f"Disease renamed: {f} -> {new_name}")

print("File tree sorting completed!")
