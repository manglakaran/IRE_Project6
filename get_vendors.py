import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import time,csv,datetime

fi = open('out_links_final.txt','r')
readlist = []
for i in fi.readlines():
	readlist.append(i.strip())
date = datetime.date.today()
serial=0

for link in readlist:
	serial +=1
	cnt = {}
	time.sleep(2)
	#link = "http://www.amazon.in/Lava-P7-Blue-Black/dp/B01B7PEWDC"
	try:
		new_r = requests.get(link,verify = False)
		#print link
		new_data = new_r.text 
		new_soup = BeautifulSoup(new_data)
		#print new_soup
		vendor_class = new_soup.findAll("div",{"id":"olp_feature_div"})
		print str(serial) + " " + vendor_class[0].find('a')['href']
		#break
	except Exception as e:
		print str(serial) + " " + "##"