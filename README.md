# 🧬 ATS-Friendly CV with Python (RenderCV + YAML)

This repository shows a simple workflow to create **ATS-friendly CVs using Python, YAML, and RenderCV**.

As a **protein scientist**, I don’t code every day — but this approach helped me create structured, clean CVs that are easy to maintain and readable by Applicant Tracking Systems (ATS).

The goal is simple:  
👉 Help others build a clean, reproducible CV using minimal tools.

---

## 📂 Repository structure

- `AST_friendly_cvs.py` → Python script to generate the CV  
- `Ats_CV.yaml` → CV content (editable)  
- `pic_example.jpg` → Example profile picture  

---

## ⚙️ 1. Install RenderCV

Make sure you have Python installed.

Then install RenderCV:

```bash
pip install rendercv

🧾 Step 2 — YAML CV

# Open the file:
Ats_CV.yaml

# This file contains:
# - Experience
# - Skills
# - Education
# - Layout and structure

# Key idea:
# You separate CONTENT (YAML) from FORMAT (RenderCV)

# Benefits:
# - Easy to update
# - Clean structure
# - Reproducible CV
