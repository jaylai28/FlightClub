#!/usr/bin/env python3
#This file will need to use the DataManager,FlightSearch, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
from tqdm import tqdm
start_time = time.time()


SAMPLE_SPREADSHEET_ID = '1zWlTSc9HgmXtn96ZK4RsX_EhaVe7aMT3lQITvtj1XIk'
SAMPLE_RANGE_NAME = 'City!A2:D50'

d = DataManager(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
fs = FlightSearch()
nm = NotificationManager()


city_data = d.get_data()

for row in tqdm(city_data):
    if fs.search_flights(row[0], row[2], row[3]):
        flight = fs.get_flight_details()
        nm.send_message(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. LINK BELOW: {flight.flight_url}"
        )

print("Process finished --- %s seconds ---" % (time.time() - start_time))