import os
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    def sendFlightDetailMessage(self, flight_detail: FlightData):
        content = f"Low Price Alart!Only{flight_detail.price} to fly from {flight_detail.departure_city}-" \
                  f"{flight_detail.departure_airport_code} to {flight_detail.destination_city}-" \
                  f"{flight_detail.destination_airport_code}, from {flight_detail.out_date} to from " \
                  f"{flight_detail.return_date}"
        message = self.client.messages.create(
            body=content,
            from_='+11',
            to='+11'
        )