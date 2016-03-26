#8_3

fhand = open("mbox-short.txt")

for line in fhand:
	words = line.split()
	if len(words) > 1 and words[0] == "From":
		print (words[2])
		