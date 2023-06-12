import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_email, to_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, message, from_email, to_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

def get_daily_contests():
    response = requests.get('https://codeforces.com/api/contest.list')
    contests = response.json()['result']
    
    daily_contests = []
    for contest in contests:
        if contest['phase'] == 'BEFORE' and contest['relativeTimeSeconds'] <= 24 * 60 * 60:
            daily_contests.append(contest)

    return daily_contests

def format_contest_details(contest):
    contest_id = contest['id']
    contest_name = contest['name']
    contest_start_time = contest['startTimeSeconds']
    contest_duration = contest['durationSeconds']

    start_time = datetime.datetime.fromtimestamp(contest_start_time).strftime('%Y-%m-%d %H:%M:%S')
    duration_hours = contest_duration // 3600

    contest_url = f"https://codeforces.com/contest/{contest_id}"

    formatted_details = f"Contest Name: {contest_name}\n"
    formatted_details += f"Start Time: {start_time}\n"
    formatted_details += f"Duration: {duration_hours} hours\n"
    formatted_details += f"URL: {contest_url}\n\n"

    return formatted_details

def send_daily_contest_email(email, password, recipients):
    contests = get_daily_contests()

    if not contests:
        print("No contests found for today.")
        return

    subject = "Codeforces Daily Contest Notification"
    message = "Daily Contests:\n\n"

    for contest in contests:
        contest_details = format_contest_details(contest)
        message += contest_details

    for recipient in recipients:
        send_email(subject, message, email, recipient, password)
        print(f"Email sent to: {recipient}")

    print("Email notifications sent successfully.")

# Configure your email settings
email = 'your mail'
password = 'your mail pass or make sure that you have allowed access for "Less secure apps" in your Gmail account settings'  #https://myaccount.google.com/

# Provide the recipients' email addresses
recipients = ['recipient2@example.com', 'recipient2@example.com']

# Send daily contest email notifications
send_daily_contest_email(email, password, recipients)


#output 
'''
Daily Contests:

Contest Name: CodeTON Round 5 (Div. 1 + Div. 2, Rated, Prizes!)
Start Time: 2023-06-24 20:05:00
Duration: 3 hours
URL: https://codeforces.com/contest/1842

Contest Name: Codeforces Round (Div. 1)
Start Time: 2023-06-18 20:35:00
Duration: 2 hours
URL: https://codeforces.com/contest/1835

Contest Name: Codeforces Round (Div. 2)
Start Time: 2023-06-18 20:35:00
Duration: 2 hours
URL: https://codeforces.com/contest/1836

Contest Name: Codeforces Round (Div. 2)
Start Time: 2023-06-18 14:05:00
Duration: 2 hours
URL: https://codeforces.com/contest/1834
'''





