import os
import datetime as dt
import requests
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    HEADER = {
        "apikey": os.getenv("KIWI_APIKEY")
    }

    FLIGHT_SEARCH_END_POINT = "https://tequila-api.kiwi.com/v2/search"
    LOCATION_END_POINT = "https://tequila-api.kiwi.com/locations/query"

    def search_flight(self, origin_city_cd, destination_city_cd):
        tomorrow = dt.datetime.now() + dt.timedelta(1)
        six_month_later = dt.datetime.now() + dt.timedelta(180)

        param = {
            "fly_from": origin_city_cd,
            "fly_to": destination_city_cd,
            "dateFrom": tomorrow.strftime("%d/%m/%Y"),
            "dateTo": six_month_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        res = requests.get(url=self.FLIGHT_SEARCH_END_POINT, params=param, headers=self.HEADER)
        res.raise_for_status()

        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No frights found from {origin_city_cd} to {destination_city_cd}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport_code=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}:€{flight_data.price}")
        return flight_data


    def fill_iata_code(self, city_data):
        res_list = []
        for data in city_data:
            param = {
                 "term": data["city"],
                 "location_types": "city"
            }
            res = requests.get(url=self.LOCATION_END_POINT, params=param, headers=self.HEADER)
            res.raise_for_status()
            data["iataCode"] = res.json()["locations"][0]["code"]
            res_list.append(data)
        return res_list
