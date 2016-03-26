#8_4

fhand = open("romeo.txt")
li_dic = []								#단어 수집용 리스트 생성

for line in fhand:									#한줄씩 차례로 실행
	words = line.split()							#한 줄을 단어별로 리스트화
	if len(words) == 0: continue			#빈줄은 패스
	for letter in words:
		if li_dic.count(letter) == 0:		#리스트에 단어가 있는지 판독
			li_dic.append(letter)					#리스트에 단어 추가

print (li_dic)
		
		
