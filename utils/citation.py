import re

def generate_citation(text):
    try:
        lines = text.split("\n")

        title = lines[0][:100]
        year_match = re.search(r"(20\d{2})", text)
        year = year_match.group(0) if year_match else "2024"

        authors = "Unknown Author"

        apa = f"{authors} ({year}). {title}."
        mla = f"{authors}. \"{title}.\" {year}."

        return f"APA:\n{apa}\n\nMLA:\n{mla}"

    except:
        return "Citation could not be generated"
