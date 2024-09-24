# import smtplib
# from email.mime.text import MIMEText
#
# sender_email =
# app_specific_password =
#
# subject = "Test Email 2"
# body = "This is a test email sent from Python using iCloud's SMTP server."
# receiver_email =
#
# # Create the email
# msg = MIMEText(body)
# msg['Subject'] = subject
# msg['From'] = sender_email
# msg['To'] = receiver_email
#
# # Send the email
# try:
#     with smtplib.SMTP('smtp.mail.me.com', 587) as server:
#         server.starttls()  # Secure the connection
#         server.login(sender_email, app_specific_password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
#         print("Email sent successfully!")
# except Exception as e:
#     print(f"Failed to send email: {e}")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
# month = now.month
# print(month)
# week = now.weekday()
# print(week)
# day = now.day
# print(day)
#
# date_of_birth = dt.datetime(year=2006, month=5, day=2)
# print(date_of_birth)


# import datetime as dt
# import smtplib
# import random
# from email.mime.text import MIMEText
#
#
# def generate_quote():
#     with open("quotes.txt", "r") as quotes:
#         all_quotes = quotes.readlines()
#     return random.choice(all_quotes)
#
#
# def send_email():
#     sender_email =
#     password =
#     subject = "Quote of the day"
#     body = generate_quote()
#     receiver_mail =
#
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = receiver_mail
#
#     with smtplib.SMTP('smtp.mail.me.com', 587) as server:
#         server.starttls()
#         server.login(user=sender_email, password=password)
#         server.sendmail(to_addrs=receiver_mail, from_addr=sender_email, msg=msg.as_string())
#
#
# if 4 == dt.datetime.now().weekday():
#     send_email()


# # #################### Extra Hard Starting Project ######################
#
# # 1. Update the birthdays.csv
#
# # 2. Check if today matches a birthday in the birthdays.csv
#
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# #   with the person's actual name from birthdays.csv
#
# # 4. Send the letter generated in step 3 to that person's email address.
#
# import datetime as dt
# import smtplib
# from email.mime.text import MIMEText
# import pandas as pd
# from random import randint
#
# now = dt.datetime.now()
# month = now.month
# day = now.day
#
# data = pd.read_csv("birthdays.csv")
# birthday = data[(data["month"] == month) & (data["day"] == day)]
#
# if not birthday.empty:
#     name = birthday["name"].iloc[0]
#     email = birthday["email"].iloc[0]
#     with open(f"letters/letter_{randint(1, 3)}.txt", "r") as letter:
#         birthday_wish = letter.read()
#         birthday_wish = birthday_wish.replace("[NAME]", name)
#
#     sender =
#     receiver = email
#     password =
#     subject = "Happy birthday"
#     body = birthday_wish
#
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg['From'] = sender
#     msg['To'] = receiver
#
#     with smtplib.SMTP('smtp.mail.me.com', 587) as server:
#         server.starttls()
#         server.login(user=sender, password=password)
#         server.sendmail(to_addrs=receiver, from_addr=sender, msg=msg.as_string())
