import requests, json, os

def getTwitter(hashtag, count):
  tBlock=[]
  url='https://api.twitter.com/1.1/search/tweets.json?q=%23' + hashtag
  headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAADtO2AAAAAAAfih8%2FpRhXRp5L6IPZYqNH0mn4Gg%3DKSoXjRQo2AgfYtKKwfgNyWkYEvfub6frbY9ykCJ5zkz0kjzxWm'}
  r = requests.get(url,headers=headers)
  data=r.json()
  for a in data['statuses']:
    fullurl = "https://twitter.com/"+a['user']['screen_name']+"/status/"+str(a['id'])
    full = requests.get(fullurl)
    tBlock.append(full.json()['html'].replace("//platform.twitter","https://platform.twitter"))
    count+=1
    if count == 5:
      break

  return tBlock
