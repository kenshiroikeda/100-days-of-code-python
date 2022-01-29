import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    PRICES_END_POINT = os.getenv("SHEETY_END_POINT")
    USER_END_POINT = os.getenv("SHEETY_USERS_END_POINT")

    header = {
        "Authorization": os.getenv("SHEETY_APIKEY")
    }

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def load_price_data(self):
        res = requests.get(url=self.PRICES_END_POINT, headers=self.header)
        res.raise_for_status()
        sheet_data_list = res.json()["prices"]
        self.destination_data = sheet_data_list
        return self.destination_data

    def load_user_data(self):
        res = requests.get(url=self.USER_END_POINT, headers=self.header)
        res.raise_for_status()
        self.user_data = res.json()["users"]
        print(self.user_data)

    def update_sheet_data(self, data_list):
        for idx in range(len(data_list)):
            put_url = self.PRICES_END_POINT + "/" + str(idx + 2)
            sheet_data = data_list[idx]
            json_put = {
                "price": sheet_data
            }
            res = requests.put(url=put_url, json=json_put, headers=self.header)
            res.raise_for_status()

    def login(self):
        self.load_user_data()
        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        email = self.validate_email()
        created = False
        for data in self.user_data:
            if first_name == data["firstName"] and \
                    last_name == data["lastName"] and \
                    email == data["email"]:
                created = True
                print("You are in the club!!")
        if not created:
            self.create_user(first_name, last_name, email)

    def validate_email(self):
        email_1st = input("What is your email?")
        email_2nd = input("Type your email again.")
        if email_1st == email_2nd:
            return email_1st
        else:
            return self.validate_email()

    def create_user(self, first_name, last_name, email):
        user_param = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        res = requests.post(url=self.USER_END_POINT, json=user_param, headers=self.header)
        res.raise_for_status()
        print("Your user is registred!!")



