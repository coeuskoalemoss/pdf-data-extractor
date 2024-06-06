import streamlit as st
import PyPDF2
from pdfminer.high_level import extract_text

def extract_text_from_pdf_pypdf2(pdf_file):
    # Creating a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    print(f"Total pages: {num_pages}")

    # Initialize an empty string to store all the text
    full_text = ""

    # Iterate through each page
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        try:
            # Extract text from the page
            text = page.extract_text()
            full_text += text + "\n"
            print(f"Extracted text from page {page_num+1}")
        except Exception as e:
            print(f"Failed to extract text from page {page_num+1}: {e}")
    
    return full_text

def extract_text_from_pdf_pdfminer(pdf_file):
    try:
        # Extract text from the PDF file
        text = extract_text(pdf_file)
        return text
    except Exception as e:
        st.error(f"An error occurred while extracting text using pdfminer: {e}")
        return ""

# Streamlit app
st.title("PDF Text Extractor")

st.sidebar.header("Choose Text Extraction Method")
method = st.sidebar.selectbox("Method", ["PyPDF2", "pdfminer.six"])

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    st.write(f"**Filename:** {uploaded_file.name}")
    
    # Extract text based on the chosen method
    if method == "PyPDF2":
        text = extract_text_from_pdf_pypdf2(uploaded_file)
    else:
        text = extract_text_from_pdf_pdfminer(uploaded_file)
    
    # Display the extracted text
    if text:
        st.text_area("Extracted Text", text, height=500)
    else:
        st.error("No text could be extracted from the PDF.")