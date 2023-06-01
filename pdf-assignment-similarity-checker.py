'''
Question: Write a Python program that compares multiple PDF files stored in a directory.
The program should start by selecting the first PDF file and compare it with all the other
PDF files in the directory. It should then move on to the next PDF file and compare it with 
the remaining files, and so on, until all PDF files have been compared. For each comparison,
the program should output the similarity ratio between the two PDF files being compared. 
How would you implement this program?

Note: This question assesses your ability to design a program that iterates over a collection 
of files, performs comparisons, and generates output based on the comparisons. Be prepared to 
explain the steps involved and describe any libraries or modules you would use in your solution.
'''
import os
import pdfplumber
import difflib

def compare_pdf_similarity(file_path_1, file_path_2):
    with open(file_path_1, 'rb') as file1, open(file_path_2, 'rb') as file2:
        pdf1 = pdfplumber.open(file1)
        pdf2 = pdfplumber.open(file2)
        
        text1 = ''
        for page in pdf1.pages:
            text1 += page.extract_text()
        
        text2 = ''
        for page in pdf2.pages:
            text2 += page.extract_text()

        similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
        return similarity_ratio

# Directory containing the PDF files
pdf_directory = 'path/to/pdf/files'

# Get the list of PDF files
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# Compare each PDF file with all the other PDF files
for i in range(len(pdf_files)):
    file_path_1 = os.path.join(pdf_directory, pdf_files[i])
    print(f"Comparing {pdf_files[i]} with other PDF files:")
    
    for j in range(i+1, len(pdf_files)):
        file_path_2 = os.path.join(pdf_directory, pdf_files[j])
        
        similarity = compare_pdf_similarity(file_path_1, file_path_2)
        print(f"Similarity between {pdf_files[i]} and {pdf_files[j]}: {similarity}")
