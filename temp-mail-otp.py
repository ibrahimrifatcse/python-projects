import requests
import time

def create_temp_email():
    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox")
    data = response.json()
    if response.status_code == 200:
        email = data['email']
        password = data['password']
        return email, password
    else:
        print("Error creating temporary email.")
        return None, None

def fetch_otp(email):
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email.split('@')[0]}&domain={email.split('@')[1]}")
    data = response.json()
    if response.status_code == 200:
        if len(data) > 0:
            otp = data[0]['body'].split()[-1]  # Assuming OTP is the last word in the email body
            return otp
        else:
            return None
    else:
        print("Error fetching OTP.")
        return None

# Usage example
email, password = create_temp_email()
print(f"Temporary Email: {email}")
print(f"Password: {password}")

# Simulating a delay before fetching OTP
time.sleep(10)

otp = fetch_otp(email)
if otp:
    print(f"Received OTP: {otp}")
else:
    print("No OTP received yet.")

    
    '''
    




Please note that this example uses the 1secmail 
API, which may have limitations or require an 
API key for certain features. Additionally,
there's a delay of 10 seconds (`time.sleep(10)`) 
added before fetching the OTP to simulate a wait
time for the email to arrive. You can adjust the 
delay according to your requirements.
    '''
