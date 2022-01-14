import requests

API_KEY = "xxx"
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
