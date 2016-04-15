import csv

ofile  = open("Product_Catalogue_tv_new.csv", "a+b")
c = csv.writer(ofile)
c.writerow(["SerialN","Name","Ratings","Price","Condition","Date"])
ofile.close()

with open('Product_Catalogue_tv.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		for i in xrange(0,len(row)):
			if row[i] == '':
				row[i] = 'Not Available'
		ofile  = open("Product_Catalogue_tv_new.csv", "a+b")
		c = csv.writer(ofile)
		c.writerow(row)
		ofile.close()