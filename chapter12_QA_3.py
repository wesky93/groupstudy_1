import urllib.request
import sys

#변수 모음
url = input("Enter the url : ")					#입력할 url "http://www.py4inf.com/code/mbox.txt"
count = 0																#문자열 갯수

#올바른 주소인지 확인
try:
	fhsnd = urllib.request.urlopen(url)
except:
	print("Wrong url")
	fhsnd.close()
	sys.exit()
		
#데이터 처리 시작
while True:
	data = str(fhsnd.read(500).decode("utf-8"))
	if len(data) == 0:				# 더이상 받을 자료 없는 상황 처리
		print("No more data")
		break
	elif count == 3000 :			# 요구 충족시 루프 탈출
		break
	
	#문자 계수
	for word in data:
		if count == 3000 :			# 요구 충족시 루프 탈출
			break
		if len(word) == 0:			#공백은 계수에서 제외 처리
			continue
		count += 1
		print(word)

print(count)
fhsnd.close()

	
	