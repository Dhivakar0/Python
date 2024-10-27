import smtplib
import datetime as dt
import random

my_email = "pythontestingku@gmail.com"

password = "bfwtawemsvrruiue"

# with smtplib.SMTP(host= "smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email, to_addrs= "pythontestingkudaan@yahoo.com",
#         msg="Subject: Testing mail \n\n This is testing mail created using Python smtlib"
#     )

now = dt.datetime.now()

weekday = now.weekday()

if weekday == 5:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = my_email, password= password)
            connection.sendmail(from_addr= my_email, to_addrs= "pythontestingkudaan@yahoo.com",
                                msg = f"Subject: Motivation \n\n  Here is your motivation quote to start your day! Have a nice day!\n {quote}")