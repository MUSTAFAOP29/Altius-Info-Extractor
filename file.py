import streamlit as st
import pdfplumber
import fitz  # PyMuPDF
import json
import os
import tempfile
import google.generativeai as genai

# ---------------- NORMAL EXTRACTION ----------------
def extract_pdf(pdf_path, extract_images=False):
    data = {"pages": []}
    pdf = pdfplumber.open(pdf_path)
    doc = fitz.open(pdf_path)

    for i, page in enumerate(pdf.pages, start=1):
        page_data = {"page_number": i, "content": []}

        # Extract text as paragraphs
        text = page.extract_text()
        if text:
            for para in text.split("\n"):
                page_data["content"].append({
                    "type": "paragraph",
                    "text": para.strip()
                })

        # Extract tables
        tables = page.extract_tables()
        for t in tables:
            page_data["content"].append({
                "type": "table",
                "table_data": t
            })

        # Extract images
        if extract_images:
            img_dir = os.path.join("images")
            os.makedirs(img_dir, exist_ok=True)
            fitz_page = doc[i-1]
            for img_index, img in enumerate(fitz_page.get_images(full=True), start=1):
                xref = img[0]
                base_image = doc.extract_image(xref)
                ext = base_image["ext"]
                img_bytes = base_image["image"]
                filename = f"page{i}_img{img_index}.{ext}"
                filepath = os.path.join(img_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(img_bytes)
                page_data["content"].append({
                    "type": "image",
                    "path": filepath
                })

        data["pages"].append(page_data)

    pdf.close()
    doc.close()
    return data

# ---------------- GENAI EXTRACTION ----------------
def extract_with_gemini(pdf_path):
    genai.configure(api_key="AIzaSyD1R0pFEFRmaQKru1r7RxdGQ5cT5Ma7gVQ")
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([
        {"mime_type": "application/pdf", "data": pdf_bytes},
        "Extract structured JSON from this PDF with text, tables, and images (if possible)."
    ])

    try:
        data = json.loads(response.text)
    except Exception:
        data = {"error": "Could not parse JSON response", "raw": response.text}

    return data

# ---------------- STREAMLIT APP ----------------
st.title("📄 PDF Extractor (Text, Tables, Images)")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
method = st.radio("Choose Extraction Method", ["Normal", "GenAI (Gemini)"])
extract_images = st.checkbox("Extract Images (Normal mode only)", value=False)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if method == "Normal":
        data = extract_pdf(tmp_path, extract_images)
    else:
        data = extract_with_gemini(tmp_path)

    # Save JSON
    json_path = "output.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    st.success("✅ Extraction complete!")
    st.download_button("Download JSON", data=json.dumps(data, indent=2), file_name="output.json")

    # Show extracted content
    if method == "Normal":
        for page in data["pages"]:
            st.subheader(f"Page {page['page_number']}")
            for block in page["content"]:
                if block["type"] == "paragraph":
                    st.write(block["text"])
                elif block["type"] == "table":
                    st.table(block["table_data"])
                elif block["type"] == "image":
                    st.image(block["path"])
    else:
        st.json(data)
