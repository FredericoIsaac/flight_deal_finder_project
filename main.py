from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


from pprint import pprint

# Create Instance
sheet = DataManager()

# Get sheet data
sheet_data = sheet.sheet_data


# pprint(sheet_data)

# Check if IATA CODES empty

for city in sheet_data:
    if not city["iataCode"]:
        flight_searcher = FlightSearch(city)
        flight_searcher.get_iata_code()
        sheet.put_data(city)

    flight_search = FlightData(city)
    flight_price = flight_search.price

    flight_info = {
        "price": flight_search.price,
        "from_code": flight_search.flyfrom_code,
        "from_name": flight_search.flyfrom_name,
        "to_code": flight_search.flyto_code,
        "to_name": flight_search.flyto_name,
    }

    print(city)
    if city["lowestPrice"] > flight_info["price"]:
        sms = NotificationManager(flight_info)
