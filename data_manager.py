import requests


TOKEN = ""


class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/"
        self.header = {
            "Authorization": f"Bearer {TOKEN}"
        }
        self.sheet_data = self.get_data()["prices"]

    def get_data(self):
        response = requests.get(url=self.url, headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data

    def put_data(self, city_data):
        row_id = city_data["id"]
        new_data = {"price": city_data}
        response = requests.put(url=f"{self.url}/{row_id}", headers=self.header, json=new_data)
