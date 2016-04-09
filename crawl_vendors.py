import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import time,csv,datetime


fi = open('vendor_outlinks.txt','r')
ofile  = open("vendor_details_9.csv", "a+b")
c = csv.writer(ofile)
c.writerow(["SerialN","Name","Ratings","Price","Condition","Date"])
ofile.close()
date = datetime.date.today()

for i in fi.readlines():
	link = "http://www.amazon.in/" + i.split(" ")[1].strip()
	serial = i.split(" ")[0].strip()
	try:
		new_r = requests.get(link,verify = False)
		print link
		new_data = new_r.text 
		new_soup = BeautifulSoup(new_data)
		all_offers = new_soup.findAll("div",{"role":"main"})
		l_offers = all_offers[0].findAll("div",{"class":"olpOffer"})
		for offer in l_offers:
			try:
				price = offer.find("span",{"class":"olpOfferPrice"}).text.strip().encode('utf-8')
			except:
				price = None
			try:
				cond = offer.find("span",{"class":"olpCondition"}).text.strip().encode('utf-8')
			except:
				cond = None
			try:	
				name = offer.find("h3",{"class":"olpSellerName"}).text.strip().encode('utf-8')
			except:
				name = None
			try:
				rating = offer.find("i",{"class":"a-icon-star"}).text.strip().encode('utf-8')
			except : 
				rating = None
			print serial,price,cond,name,rating
			ofile  = open("vendor_details_9.csv", "a+b")
			c = csv.writer(ofile)
			c.writerow([serial,name,rating,price,cond,date])
			ofile.close()

	except:
		pass