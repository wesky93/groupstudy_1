
#변수 선언
number = None #입력 숫자
count_number = 0 #총 갯수 초기화
sum_number = 0 #총 계 초기화
ev_number = 0 #총 평균 초기화


while True:
	number = input("Enter a number: ")		
	if number == "done" :									
		break
	else:																	
		try:
			number = int(number)
			count_number = count_number+1
			sum_number = sum_number+number
		except:
			print ("Invalid input")
		

ev_number = sum_number/count_number
print (sum_number," ",count_number," ",ev_number)
