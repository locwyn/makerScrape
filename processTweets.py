import json

with open('2018_02_28_maker.json') as f:
  tweets = f.readlines()

for x in tweets:
  tjson = json.loads(x)
  print(tjson['id'])
