
title = input("Enterile name: ")

try:
	o_file = open(title)
except:
	print ("file can't found")
	exit()

for line in o_file:
	upline = line.upper()
	print (upline)