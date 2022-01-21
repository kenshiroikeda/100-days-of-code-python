import datetime
import os
import requests

API_KEY = os.getenv("NUT_APIKEY")
APP_ID = os.getenv("NUT_APP_ID")
POST_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
POST_SHEETY_URL = os.getenv("POST_SHEETY_URL")
input_txt = input("Tell me which exercise you did")

header_param = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "ken_ike"
}

request_param = {
    "query": input_txt,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

res = requests.post(url=POST_URL, json=request_param, headers=header_param)
res.raise_for_status()

sheety_header_param = {
    "Authorization": os.getenv("SHEETY_AUTH"),
    "Content-Type":  "application/json"
}

now = datetime.datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%I:%M:%S %p")


for data in res.json()["exercises"]:
    sheety_param = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    res_sheety = requests.post(url=POST_SHEETY_URL, json=sheety_param, headers=sheety_header_param)
    res_sheety.raise_for_status()

