import requests
from datetime import datetime
from twilio.rest import Client
import os

ACCOUNT_SID = "ACCOUNT_SID_INFO"
AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "+123456789"
TWILIO_VERIFIED_NUMBER = "+999999999"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)


    def send_message(self, message):
        message = self.client.messages.create(
        body= message ,
        from_=TWILIO_VIRTUAL_NUMBER,
        to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

