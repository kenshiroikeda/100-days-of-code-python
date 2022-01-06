import smtplib
import datetime as dt
import random

MONDAY = 1
MY_EMAIL = "from@mail.com"
TO_EMAIL = "to@mail.com"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == MONDAY:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()

    message = random.choice(quotes_list)

    with smtplib.SMTP("smtp.mail.com", port=111) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password="password")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:MondayMotivation\n\n{message}")

else:
    print("Today is not Monday")
