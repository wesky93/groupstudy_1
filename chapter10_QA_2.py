#10_2
import sys

#변수 선언
dic_time = dict()					#시간 계수용 변수

#프로그램 시작
#입력 파일 검토
fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()

#시간 추출 및 계수
for line in o_file:
	check_line = line.split()
	if len(check_line) > 1 and check_line[0] == "From":	
		row_time = check_line[-2].split(":")			#시간 분리
		hour = row_time[0]												#시간 추출
		dic_time[hour] = dic_time.get(hour, 0)+1	#시간 계수


#시간 정렬
li_time = list(dic_time.items())				#시간 정렬용 튜플리스트
li_time.sort(reverse=False)

for time, count in li_time:
	print(time," ",count)

