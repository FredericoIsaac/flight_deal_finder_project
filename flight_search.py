import requests


API_KEY_TEQUILA = ""


class FlightSearch:
    def __init__(self, city):
        self.city = city
        self.url = "https://tequila-api.kiwi.com"

        self.header = {
            "apikey": API_KEY_TEQUILA,
        }


    def get_iata_code(self):
        parameters = {
            "term": self.city["city"],
            "location_types": "city"
        }
        response = requests.get(url=f"{self.url}/locations/query", headers=self.header, params=parameters)
        response.raise_for_status()
        iata_data = response.json()
        iata_code = iata_data["locations"][0]["code"]
        self.city["iataCode"] = iata_code