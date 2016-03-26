#10_1
import sys

#변수 선언
dic_who = dict()					#보낸이 저장 및 계수

#프로그램 시작
#입력 파일 검토
fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()

#보낸이 저장 및 계수
for line in o_file:
	check_line = line.split()
	if len(check_line) > 1 and check_line[0] == "From":		#대상 선별
		who = check_line[1]
		dic_who[who] = dic_who.get(who, 0)+1


#보낸이 정렬용 튜플리스트 생성
li_who = list()				#보낸이 정렬용 튜플리스트
for who, count in dic_who.items():
	li_who.append((count,who))
	
li_who.sort(reverse=True)
max_who = li_who[0]
print(max_who[1]," ",max_who[0])

