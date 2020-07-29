#!/usr/bin/python

import smtplib

#The smtp module (Simple Mail Transfer Protocol) enables sending emails in python
#The sender's email must be configured to less secure apps.
#This configuration can be made on visiting account information.
#Under the category security, less secure apps must turned on

#"Sender's Email-ID"
sender_email = "removirtual@gmail.com"

#"Receiver's Email-ID"
receiver = "nowitsharder@gmail.com"

#"Sender's password"
password = "removirtual123$"

#"Subject of the Email"
subject = "Interview confirmation"

#"Content of the email"
body_of_the_email = input("Enter the content of the email : ")

content = "Subject: {}\n\n{}".format(subject, body_of_the_email)

#Specifications of the Email

server = smtplib.SMTP("smtp.gmail.com" , 587)

#Here the Gmail service is used, a different Email service can also be used
#The port 587, across which the email is sent

server.starttls()
server.login(sender_email, password)

#Login is authorised

print("Login success")

server.sendmail(sender_email, receiver, content)
print("Email sent to the receiver")

#Email is sent, prints success on sending the email
