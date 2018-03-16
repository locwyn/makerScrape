import json

with open('2018_03_14_maker.json') as f:
  tweets = f.readlines()

count = 0
"""
for x in tweets:
  tjson = json.loads(x)
  if tjson['user']['followers_count'] >= 2000:  
    try:
      tjson['retweeted_status']
    except KeyError:    
      count += 1
"""
for y in tweets:
#  tjson = json.loads(y)
  if 'retweeted_status' in y:
    count += 1

print(count)
