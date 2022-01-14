import requests

API_KEY = "b2c7a4738c612e61783a2ade1c569445"
LAT = 35.694706
LON = 139.982620

param = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=param)
res.raise_for_status()
print(res.json()["hourly"])
