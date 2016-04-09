import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import time,csv,datetime

fi = open('out_links_final.txt','r')
readlist = []
for i in fi.readlines():
	readlist.append(i.strip())
date = datetime.date.today()
serial =0

for link in readlist:
	serial +=1
	if(serial > 854):
		time.sleep(5)
		try:
			new_r = requests.get(link,verify = False)
			#print link
			new_data = new_r.text 
			new_soup = BeautifulSoup(new_data)
			image_class = new_soup.find('div',{'id':'imageBlock_feature_div'}).find('div',{'id':'imgTagWrapperId'}).find('img')
			print str(serial) + " " + image_class['src']
			
			
		except:
			print str(serial) + " " + '##'
	else:
		pass