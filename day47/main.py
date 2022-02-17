import os
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "ITEM_URL"
HEADER = {
    "Accept-Language":"ja,en-US;q=0.9,en;q=0.8",
    "User-Agent": os.getenv("USER_AGENT")
}
MY_EMAIL = "from@mail.com"
TO_EMAIL = "to@mail.com"
TARGET_VALUE = 38000

res = requests.get(url=URL, headers=HEADER)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
current_value = int(soup.find(class_="a-price-whole").text.replace(",",""))

if current_value < TARGET_VALUE:
    with smtplib.SMTP("smtp.mail.com", port=111) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password="password")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:AmazonPriceAlart\n\nNow is the time to buy the item!! "
                                f"current price is {current_value}")

