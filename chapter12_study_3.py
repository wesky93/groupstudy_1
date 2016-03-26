import urllib.request

count = dict()
fhsnd = urllib.request.urlopen("http://www.py4inf.com/code/romeo.txt")

for line in fhsnd:
	words = line.decode("utf-8").split()
	#words = txt.split()
	for word in words:
		count[word] = count.get(word,0)+1
print (count)

'''
for line in fhsnd:
	txt = line.decode('utf-8')
	print (txt.strip())
'''