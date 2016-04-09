import scrapy
import urlparse
from scrapy.spider import Request 
from bs4 import BeautifulSoup
from scrapy.spider import BaseSpider
check = True
class pagespider(BaseSpider):
	name = "pgspider"
	allowed_domains= ["amazon.in"]
	start_urls = ["http://www.amazon.in/TVs/b/ref=sd_allcat_nav_shopall_television?ie=UTF8&node=1389396031"]


	def parse(self , response):
		
		soup = BeautifulSoup(response.body).find_all("ul",{"class":"fg-cell-list fg-mobile-right"})[0]
		print "===================================IN==========================================="
		for item in soup:
			x = item.contents[0].get("href")
			print x
			url = urlparse.urljoin(response.url, x)
			yield scrapy.http.Request(url,callback=self.parse_page)
			break
		print "===================================OUT==========================================="


	def parse_page(self,response):
		print "--------------- >>>>>>>>>>  IIIIINNNNNN  ------------------------"
		soup = BeautifulSoup(response.body).find_all("div",{"id":"mainResults"})[0]
		soup = soup.find_all("a",{"class":"a-link-normal s-access-detail-page  a-text-normal"})
		for item in soup:
			url = item.get("href")
			url = urlparse.urljoin(response.url, url)
			yield scrapy.http.Request(url,callback=self.scrape_data)

		#soup = BeautifulSoup(response.body).find_all("div",{"id":"pagn"})[0].find_all("span",{"class","pagnLink"})	
		#if check:
		#	global check 
		#	check = False
		#	for item in soup:
		#		url = item.contents[0].get("href")
		#		url = urlparse.urljoin(response.url, url)
		#		yield scrapy.http.Request(url,callback=self.parse_page)			
		
			
		
			
	def scrape_data(self,response):
		
		temp = BeautifulSoup(response.body).find_all("div",{"class":"pdTab"})[0]
		
		temp = temp.find_all("td")
		print "=====================================================>>>>>>>>>>>>>>>>>>>>>>>>>"
		print temp[2].text
		print temp[3].text
		print "=====================================================>>>>>>>>>>>>>>>>>>>>>>>>>"

		


			
			


