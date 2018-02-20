from twython import Twython
from twython import TwythonStreamer

APP_KEY = 'dgmlPcoo2F3Ws6LWJLmuTgOVb'
APP_SECRET = 'cME0sSMXOXHO3qG06tEwSyejzvlYlqLzx1ynKRBqGjbuYRIOZz'
ACCESS_TOKEN = '903791836791267328-otZ5372pWtzUDvSEOU9IWeSyPojrnz5'
ACCESS_SECRET = 'cfCMYG8815czjkRljOo1HAvg09pvu9GPyFVMmfKZOI4XD'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
        
stream = MyStreamer(APP_KEY, APP_SECRET,
                    ACCESS_TOKEN, ACCESS_SECRET)
stream.statuses.filter(track='twitter')        
