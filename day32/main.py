# import smtplib
#
# my_email = "mail@mail.com"
#
# with smtplib.SMTP("smtp.mail.com", port=111) as connection :
#     connection.starttls()
#     connection.login(user=my_email, password="password")
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Hello")
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

day_of_birth = dt.datetime(year=1986, month=12, day=2)
print(day_of_birth)