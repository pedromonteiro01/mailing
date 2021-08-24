import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

EMAIL_ADDRESS = input('Your email: ')
EMAIL_PASSWORD = getpass('Your password: ')
EMAIL_RECEIVER = input('Receiver email: ')

msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_RECEIVER
msg['Subject'] = input('Subject: ')
body = input('Email body: ')
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()
server.starttls()
server.ehlo()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

text = msg.as_string()
server.sendmail(EMAIL_ADDRESS, EMAIL_RECEIVER, text)
server.quit()