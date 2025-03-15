from twilio.rest import Client

my_twilio_number = +13134762190
account_sid = "AC6df112f0b91b08da20efb1b7d93569ed"
auth_token = "da8d96a52ac69628e3d70418fe9ed4fe"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(username=account_sid,password=auth_token)

    def send_message(self,message_body):
        message = self.client.messages.create(
            from_=my_twilio_number,
            body=message_body,
            to='+916382727512'
        )
        print(f"message status is {message.status}")
        print(f"message sid is {message.sid}")