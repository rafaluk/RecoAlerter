import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManager:
    def __init__(self, login=None, password=None, recipient=None, subject=None, message=None, host="smtp.gmail.com", port=587):
        self.login = login
        self.password = password
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.host = host
        self.port = port

    def prepare(self, unseen_news: list):
        message = ''
        for news in unseen_news:
            message += news + '\n'

    def send(self, login, password, recipient, subject, message):
        server = smtplib.SMTP(host=self.host, port=587)
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
