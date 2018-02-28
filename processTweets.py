import json

with open('2018_27_02_maker,json') as f:
  tweets = f.readlines()

tjson = json.loads(tweets[0])
print(tjson['id'])
