import fitz  # PyMuPDF
import re

def extract_text(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except:
        return None


def split_sections(text):
    sections = {
        "Abstract": "",
        "Introduction": "",
        "Methodology": "",
        "Results": "",
        "Conclusion": ""
    }

    patterns = {
        "Abstract": r"(?i)(abstract)(.*?)(introduction)",
        "Introduction": r"(?i)(introduction)(.*?)(methodology|methods)",
        "Methodology": r"(?i)(methodology|methods)(.*?)(results)",
        "Results": r"(?i)(results)(.*?)(discussion|conclusion)",
        "Conclusion": r"(?i)(conclusion)(.*)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            sections[key] = match.group(2).strip()

    # fallback if empty
    if all(v == "" for v in sections.values()):
        sections = {"Full Text": text[:3000]}

    return sections
