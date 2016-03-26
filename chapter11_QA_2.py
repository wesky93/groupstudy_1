import re
import sys

filename = input("Enter a filename : ")
sumall = 0	#총 합을 담는 변수
count = 0		#총 갯수를 담는 변수

try:
	with open(filename) as row_file:
		for line in row_file:
			line = line.rstrip()
			x = re.findall("^New.*: ([0-9]+)", line)
			if len(x) > 0 :
				count += 1
				sumall += int(x[0])

except:			#에러 처리
	print("typing file name")
	sys.exit()

av = sumall/count	#평균값
print(av)