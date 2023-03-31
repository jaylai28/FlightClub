import requests
from datetime import datetime
from twilio.rest import Client
import os

ACCOUNT_SID = "AC0a193f5908f9f803c34bd25e0347e56b"
AUTH_TOKEN = "4207c348e172013b4b85c5932966c821"
TWILIO_VIRTUAL_NUMBER = "+15627849971"
TWILIO_VERIFIED_NUMBER = "+61435333962"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)


    def send_message(self, message):
        print(message)

        
        # message = self.client.messages.create(
        # body= message ,
        # from_=TWILIO_VIRTUAL_NUMBER,
        # to=TWILIO_VERIFIED_NUMBER
        # )
        # print(message.sid)

