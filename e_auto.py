import pandas as pd
import smtplib

SenderAddress = input("Enter your email: ")
password = input("enter your one time password: ")
file = input('Enter the File Name: ')

e = pd.read_excel(file)
emails = e['emails'].values
names = e['names'].values
# for email,name in zip(emails,names):
#     print("name: ",name.split(" ")[0]," email:",email)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)

for email,name in zip(emails,names):
    subject = "Looking for a graphic designer"
    msg = f'''Hi {name.split(" ")[0]}, 
    Text here'''

    body = "Subject: {}\n\n{}".format(subject,msg)
    server.sendmail(SenderAddress, email, body)
    print("done")
server.quit()
