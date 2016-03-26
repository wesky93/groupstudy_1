#9_2
import sys

date_dict = dict()		#요일 계수용 딕셔너리 변서 선언

fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()
	
for line in o_file:
	check_line = line.split()
	if len(check_line) == 0: continue		#공백줄 스킵
	if check_line[0] == "From":
		date = check_line[2]
		date_dict[date] = date_dict.get(date,0)+1
		
print(date_dict)