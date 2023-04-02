from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'keys.json'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME):
        self.creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.df = None
        self.dict = {}
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()
        self.SAMPLE_SPREADSHEET_ID = SAMPLE_SPREADSHEET_ID
        self.SAMPLE_RANGE_NAME = SAMPLE_RANGE_NAME


    def get_data(self):
        # Call the Sheets API
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                    range=self.SAMPLE_RANGE_NAME).execute()
        self.df = result.get('values', [])
        # self.df = pd.DataFrame(values)
        
        return self.df
    
    def write_data(self, RANGE_NAME, data):
        request = self.sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, 
                                        range=f"A{RANGE_NAME}", valueInputOption="USER_ENTERED", 
                                        body={"values":data})
        request.execute()
    
    def get_city(self):
        self.get_data()
        return self.df["City"]
    
    def get_city_code(self):
        self.get_data()
        return self.df["IATA Code"]

    def get_price(self, city):
        self.get_data()
        for value in self.df:
            if value[1] == city:
                price = value[-1]

        return price
