# importing core and  recursively  configuration
from core import *

# me == my email address
# you == recipient's email address
sending_adress = "send@gmail.com"
receiving_address = "receiving@gmail.com"
# message values
msg['Subject'] = "my subject"
msg['From'] = sending_adress
msg['To'] = receiving_address
content('file.html')


# Sending mail
mail.sendmail(sending_adress, receiving_address, msg.as_string())
mail.quit()

#confirming mail
print("Email sent - > congrats")
