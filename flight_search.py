import requests
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = 'T6z77lnFtgtuDg1QNHIUmLHKUj8bJngP'
        self.search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.headers = {
         'apikey': self.api_key}
        self.search_data = {}


    def search_flights(self, city_from, city_to, max_price):
        today = dt.now()
        month_6 = today + relativedelta(months=6)
        today = today.strftime("%Y-%m-%d")
        month_6 = month_6.strftime("%Y-%m-%d")
        search_param = {
            "fly_from": city_from,
            "fly_to": city_to,
            "date_from": today,
            "date_to": month_6,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "AUD",
            "price_to": max_price,
            "selected_cabins": "M"
        }
        res = requests.get(self.search_endpoint, params = search_param, headers= self.headers)
        res.raise_for_status()
        res.status_code
        self.search_data = res.json()
        if len(self.search_data.get("data")) == 0:
            return False
        else:
            return True

    def get_flight_details(self):
        flight_data = FlightData(
        self.search_data["data"][0]["price"],
        self.search_data["data"][0]["cityFrom"],
        self.search_data["data"][0]["flyFrom"],
        self.search_data["data"][0]["cityTo"],
        self.search_data["data"][0]["flyTo"],
        self.search_data["data"][0]["route"][0]["local_departure"].split('T')[0],
        self.search_data["data"][0]["route"][1]["local_departure"].split('T')[0],
        self.search_data["data"][0]["deep_link"]
        )        

        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
        
