##################### Extra Hard Starting Project ######################
import os
import random
import smtplib
import datetime as dt
import pandas as pd

MY_EMAIL = "from@mail.com"


# 4. Send the letter generated in step 3 to that person's email address.
def sendMessage(dict_send_message):
    for data in dict_send_message:
        content_filename = random.choice(os.listdir("./letter_templates"))
        message = ""
        with open(f"./letter_templates/{content_filename}") as file:
            lines = file.readlines()
            for line in lines:
                message += line.replace("[NAME]", data["name"])
            print(message)

        with smtplib.SMTP("smtp.mail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password="password")
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=data["email"], msg=f"Subject:Happy BirthDay!!\n\n{message}")

# 2. Check if today matches a birthday in the birthdays.csv
dict_birthday = pd.read_csv("birthdays.csv").to_dict(orient='records')
dict_celebration = []

month = dt.datetime.now().month
day = dt.datetime.now().day
for birth_data in dict_birthday:
    if birth_data['month'] == month and birth_data['day'] == day:
        dict_celebration.append(birth_data)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(dict_celebration) > 0:
    sendMessage(dict_celebration)
else:
    print("There is no friends whose birthday is today.")









