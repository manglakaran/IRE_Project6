import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import time,csv,datetime

fi = open('out_links_final.txt','r')
readlist = []
for i in fi.readlines():
	readlist.append(i.strip())
date = datetime.date.today()

ofile  = open("Product_Catalogue_9.csv", "a+b")
c = csv.writer(ofile)
c.writerow(["SerialN","Name","Ratings","Price",'OS','Colour' ,'RAM','Product Dimensions', 'Connectivity technologies', 'Special features',"Date"])
ofile.close()

scrape_l = ['OS','Colour' ,'RAM','Product Dimensions', 'Connectivity technologies', 'Special features'] 
cnt = dict()
serial = 0
for link in readlist:
	serial +=1
	cnt = {}
	time.sleep(2)
	#link = "http://www.amazon.in/Micromax-Bolt-A71-White/dp/B00I0SL526"
	try:
		new_r = requests.get(link,verify = False)
		print link
		new_data = new_r.text 
		new_soup = BeautifulSoup(new_data)
		title_class = new_soup.findAll("div",{"id":"title_feature_div"})
		#print title_class
		title_name = title_class[0].findAll("span")[0].text
		if title_name:
			name = title_name.encode('utf-8')
		else:
			name = None	
		name = None
		new_soup = BeautifulSoup(new_data)
		rating_class = new_soup.find('div',{'id':'averageCustomerReviews'})
		try:
			rating =  rating_class.select('span > a > i')[0].find('span').text.encode('utf-8')
		except :
			rating = None
		
		new_soup = BeautifulSoup(new_data)
		price_class = new_soup.find('div',{'id':'price_feature_div'})
		#print price_class
		price1 = None
		try:
			price = price_class.find('span',{'id':'priceblock_saleprice'}).text.strip().encode('utf-8')
			if price == "":
				price1 = price_class.find('span',{'id':'priceblock_ourprice'}).text.strip().encode('utf-8')
		except:
			try:
				price =  price_class.find('span').text.strip().encode('utf-8')
				if price == "":
					price1 = price_class.find('span',{'id':'priceblock_ourprice'}).text.strip().encode('utf-8')
			except:
				price =  None
		if price == "" or price == None:
			price = price1
		new_soup = BeautifulSoup(new_data)
		table = new_soup.find('div',{'class':'pdTab'}).find('table')
		for row in table.findAll("tr"):
			cells = row.findAll("td")
			if 	cells[0].text.strip() in scrape_l:
				cnt[cells[0].text.strip()] = cells[1].text.strip()
		for item in scrape_l:
			try:
				cnt[item] = cnt[item].encode('utf-8')
			except:
				cnt[item] = None
		ofile  = open("Product_Catalogue_9.csv", "a+b")
		c = csv.writer(ofile)
		c.writerow([str(serial),name,rating,price,cnt['OS'],cnt['Colour'] ,cnt['RAM'],cnt['Product Dimensions'], cnt['Connectivity technologies'], cnt['Special features'],date])
		ofile.close()	
		print "yes"
	except:
		ofile  = open("Product_Catalogue_9.csv", "a+b")
		c = csv.writer(ofile)
		a = None
		c.writerow([str(serial),a,a,a,a,a ,a,a, a, a,date])
		ofile.close()
		print "no"
	'''	try:
			cnt[cells[0].text.strip()] += 1
		except:
			cnt[cells[0].text.strip()] = 1
	if serial == 15:
		print cnt
		break
	'''
