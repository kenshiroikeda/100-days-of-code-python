import os
import datetime as dt
import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    HEADER = {
        "apikey": os.getenv("KIWI_APIKEY")
    }

    FRIGHT_SEARCH_END_POINT = "https://tequila-api.kiwi.com/v2/search"
    LOCATION_END_POINT = "https://tequila-api.kiwi.com/locations/query"

    def search_flight(self):
        fly_from = input("Please input your departure airport...   : ")
        fly_to = input("Please implement se input your destination airport...   : ")
        tomorrow = dt.datetime.now() + dt.timedelta(1)
        six_month_later = dt.datetime.now() + dt.timedelta(180)

        param = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": tomorrow.strftime("%d/%m/%Y"),
            "dateTo": six_month_later.strftime("%d/%m/%Y"),
        }

        res = requests.get(url=self.FRIGHT_SEARCH_END_POINT, params=param, headers=self.HEADER)
        res.raise_for_status()
        print(res.json())

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
