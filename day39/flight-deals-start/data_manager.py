import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    END_POINT = os.getenv("SHEETY_END_POINT")

    header = {
        "Authorization": os.getenv("SHEETY_APIKEY")
    }

    def load_sheet_data(self):
        res = requests.get(url=self.END_POINT, headers=self.header)
        res.raise_for_status()
        print(res.json())