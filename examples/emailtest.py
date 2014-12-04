#!/usr/bin/python

import time

message = "These are the new users that signed up today."

daystring = time.strftime("%Y-%m-%d")
#daystring = '2014-08-23'

message = message + "\n\nMessage generated from src/wui/syschecks/newusers.py\n"

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# Create a text/plain message
msg = MIMEText(message)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "SGStatus: New users for " + daystring 
msg['From'] = 'dane@awr.com'
msg['To'] = 'dane@awr.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('us-cam-mail-queue')
s.sendmail("dane@awr.com", ['dane@awr.com'], msg.as_string())
s.quit()

