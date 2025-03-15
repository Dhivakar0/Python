from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twilio credentials
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
twilio_number = os.environ['my_twilio_number']

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, this is a test message",
    from_=twilio_number,
    to='+916382727512'
)

print(message.sid)
