import smtplib
import ssl


def send_email(visitor_email, visitor_message):
    host = "smtp.gmail.com"
    port = 465

    username = "yuriy.yurkiv.db@gmail.com"
    password = "zymlgatyawcoaleg"

    receiver = "yuriy.yurkiv.db@gmail.com"

    context = ssl.create_default_context()

    message = f"""Subject: Portfolio app - {visitor_email}
    
{visitor_message}

{visitor_email}
    """

    print(message)

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message)