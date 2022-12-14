import smtplib
import datetime as dt
import random

my_email = "manafreedom@gmail.com"
password = "deptazfajupzldvx"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="serenagolucky@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )
