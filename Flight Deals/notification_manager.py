from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(username=os.environ['account_sid'],password=os.environ['auth_token'])

    def send_message(self,message_body):
        message = self.client.messages.create(
            from_=os.environ['my_twilio_number'],
            body=message_body,
            to='+916382727512'
        )
        print(f"message status is {message.status}")
        print(f"message sid is {message.sid}")