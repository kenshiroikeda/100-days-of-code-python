import smtplib

my_email = "mail@mail.com"

with smtplib.SMTP("smtp.mail.com", port=111) as connection :
    connection.starttls()
    connection.login(user=my_email, password="password")
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Hello")


