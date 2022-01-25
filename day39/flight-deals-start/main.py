#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

fs = FlightSearch()
# fs.search_flight()
dm = DataManager()
loaded_sheet_data = dm.load_sheet_data()
iata_list = fs.fill_iata_code(loaded_sheet_data)
dm.update_sheet_data(iata_list)