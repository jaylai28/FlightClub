import requests

tequila_endpoint = 'https://api.tequila.kiwi.com/locations/query'
api_key = 'API_KEY'
headers = {'Accept': 'application/json',
        'apikey': api_key
        }

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, flight_url):
        self.IATA_Code = None
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.flight_url = flight_url

    def get_location(self, city):
        tequila_params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"
        }
        response = requests.get(tequila_endpoint, params = tequila_params, headers = headers)
        response.raise_for_status()
        data = response.json()["locations"]
        self.IATA_Code = data[0]["code"]
        return self.IATA_Code

