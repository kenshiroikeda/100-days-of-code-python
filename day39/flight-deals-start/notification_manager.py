import os
import smtplib

from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    def get_message(self, flight_detail: FlightData):
        content = f"Low Price Alart! Only{flight_detail.price} to fly from {flight_detail.departure_city}-" \
                  f"{flight_detail.departure_airport_code} to {flight_detail.destination_city}-" \
                  f"{flight_detail.destination_airport_code}, from {flight_detail.out_date} to from " \
                  f"{flight_detail.return_date}"
        if flight_detail.stop_over > 0:
            content += f"\nFlight has {flight_detail.stop_over} stop over, via {flight_detail.via_city}."
        return content

    def sendFlightDetailMessage(self, flight_detail: FlightData):
        content = self.get_message(flight_detail)
        message = self.client.messages.create(
            body=content,
            from_='+11',
            to='+11'
        )

    def sendFlightDetailEmail(self, flight_detail: FlightData, to_email):
        with smtplib.SMTP("smtp.mail.com", port=111) as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password="password")
            connection.sendmail(from_addr=os.getenv("MY_EMAIL"), to_addrs=to_email,
                                content=self.get_message(flight_detail))
