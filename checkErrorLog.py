
import os
import sys
import time

def checkForNewErrorLog(fileName):
  if os.path.isfile(fileName):
    print("New Error Log Exists")
  else:
    print("No, New Logs")

if __name__ == "__main__":
  fileName = 
  checkForNewErrorLog(fileName)
