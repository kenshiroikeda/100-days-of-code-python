#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

fs = FlightSearch()
dm = DataManager()
dm.login()

# nm = NotificationManager()
# loaded_sheet_data = dm.load_sheet_data()
#
#
# iata_list = fs.fill_iata_code(loaded_sheet_data)
# dm.update_sheet_data(iata_list)
#
# for destination in iata_list:
#     flight = fs.search_flight(
#         ORIGIN_CITY_IATA,
#         destination["iataCode"]
#     )

