import urllib.request

img = urllib.request.urlopen("http://www.py4inf.com/cover.jpg")
fhand = open("cover.jpg", "w")
size = 0

while True:
	info = img.read(100000)
	if len(info) < 1: break
	size = size+len(info)
	fhand.write(info.decode("utf-8"))
		
print (size,"characters copied.")
fhand.close()