#8_6
import sys

#입력값 처리 함수
def checkinput(n_list):
	check = input("Enter a number: ")
	if check == "done":
		n_list.sort()
		n_max = n_list[-1]
		n_min = n_list[0]
		print ("max number : ",n_max," ","mini number : ",n_min)
		sys.exit()
	try:
		number = int(check)
		return number
	except:
		print("typing right number!")
		
#값 수집 리스트		
num_list = []

#입력값 확인 및 리스트추가		
while True:
	num = checkinput(num_list)
	if num == None: continue
	num_list.append(num)
	#디버깅용 print(num_list)





		
