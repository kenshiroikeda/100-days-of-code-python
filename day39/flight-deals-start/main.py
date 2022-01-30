# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()

dm.login()

distination_list = fs.get_iata_code(dm.load_price_data())
dm.fill_iata_code(distination_list)

for destination in distination_list:
    flight = fs.search_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"]
    )
    if flight.price < destination["lowestPrice"]:
        nm.sendFlightDetailEmail(flight, dm.user_data["email"])

