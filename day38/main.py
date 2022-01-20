import os
import requests

API_KEY = os.getenv("NUT_APIKEY")
APP_ID = os.getenv("NUT_APP_ID")
POST_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(res.text)


