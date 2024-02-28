from twilio.rest import Client
import smtplib
import requests

TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR_TWILIO_VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_NUMBER"
EMAIL = "YOUR_MAIL"
PASS = "YOUR_APP_PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, message):
        url = 'YOUR_SHEETY_ENDPOINT'
        response = requests.get(url)
        json_data = response.json()
        for email in json_data['users']:
            to_adress = email['email']
            connect = smtplib.SMTP("YOUR_EMAIL_SERVICE_PROVIDER_HOST e.g. smtp.gmail.com", port="YOUR_EMAIL_SERVICE_PROVIDER_PORT e.g. 587")
            connect.starttls()
            connect.login(user=EMAIL,password=PASS)
            connect.sendmail(from_addr=EMAIL, to_addrs=to_adress, msg=message.encode('utf-8'))
            connect.close()