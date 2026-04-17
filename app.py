import streamlit as st
from utils.pdf_processor import extract_text, split_sections
from utils.summarizer import summarize_text
from utils.paraphraser import paraphrase_text
from utils.citation import generate_citation

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🧠 AI Research Paper Summarizer + Plagiarism Corrector")

uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text(uploaded_file)

    if not text:
        st.error("❌ Could not extract text from PDF")
    else:
        sections = split_sections(text)

        st.success("✅ Sections detected!")

        view_option = st.radio("Select View:", ["Summary", "Rewritten"])

        for section, content in sections.items():
            st.subheader(section)

            if view_option == "Summary":
                summary = summarize_text(content)
                st.write(summary)

            else:
                rewritten = paraphrase_text(content)
                st.write(rewritten)

        st.subheader("📚 Citation")
        citation = generate_citation(text)
        st.code(citation)

        st.download_button(
            "📥 Download Full Report",
            text,
            file_name="processed_text.txt"
        )
