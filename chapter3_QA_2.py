#3_2
import sys
try:
	hours = int(input("Enter Hours : "))
except:
	print ("Error, please enter numeric input")
	sys.exit()

try:
	rate = float(input("Enter Rate : "))
except:
	print ("Error, please enter numeric input")
	sys.exit()

	
if hours >= 40:
	rate = rate*1.5

pay = str(hours * rate)
print ("Pay : "+pay)