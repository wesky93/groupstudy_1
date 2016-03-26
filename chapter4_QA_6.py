#4.6
import sys

def computepay(hours,rate):
	if hours >= 40:
		rate = rate*1.5
		pay = str(40*10 + (hours-40)*rate)
	else:
		pay = str(hours * rate)
	
	print ("Pay : "+pay)

	
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

computepay(hours,rate)