import scrapy
import urlparse
from scrapy.spider import Request 
from bs4 import BeautifulSoup
from scrapy.spider import BaseSpider
class pagespider(BaseSpider):
	name = "amazon"
	allowed_domains= ["amazon.in"]
	start_urls = ["http://www.amazon.in/TVs/b/ref=sd_allcat_nav_shopall_television?ie=UTF8&node=1389396031"]


	def parse(self , response):
		
		soup = BeautifulSoup(response.body).find_all("ul",{"class":"fg-cell-list fg-mobile-right"})[0]
		print "===================================IN==========================================="
		for item in soup:
			x = item.contents[0].get("href")
			url = urlparse.urljoin(response.url, x)
			yield scrapy.http.Request(url,callback=self.parse_page)
			break
		print "===================================OUT==========================================="


	def parse_page(self,response):
		print "heyyyyyyyyyyyyyyyyyyy"
		soup = BeautifulSoup(response.body).find_all("div",{"id":"mainResults"})[0]
		soup = soup.find_all("li")
		print soup
		#for item in soup:
		#	inter = item.find_all("a")
		#	for innerItem in inter:
		#		url = innerItem.get("href")
		#		print url
			#	yield scrapy.http.Request(url,callback=self.scrape_data)
			









	def scrape_data(self,response):
		details={}
		
		temp = BeautifulSoup(response.body).find_all("title")[0].text.split()
		details['title'] = temp[0]+" "+temp[1]
		print "=====================================================>>>>>>>>>>>>>>>>>>>>>>>>>"
		print details['title']
		print "=====================================================>>>>>>>>>>>>>>>>>>>>>>>>>"
		


			
			


