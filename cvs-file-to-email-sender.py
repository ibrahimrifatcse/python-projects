import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read data from CSV file
emails = []
names = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        emails.append(row[0])
        names.append(row[1])

# Email configuration
sender_email = 'your_email@gmail.com'
password = 'your_password'
subject = 'Club Meeting Update'
message = 'Dear {name},\n\nThis is to inform you about the latest updates regarding the club meeting.\n\nBest regards,\nYour Club'

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
