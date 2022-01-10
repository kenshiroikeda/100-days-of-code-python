from time import sleep

import requests
import smtplib
from datetime import datetime

MY_LAT = 35.690600  # Your latitude
MY_LONG = 140.001480  # Your longitude
ADJUST_JST = 9
MY_EMAIL = "hoge@mail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_iss_overhead():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        print("ISS is far from your city...")
        return False


def is_night():
    res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    json_data = res.json()
    sunrise = (int(json_data["results"]["sunrise"].split("T")[1].split(":")[0]) + ADJUST_JST) % 24
    sunset = (int(json_data["results"]["sunset"].split("T")[1].split(":")[0]) + ADJUST_JST) % 24
    time_now = datetime.now()
    if sunrise < time_now.hour < sunset:
        return True
    else:
        print("Your city is in the night...")
        return False


def notify_iss_watchable():
    # If the ISS is close to my current position
    # and it is currently dark
    if is_iss_overhead() and is_night():

    # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.mail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password="password")
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="mail@mail.com",
                                msg=f"Subject:Look up the sky!!\n\nYou can see ISS in the sky!!")

    # BONUS: run the code every 60 seconds.
    sleep(60)
    notify_iss_watchable()


notify_iss_watchable()