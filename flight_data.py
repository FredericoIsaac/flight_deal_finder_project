from pprint import pprint

import requests
from datetime import datetime
from datetime import timedelta

API_KEY_TEQUILA = ""


def get_date():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    six_months = today + timedelta(days=6*30)
    six_months = six_months.strftime("%d/%m/%Y")

    return tomorrow, six_months


class FlightData:
    def __init__(self, city):
        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.city = city
        self.departure_city = "LON"

        self.header = {
            "apikey": API_KEY_TEQUILA
        }


        self.trip_lookup = get_date()
        self.flight_data = self.get_flights()
        self.price = self.flight_data["data"][0]["price"]
        self.flyfrom_code = self.flight_data["data"][0]["duration"]["flyfrom"]
        self.flyfrom_name = self.flight_data["data"][0]["duration"]["cityFrom"]
        self.flyto_code = self.flight_data["data"][0]["countryFrom"]["code"]
        self.flyto_name = self.flight_data["data"][0]["countryFrom"]["name"]

    def get_flights(self):
        parameters = {
            "fly_from": self.departure_city,
            "fly_to": self.city["iataCode"],
            "date_from": self.trip_lookup[0],
            "date_to": self.trip_lookup[1],
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=self.url, headers=self.header, params=parameters)
        response.raise_for_status()
        flight_data = response.json()
        return flight_data


