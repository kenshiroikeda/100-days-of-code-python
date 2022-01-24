#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

# fs = FlightSearch()
# fs.search_flight()
dm = DataManager()
dm.load_sheet_data()