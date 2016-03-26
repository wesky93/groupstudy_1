import re
import sys

filename = "mbox.txt"

with open(filename) as row_file:
	try:
		retxt = input("Enter a regular expression : ")
		count = 0
		for line in row_file:
			line = line.rstrip()
			x = re.findall(retxt,line)
			if len(x) > 0 :
				count += 1
		print(filename," had ",count,"lines that matched ",retxt)
	except:
		print("typing correct regular expression")
		sys.exit()