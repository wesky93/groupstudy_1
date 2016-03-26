#7_3

#변수 선언
count = 0
egg = "na na boo boo"

#파일입력 처리
try:
	title = input("Enterile name: ")
	if title == egg:
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
	else:
		o_file = open(title)
		for line in o_file:
			count = count+1
		print ("There were ",count," subject lines in ",title)
except:
	print ("file can't found")

