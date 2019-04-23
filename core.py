# smtplib library for mails
import smtplib

# importing smtp configuration
from config import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Class for smtp configuration
class SmtpConfig:

    def __init__(self, server, port, user_name, password):
        self.server = server
        self.port = port
        self.user_name = user_name
        self.password = password

# conection setup
connection = SmtpConfig(smtp_server, smtp_port, smtp_username, smtp_password)

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')

def content(file):


    with open(file, 'r') as f:
        html = f.read()
        # Create the body of the message (a plain-text and an HTML version).
        #reading html

        # Record the MIME types of both parts - text/plain and text/html.
        mail_content = MIMEText(html, 'html')
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.

        msg.attach(mail_content)



# conect and Send the message via local SMTP server.
mail = smtplib.SMTP(connection.server, connection.port)

mail.ehlo()

mail.starttls()

mail.login(connection.user_name, connection.password)
