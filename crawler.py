

import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import time



for j in xrange(25, 74): 	
	time.sleep(5)
	new_r = requests.get('http://www.amazon.in/s/ref=lp_4916280031_pg_2?rh=n%3A976419031%2Cn%3A%211499770031%2Cn%3A%211499772031%2Cn%3A4916280031&page='+ str(j)+'&ie=UTF8&qid=1458934390',verify = False)
	new_data = new_r.text 
	new_soup = BeautifulSoup(new_data) #make the soup!
	#print new_soup
	main_class = new_soup.findAll("div",{"class" : "s-result-list-parent-container"})
	#print len(main_class)
	if(len(main_class) > 0):
		names = main_class[0].findAll("ul")
		for name in names:
			lis = name.findAll('li',{"class": "s-result-item"})
			if len(lis):
				for item in lis:
					link = item.find("a",{"class": "a-link-normal"})
					print link['href']
			else :
				pass
				
	else:
		print 'data khatam'
		break
	
#except Exception as e:
#	print e
#	pass


		
	