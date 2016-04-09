import urllib2,csv,urllib,re

def download_file(download_url,name):
    response = urllib2.urlopen(download_url)
    file = open( name, 'w')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
	#new =  row[3].strip().replace(' ', '%20' )
	f = open("out_images_2.txt","r")
	for i in f.readlines():
		try:
			serial = i.split(" ")[0]
			down_url = i.split(" ")[1]
			if down_url == "##" : 
				pass
			else : 
				download_file(down_url, "product_" + serial + ".jpg")
		except:
			pass	
