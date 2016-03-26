import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.py4inf.com",80))
txt = "GET http://www.py4inf.com/code/remeo.txt HTTP/1.0\n\n"
txt = txt.encode()
mysock.send(txt)

while True:
	data = mysock.recv(512)
	if (len(data)<1):
		break
		
	print (data)

mysock.close()