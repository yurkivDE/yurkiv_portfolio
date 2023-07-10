import smtplib
import ssl
import os


def send_email(visitor_email, visitor_message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("APP_EMAIL")
    password = os.getenv("APP_EMAIL_PASS")

    receiver = os.getenv("APP_EMAIL")

    context = ssl.create_default_context()

    message = f"""Subject: Portfolio app - {visitor_email}
    
{visitor_message}

{visitor_email}
    """

    print(message)

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message)