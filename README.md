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
```
---
🧾 Step 2 — YAML CV

# Open the file:
Ats_CV.yaml

'# This file contains:
'# - Experience
'# - Skills
'# - Education
'# - Layout and structure

'# Key idea:
'# You separate CONTENT (YAML) from FORMAT (RenderCV)

'# Benefits:'# - Easy to update'# - Clean structure'# - Reproducible CV
---

## 🖥️ 3. Run the script (Spyder or Python)

You can run the script using **Spyder** or any Python IDE.

Make sure the paths inside `AST_friendly_cvs.py` match your local directory:
```python
base_dir = r"C:\Users\Hugo\Desktop\Resume_Hugo_Amedei\AST_cv\Ats_cv"
## make sure that the yaml file match (yaml file can be opened and edited as a txt file).
yaml_file = os.path.join(base_dir, "Ats_CV.yaml")
```
Then run:
```python
python AST_friendly_cvs.py

```
This will:

Call RenderCV
Process your YAML file
Generate your CV automatically

📄 4. Output

After running the script, your CV will be generated in:
/output

Generated files include:

PDF (ATS-friendly CV)
HTML version
Markdown version

👉 The PDF file is ready to use for job applications.

🤝 Final note

This workflow is designed to help create clean, structured CVs using simple tools (Python + YAML).

As a protein scientist, I use Python occasionally, and I found this approach very useful for organizing and maintaining CVs.

Feel free to adapt and use it for your own applications.
