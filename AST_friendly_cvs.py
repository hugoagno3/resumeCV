# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:27:50 2026

@author: Hugo
"""

"""
Created on Sun Mar 15 20:56:24 2026

@author: Hugo
"""

# -*- coding: utf-8 -*-
"""
Render Olga Bobrovska CV with RenderCV from Spyder
"""

import os
import subprocess

# =========================
# Paths
# =========================


base_dir = r"C:\Users\Hugo\Desktop\Resume_Hugo_Amedei\AST_cv\boehringer application"
yaml_file = os.path.join(base_dir, "Hugo_Amedei_CV.yaml")
output_dir = os.path.join(base_dir, "output")

# =========================
# Create output folder
# =========================

os.makedirs(output_dir, exist_ok=True)

# =========================
# Run RenderCV
# =========================

result = subprocess.run(
    [
        "rendercv",
        "render",
        yaml_file,
        "--output-folder",
        output_dir
    ],
    cwd=base_dir,
    capture_output=True,
    text=True
)

# =========================
# Show results
# =========================

print("=== STDOUT ===")
print(result.stdout)

print("=== STDERR ===")
print(result.stderr)

print("Return code:", result.returncode)
print("YAML file exists:", os.path.exists(yaml_file))
print("Output folder exists:", os.path.exists(output_dir))

if os.path.exists(output_dir):
    print("Files in output folder:")
    print(os.listdir(output_dir))


