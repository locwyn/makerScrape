#!/user/bin/env python
import os
import sys
import time
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from emailInfo import *

def checkForNewErrorLog(fileName):
  if os.path.isfile(fileName):
    timeAnHourAgo = time.time() - (60 * 60)
    stat = os.stat(fileName)
    if stat.st_mtime >= timeAnHourAgo:
      print("Updated Error Log Exists. Sending EMail.")
      sendEmail(fileName)
    else:
      print("Old Error Log Exists")
  else:
    print("No Error Log Exists")

def sendEmail(fileName):
  fromaddr = fromAddress
  toaddr = toAddress
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "MakerTweets: New Error Detected"
  body = "New Error logged in " + fileName
  msg.attach(MIMEText(body, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(fromaddr, emailPassword)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

if __name__ == "__main__":
  fileName = datetime.datetime.now().strftime('%Y_%m_%d') + '_error.log'
  checkForNewErrorLog(fileName)
