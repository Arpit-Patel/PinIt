import requests, json, os

def getTwitter(hashtag, count):
  cnt=0
  urls=[]
  url='https://api.twitter.com/1.1/search/tweets.json?q=%23' + hashtag
  headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAADtO2AAAAAAAfih8%2FpRhXRp5L6IPZYqNH0mn4Gg%3DKSoXjRQo2AgfYtKKwfgNyWkYEvfub6frbY9ykCJ5zkz0kjzxWm'}
  r = requests.get(url,headers=headers)
  data=r.json()
  for a in data['statuses']:
    fullurl = "https://twitter.com/"+a['user']['screen_name']+"/status/"+str(a['id'])
    urls.append(fullurl)
    cnt+=1
    if cnt >= 5:
      break

  return urls