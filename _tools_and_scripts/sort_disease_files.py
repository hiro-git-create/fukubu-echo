import os
import glob
import re

base_dir = r"C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Rename disease files with numeric ordering prefixes for perfectly sorted file tree in Obsidian
disease_dir = os.path.join(base_dir, "03_diseases")

rename_map = {
    # 1. Liver
    "liver_fatty.md": "01_liver_fatty.md",
    "liver_cirrhosis.md": "02_liver_cirrhosis.md",
    "liver_hcc.md": "03_liver_hcc.md",
    "liver_hemangioma.md": "04_liver_hemangioma.md",
    "liver_metastasis.md": "05_liver_metastasis.md",
    
    # 2. Biliary
    "biliary_stones.md": "06_biliary_stones.md",
    "biliary_cholecystitis.md": "07_biliary_cholecystitis.md",
    "biliary_polyps_adm.md": "08_biliary_polyps_adm.md",
    
    # 3. Pancreas
    "pancreas_mass_classification.md": "09_pancreas_mass_classification.md",
    "pancreas_cancer.md": "10_pancreas_cancer.md",
    "pancreas_cystic.md": "11_pancreas_cystic.md",
    "pancreas_pancreatitis.md": "12_pancreas_pancreatitis.md",
    
    # 4. Kidney & Spleen
    "kidney_hydronephrosis.md": "13_kidney_hydronephrosis.md",
    
    # 5. GI
    "gi_appendicitis.md": "14_gi_appendicitis.md",
    "gi_ileus.md": "15_gi_ileus.md",
    
    # 6. Vessels
    "vessels_aaa.md": "16_vessels_aaa.md",
    "vessels_nutcracker.md": "17_vessels_nutcracker.md",
    "vessels_mals.md": "18_vessels_mals.md"
}

for old_name, new_name in rename_map.items():
    old_p = os.path.join(disease_dir, old_name)
    new_p = os.path.join(disease_dir, new_name)
    if os.path.exists(old_p):
        os.rename(old_p, new_p)
        print(f"Renamed: {old_name} -> {new_name}")

print("File tree ordering updated successfully!")
