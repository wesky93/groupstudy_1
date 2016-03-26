#9_4
import sys

#변수 선언
date_dict = dict()		#요일 계수용 딕셔너리 변서 선언
many_email = str()		#이메일 최대 보유자
max_email = 0			#최대 이메일 계수

#프로그램 시작
#입력 파일 검토
fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()

#이메일 주소 검토
for line in o_file:
	check_line = line.split()
	if len(check_line) == 0: continue		#공백줄 스킵
	if check_line[0] == "From":
		date = check_line[1]
		date_dict[date] = date_dict.get(date,0)+1
	if date_dict[date] > max_email:
		many_email = date
		max_email = date_dict[date]

print(many_email," ",max_email)