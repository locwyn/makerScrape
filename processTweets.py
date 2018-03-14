import json

with open('2018_03_01_maker.json') as f:
  tweets = f.readlines()

count = 0

for x in tweets:
  tjson = json.loads(x)
  if (tjson['retweeted_status']):
    count += 1

print(count)
