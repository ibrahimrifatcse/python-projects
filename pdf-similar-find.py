import pdfplumber
from difflib import SequenceMatcher

def compare_pdf_similarity(file1, file2):
    # Open the first PDF file
    with pdfplumber.open(file1) as pdf1:
        text1 = ""
        # Extract text from all pages
        for page in pdf1.pages:
            text1 += page.extract_text()

    # Open the second PDF file
    with pdfplumber.open(file2) as pdf2:
        text2 = ""
        # Extract text from all pages
        for page in pdf2.pages:
            text2 += page.extract_text()

    # Calculate the similarity between the two texts
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()

    return similarity_ratio

# Provide the file paths of the two PDF files
pdf_file1 = "good with words writing and editing.pdf"
pdf_file2 = "good words.pdf"

# Compare the PDF files and get the similarity ratio
similarity_ratio = compare_pdf_similarity(pdf_file1, pdf_file2)

# Print the similarity ratio
print("Similarity Ratio: {:.2%}".format(similarity_ratio))
