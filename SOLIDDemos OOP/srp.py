import sqlite3
from sqlite3 import Error

class User:
    def RegisterUser(self, uname, passwd, email ):
        con = sqlite3.connect('sqldb.db')
        sql = "insert into Users values ('{0}','{1}','{2}')".format(uname,passwd,email)
        con.execute(sql)
        con.commit()
        print(f"User Registered with {uname} and {passwd}")
       
import syslog
class Logger:
    def WriteLogToSystem(self, message):
        syslog.syslog(syslog.LOG_ERR, message)


import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def SendEmail(self, to_email, message_content,subject='User Registered') :
        with open('credentials.json') as f:
            data = json.load(f)

        smtp_server = "smtp.gmail.com"
        port = 465
        sender_email = data["fromuser"]
        password = data["password"]

        context = ssl.create_default_context()
        message = MIMEMultipart("alternative")

        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message_content = f'Hello, <br/><b>Message from TechnoAcademy: </b> <br/> {message_content} <br/>All The Best <br/>Best Wishes, <br />TechnoAcademy.net Support Team'

        part = MIMEText(message_content,"html")

        message.attach(part)

        with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
            server.login(sender_email , password)
            server.sendmail(sender_email,to_email,message.as_string())

        print(f"Mail Sent to {to_email}")

class Registrations:
    def RegisterUser(self, uname, pwd, email):
        try:
            User().RegisterUser(uname, pwd, email)
            Email().SendEmail(email, 'You have Successfully Registered')
        except Exception:
            Logger().WriteLogToSystem('Error While Registering User')


r = Registrations()
r.RegisterUser('sekhar', 'srinivasan', 'sekharonline4u@gmail.com')

