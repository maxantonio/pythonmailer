# smtplib library for mails
import smtplib

# importing smtp configuration
from config import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "me@gmail.com"
you = "to@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
#reading html
with open('file.html', 'r') as f:
    html = f.read()


# Record the MIME types of both parts - text/plain and text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.

msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP(connection.server, connection.port)

mail.ehlo()

mail.starttls()

mail.login(connection.user_name, connection.password)
mail.sendmail(me, you, msg.as_string())
mail.quit()
