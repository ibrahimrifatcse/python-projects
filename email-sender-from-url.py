# pip install gspread oauth2client

import gspread
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Connect to Google Spreadsheet
gc = gspread.service_account(filename='ibrahim.json')
spreadsheet_url = 'https://docs.google.com/spreadsheet'
worksheet_name = 'ibrahim'
spreadsheet = gc.open_by_url(spreadsheet_url)
worksheet = spreadsheet.worksheet(worksheet_name)

# Extract email addresses and names from the worksheet
data = worksheet.get_all_values()
emails = [row[0] for row in data[1:]]
names = [row[1] for row in data[1:]]

# Email configuration
sender_email = 'your_email@gmail.com'
password = 'your_password'
subject = 'Important Updates for Tomorrow'
message = 'Dear {name},\n\nHope you are doing well! I wanted to share our upcoming GED CT2 syllabus : \n GDP calculation \n some slide : \n slide-\n 1. https://drive.google.com/file/d/1EGG1h_qkT0G0nS0oz6vhYIuKjqnIkI2o/view \n2. https://drive.google.com/file/d/1PtmszxfcPxh78ibbLZiywthRpRBNIc_U/view \n3.https://drive.google.com/file/d/1E8NjnOlhFN4825js3ZtouqHwAVR2SiSq/view.\n\n.Best regards,\nIbrahim Rifat'

# Iterate over each student and send email
for email, name in zip(emails, names):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    # Create the message body
    body = message.format(name=name)
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print(f"Email sent to {name} at {email}")

print("All emails sent successfully.")
