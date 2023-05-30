import os
import re
import PyPDF2
import pandas as pd
import tempfile

def extract_resume_data(resume_text):
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
        'Certification': 'Not found',
        'Extracurricular Activity': 'Not found',
        'Education': 'Not found',
        'Technical Skills': 'Not found',
        'Languages': 'Not found',
        'Art Technology': 'Not found',
        'Interests': 'Not found'
    }

    name_match = re.search(r'^(.*?)\n', resume_text, re.MULTILINE)
    if name_match:
        data['Name'] = name_match.group(1).strip()

    skills_match = re.search(r'Programming (.*?)$', resume_text, re.MULTILINE)
    if skills_match:
        data['Skills'] = skills_match.group(1).strip()

    work_experience_match = re.search(r'Experience\n(.*?)$', resume_text, re.MULTILINE | re.DOTALL)
    if work_experience_match:
        data['Work Experience'] = work_experience_match.group(1).strip()

    phone_number_match = re.search(r' (.*?) \|', resume_text)
    if phone_number_match:
        data['Phone Number'] = phone_number_match.group(1).strip()

    email_match = re.search(r' (.*?) \|', resume_text)
    if email_match:
        data['Email'] = email_match.group(1).strip()

    linkedin_match = re.search(r' (.*?)$', resume_text, re.MULTILINE)
    if linkedin_match:
        data['LinkedIn'] = linkedin_match.group(1).strip()

    return data


def process_resumes(directory):
    resume_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    df = pd.DataFrame(columns=[
        'Resume',
        'Name',
        'Work Experience',
        'Phone Number',
        'Email',
        'LinkedIn',
        'Skills'
    ])

    for resume_file in resume_files:
        resume_path = os.path.join(directory, resume_file)

        with open(resume_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            resume_text = ''
            for page in pdf_reader.pages:
                resume_text += page.extract_text()

            resume_data = extract_resume_data(resume_text)
            df = pd.concat([df, pd.DataFrame([{
                'Resume': resume_file,
                'Name': resume_data['Name'],
                'Work Experience': resume_data['Work Experience'],
                'Phone Number': resume_data['Phone Number'],
                'Email': resume_data['Email'],
                'LinkedIn': resume_data['LinkedIn'],
                'Skills': resume_data['Skills']
            }])])

    return df


directory = 'G:\python projects\Resume'
df = process_resumes(directory)

output_file = os.path.join(tempfile.gettempdir(), 'output.xlsx')
df.to_excel(output_file, index=False, engine='xlsxwriter')
print('Data saved to Excel:', output_file)
