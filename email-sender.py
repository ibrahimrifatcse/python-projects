import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Read data from CSV file
with open('ibrahim - Sheet1.csv', 'r') as file:
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

# Iterate over each student and send email
for email, name in zip(emails, names):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    # Create the message body
    body = message.format(name=name)
    msg.attach(MIMEText(body, 'plain'))
'''
    # Attach the image
    image = MIMEImage(image_data)
    image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
    msg.attach(image)
'''
    # Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print(f"Email sent to {name} at {email}")

print("All emails sent successfully.")


'''
1. Are you missing out on important updates? Are you tired of not receiving timely information,
classroom notifications, or relying on group messages for updates? Don't worry! We've got you
covered. Enter your email and name below, and we'll make sure to send you the latest class 
minutes directly to your inbox. Stay informed and never miss a beat. We're here to make your 
learning experience seamless and hassle-free. Join us today and stay connected!

2. Stay informed and never miss a beat! Get timely class updates and notifications directly
to your inbox. Enter your email and name below to receive class minutes and stay connected 
with us. Join now for hassle-free information delivery.
'''
'''
The number 587 is the port number used for SMTP (Simple Mail Transfer Protocol) over TLS/SSL. SMTP is the protocol used for sending email, and port 587 is the standard port for submitting email to an email server.

When you use `smtplib.SMTP('smtp.gmail.com', 587)`, you are connecting to the Gmail SMTP server (`smtp.gmail.com`) on port 587 to send your emails.

Regarding `MIMEMultipart` and `MIMEText`, these are classes from the `email.mime.multipart` and `email.mime.text` modules, respectively, which are part of the `email` package in Python's standard library.

- `MIMEMultipart` is a class for creating multipart email messages, which can contain both plain text and HTML content, as well as attachments.
- `MIMEText` is a class for creating a plain text email message.

In your code, you are using `MIMEMultipart` to create the main email message object, and then attaching a `MIMEText` object as the plain text body of the email.

By using these classes, you can create more complex email messages with multiple parts, such as HTML content, attachments, and alternative text versions.

It's important to note that the code you provided has a typo in the line `body - message.formate(name=name)`. It should be `body = message.format(name=name)` instead.
'''