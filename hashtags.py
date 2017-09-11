import requests,json,os

try:
	os.remove('testinghtml.html')
except WindowsError:
	print "error"
url='https://api.twitter.com/1.1/search/tweets.json?q=%23hackthe6ix'
headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAADtO2AAAAAAAfih8%2FpRhXRp5L6IPZYqNH0mn4Gg%3DKSoXjRQo2AgfYtKKwfgNyWkYEvfub6frbY9ykCJ5zkz0kjzxWm'}
r = requests.get(url,headers=headers)
data=r.json()
file=open('testinghtml.html','w')
file.write('<html><head><title>TwitterTest</title></head><body>\n')
#print data['statuses'][0]['user']['screen_name']
#print data['statuses'][0]['id']
for a in data['statuses']:
	fullurl = "https://publish.twitter.com/oembed?url=https://twitter.com/"+a['user']['screen_name']+"/status/"+str(a['id'])
	full = requests.get(fullurl)
	file.write(full.json()['html'].replace("//platform.twitter","https://platform.twitter"))
#print full.json()['html']
file.write('</body></html>')
file.close()

def getTwitter():
	b=[]
	url='https://api.twitter.com/1.1/search/tweets.json?q=%23hackthe6ix'
	headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAADtO2AAAAAAAfih8%2FpRhXRp5L6IPZYqNH0mn4Gg%3DKSoXjRQo2AgfYtKKwfgNyWkYEvfub6frbY9ykCJ5zkz0kjzxWm'}
	r = requests.get(url,headers=headers)
	data=r.json()
	for a in data['statuses']:
		fullurl = "https://twitter.com/"+a['user']['screen_name']+"/status/"+str(a['id'])
		b.append(fullurl)
	return b

def getTwitterId():
	b=[]
	url='https://api.twitter.com/1.1/search/tweets.json?q=%23hackthe6ix'
	headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAADtO2AAAAAAAfih8%2FpRhXRp5L6IPZYqNH0mn4Gg%3DKSoXjRQo2AgfYtKKwfgNyWkYEvfub6frbY9ykCJ5zkz0kjzxWm'}
	r = requests.get(url,headers=headers)
	data=r.json()
	for a in data['statuses']:
		fullurl = a['user']['screen_name']+" "+str(a['id'])
		b.append(fullurl)
	return b

