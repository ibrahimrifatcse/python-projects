import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Read data from CSV file
with open('ibrahim - Sheet2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    data = list(reader)

# Extract email addresses and names from data
emails = [row[0] for row in data]
names = [row[1] for row in data]

# Email configuration
sender_email = '******@gmail.com'
password = 'your gmail password'
subject = 'Subject: Weekend Update - May 22, 2023'
message = 'Dear {name},\n\nI hope this email finds you well. \nHeres update:\nDLD:\nCT2  is scheduled for Monday, May 22, 2023.\nTopics to focus on include: Magnitude Comparator, Encoder, Decoder, Multiplexer, and Demultiplexer.\n\nOOP:\n portfolio topics:\n1.Abstract Class and Interface. \n2.Exception Handling and Packageions.\n\nEconomics:CT2 for Economics is scheduled for Tuesday, May 23, 2023.\nCT2 topic is GDP Calculation and + *******.\n\nEnjoy your weekend!\n\nBest regards,\nCR Ibrahim Rifat'

# File attachments
#attachment_file1 = 'path_to_excel_file.xlsx'
#attachment_file2 = 'artificial.pdf'
#attachment_file3 = 'path_to_word_file.docx'
#attachment_file4 = 'ibrahim - Sheet1.csv'
#attachment_file5 = 'path_to_song.mp3'
#attachment_file6 = 'path_to_text.txt'
#attachment_file7 = 'image.png'

# Iterate over each student and send email
for email, name in zip(emails, names):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    # Create the message body
    body = message.format(name=name)
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    for file_path in [ attachment_file7,attachment_file1,attachment_file4]:
        with open(file_path, 'rb') as attachment_file:
            attachment_data = attachment_file.read()

        file_name = os.path.basename(file_path)
        attachment = MIMEApplication(attachment_data)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(attachment)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print(f"Email sent to {name} at {email}")

print("All emails sent successfully.")
