#9_5
import sys

#변수 선언
by_who = dict()		#보낸 도메인 저장

#프로그램 시작
#입력 파일 검토
fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()

#도메인 추출
for line in o_file:
	check_line = line.split()
	if len(check_line) == 0: continue		#공백줄 스킵
	if check_line[0] == "by":
		domain = check_line[1]
		by_who[domain] = by_who.get(domain,0)+1

print(by_who)