from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(username=os.environ['account_sid'],password=os.environ['auth_token'])
        self.twilio_recipient = os.environ['recipient']
        self.sender = os.environ['my_email']
        self.password = os.environ['password']
        # self.recipient = os.environ['recipient_email']

    def send_message(self,message_body):
        message = self.client.messages.create(
            from_=os.environ['my_twilio_number'],
            body=message_body,
            to=self.twilio_recipient
        )
        print(f"message status is {message.status}")
        print(f"message sid is {message.sid}")

    def send_mails(self,email_list,message):
        try:
            with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(self.sender,self.password)
                for mail in email_list:
                    connection.sendmail(from_addr=self.sender,to_addrs=mail,msg=f"Subject: Low Price Alert!\n\n{message}".encode("utf-8"))
        except Exception as e:
            print(f"Error connecting to the smtp server. {e}")

