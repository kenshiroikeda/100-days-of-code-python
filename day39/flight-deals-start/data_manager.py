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
        sheet_data_list = res.json()["prices"]
        return sheet_data_list

    def update_sheet_data(self, data_list):
        for idx in range(len(data_list)):
            put_url = self.END_POINT + "/" + str(idx+2)
            sheet_data = data_list[idx]
            json_put = {
                "price": sheet_data
            }
            res = requests.put(url=put_url, json=json_put, headers=self.header)
            res.raise_for_status()

