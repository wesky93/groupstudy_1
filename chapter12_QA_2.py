import socket

#변수 모음
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input("Enter the url : ")
host = url.split("//")[1].split("/")[0]	#URL 주소 필터링														
count = 0																#문자열 갯수

print(url)
#소켓 접속
mysock.connect((host, 80))
send_url = b"GET +url+ HTTP/1.0\n\n"
mysock.send(send_url)

#데이터 수신 및 자료 처리 시작
while True:
	data = mysock.recv(500)
	if len(data) == 0:				# 더이상 받을 자료 없는 상황 처리
		print("No more data")
		break
	elif count == 3000 :			# 요구 충족시 루프 탈출
		break
	
	#문자 계수
	words = str(data)
	for word in words:
		if count == 3000 :			# 요구 충족시 루프 탈출
			break
		if len(word) == 0:			#공백은 계수에서 제외 처리
			continue
		count += 1
		print(word)

print(count)
mysock.close()
	
	