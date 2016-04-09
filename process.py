fi = open('outlinks.txt','r')
temp = []
for i in fi.readlines():
	
	temp.append(i.strip())
temp = set(temp)
#print len(temp)
for i in temp:
	print i 