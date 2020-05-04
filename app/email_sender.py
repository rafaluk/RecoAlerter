import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(login, password, recipient, subject, message, config):

    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(login, password)

    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)
    print(f'Email sent to {recipient}.')
    server.quit()

    del msg

