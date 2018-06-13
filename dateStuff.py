import datetime
import time
#dateStamp = datetime.datetime()
#theMonth = dateStamp.month
#theDate = dateStamp.strftime('%Y_%m_%d')

#print(theMonth)
theDay = "2017207"
theDayStamp = time.strptime(theDay, "%Y%j")
#print(datetime.datetime.now().strftime('%Y_%m_%d'))
print(time.strftime("%Y%m%d", theDayStamp))
