#!/user/bin/env python3
import os
import sys
import time
import datetime

def checkForNewErrorLog(fileName):
  if os.path.isfile(fileName):
    timeAnHourAgo = time.time() - (60 * 60)
    stat = os.stat(fileName)
    if stat.st_mtime >= timeAnHourAgo:
      print("Updated Error Log Exists")
    else:
      print("Old Error Log Exists")
  else:
    print("No Error Log Exists")

if __name__ == "__main__":
  fileName = datetime.datetime.now().strftime('%Y_%m_%d') + '_error.log'
  checkForNewErrorLog(fileName)
