import os
import re
import PyPDF2

def extract_resume_data(pdf_path):
    data = {
        'Name': 'Not found',
        'CGPA': 'Not found',
        'GPA': 'Not found',
        'Skills': 'Not found',
        'Institute': 'Not found',
        'Programming Skills': 'Not found',
        'IT Skills': 'Not found',
        'Work Experience': 'Not found',
        'Previous Job': 'Not found',
        'Job Duration': 'Not found',
        'Phone Number': 'Not found',
        'Email': 'Not found',
        'LinkedIn': 'Not found',
        'Certification': 'Not found'
    }
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        # Extract text from each page of the PDF
        resume_text = ''
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            resume_text += page.extract_text()
        
        # Extract information using regular expressions
        name_match = re.search(r'Name: ([^\n]+)', resume_text, re.IGNORECASE)
        if name_match:
            data['Name'] = name_match.group(1).strip()
        
        cgpa_match = re.search(r'CGPA: ([^\n]+)', resume_text, re.IGNORECASE)
        if cgpa_match:
            data['CGPA'] = cgpa_match.group(1).strip()
        
        gpa_match = re.search(r'GPA: ([^\n]+)', resume_text, re.IGNORECASE)
        if gpa_match:
            data['GPA'] = gpa_match.group(1).strip()
        
        skills_match = re.search(r'Skills: ([^\n]+)', resume_text, re.IGNORECASE)
        if skills_match:
            data['Skills'] = skills_match.group(1).strip()
        
        institute_match = re.search(r'Institute: ([^\n]+)', resume_text, re.IGNORECASE)
        if institute_match:
            data['Institute'] = institute_match.group(1).strip()
        
        programming_skills_match = re.search(r'Programming Skills: ([^\n]+)', resume_text, re.IGNORECASE)
        if programming_skills_match:
            data['Programming Skills'] = programming_skills_match.group(1).strip()
        
        it_skills_match = re.search(r'IT Skills: ([^\n]+)', resume_text, re.IGNORECASE)
        if it_skills_match:
            data['IT Skills'] = it_skills_match.group(1).strip()
        
        experience_match = re.search(r'Work Experience: ([^\n]+)', resume_text, re.IGNORECASE)
        if experience_match:
            data['Work Experience'] = experience_match.group(1).strip()
        
        previous_job_match = re.search(r'Previous Job: ([^\n]+)', resume_text, re.IGNORECASE)
        if previous_job_match:
            data['Previous Job'] = previous_job_match.group(1).strip()
        
        job_duration_match = re.search(r'Job Duration: ([^\n]+)', resume_text, re.IGNORECASE)
        if job_duration_match:
            data['Job Duration'] = job_duration_match.group(1).strip()
        
        phone_number_match = re.search(r'Phone Number: ([^\n]+)', resume_text, re.IGNORECASE)
        if phone_number_match:
            data['Phone Number'] = phone_number_match.group(1).strip()
        
        email_match = re.search(r'Email: ([^\n]+)', resume_text, re.IGNORECASE)
        if email_match:
            data['Email'] = email_match.group(1).strip()
        
        linkedin_match = re.search(r'LinkedIn: ([^\n]+)', resume_text, re.IGNORECASE)
        if linkedin_match:
            data['LinkedIn'] = linkedin_match.group(1).strip()
        
        certification_match = re.search(r'Certification: ([^\n]+)', resume_text, re.IGNORECASE)
        if certification_match:
            data['Certification'] = certification_match.group(1).strip()
    
    return data


def process_resumes(directory):
    # Get the list of PDF files in the directory
    resume_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    
    # Process each resume file
    for resume_file in resume_files:
        resume_path = os.path.join(directory, resume_file)
        resume_data = extract_resume_data(resume_path)
        
        print('Resume:', resume_file)
        print('Name:', resume_data['Name'])
        print('Work Experience:', resume_data['Work Experience'])
        print('CGPA:', resume_data['CGPA'])
        print('GPA:', resume_data['GPA'])
        print('Skills:', resume_data['Skills'])
        print('Institute:', resume_data['Institute'])
        print('Programming Skills:', resume_data['Programming Skills'])
        print('IT Skills:', resume_data['IT Skills'])
        print('Work Experience in Previous Job:', resume_data['Previous Job'])
        print('Previous Job Duration:', resume_data['Job Duration'])
        print('Phone Number:', resume_data['Phone Number'])
        print('Email:', resume_data['Email'])
        print('LinkedIn:', resume_data['LinkedIn'])
        print('Certification:', resume_data['Certification'])
        print()


# Provide the path to the directory containing the resume files
resume_directory = 'G:\python projects\Resume'
process_resumes(resume_directory)
