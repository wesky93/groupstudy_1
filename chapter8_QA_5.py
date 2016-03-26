#8_5

fhand = input("Enter a file name: ")
open_fhand = open(fhand)
li_from = []

for line in open_fhand:									
	words = line.split()							
	if len(words) > 1 and words[0] == "From":
		li_from.append(words[1])
		print (words[1])

co_from = len(li_from)
print ("There were ",co_from," lines in the file with From as the first word")
		
		
