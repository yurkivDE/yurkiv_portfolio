import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "yuriy.yurkiv.db@gmail.com"
password = "zymlgatyawcoaleg"

receiver = "yuriy.yurkiv.db@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Contact Me from Portfolio app
!!!!!!!!!!!!!!!!!!!
This is test email
from  my app
!!!!!!!!!!!!!!!!!!!
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)