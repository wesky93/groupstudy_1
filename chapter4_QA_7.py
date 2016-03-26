#4_7
import sys


def computegrade(score):
	if score >= 0.9:
		print("A")
	elif score >= 0.8:
		print("B")
	elif score >= 0.7:
		print("C")
	elif score >= 0.6:
		print("D")
	else:
		print("F")
#점수값 검증 과정
try:
	score = float(input("Enter score : "))
	if 0 > score or 1 < score:
		sys.exit()
except:
	print("Bad score")
	sys.exit()
	
#점수 판별 과정

computegrade(score)


	
