#9_1
o_file = open("words.txt")
letter_dic = dict()

for i in o_file:
	check = i.split()
	if len(check) == 0: continue
	#디버깅용 코드 print (check)
	for letter in check:
		if letter in letter_dic: continue
		letter_dic[letter] = 1
		#디버깅용 코드 print(letter_dic)
		
print(letter_dic)
		
	