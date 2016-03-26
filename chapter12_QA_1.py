import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input("Enter the url : ")
host = url.split("//")[1].split("/")[0]
try:
	print(url)
	mysock.connect((host, 80))
	send_url = b"GET +url+ HTTP/1.0\n\n"
	mysock.send(send_url)
	while True:
		data = mysock.recv(512).decode("utf-8")
		if ( len(data) < 1 ) :
			break
		print (data)
except Exception as e:
	print(e)
finally:
	mysock.close()