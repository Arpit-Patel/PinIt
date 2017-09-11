from hashtags import getTwitterId
import time
while True:
	print "updating"
	file = open("stuff.txt",'w')
	for a in getTwitterId():
		file.write(a+'\n')
	file.close()
	print "sleeping"
	time.sleep(5)