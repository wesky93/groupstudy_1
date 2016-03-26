
#변수 선언
number = None #입력 숫자
count_number = 0 #총 갯수 초기화
sum_number = 0 #총 계 초기화
ev_number = 0 #총 평균 초기화
min_num = 0
max_num = 0

while True:
	number = input("Enter a number: ")
	if number == "done" :
		break
	else:
		try:
			number = int(number)
			count_number = count_number+1
			sum_number = sum_number+number
			#최대 최소값 확인
			if min_num == 0 or number < min_num:
				min_num = number 
			if max_num == 0 or number > max_num:
				max_num = number
		except:
			print ("Invalid input")
		

print (sum_number," ",count_number," ",min_num,"  ",max_num)
