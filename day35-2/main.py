import os
import requests
from twilio.rest import Client


API_KEY = os.environ['OPENWEATHER_APIKEY']
LAT = 38.059775
LON = 138.448874

param = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=param)
res.raise_for_status()

hourly_whether_data = res.json()["hourly"][:12]
need_umbrella = False
for data in hourly_whether_data:
    for whether_detail in data["weather"]:
        if int(whether_detail["id"]) < 700:
            need_umbrella = True

if need_umbrella:
    print("bring an umbrella!!")
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="bring an umbrella!!",
                         from_='+11',
                         to='+11'
                     )
else:
    print("No rain")