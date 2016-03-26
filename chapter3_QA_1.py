#3_1
hours = int(input("Enter Hours : "))
rate = float(input("Enter Rate : "))
if hours >= 40:
	rate = rate*1.5

pay = str(hours * rate)
print ("Pay : "+pay)