#영문 문자 빈도만 계수합니다.
import sys

#입력 파일 검토
fname = input("Enter file name:")
try:
	o_file = open(fname)
except:
	print("wrong file name")
	sys.exit()

#알파벳 리스트 변수 선언
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dic_letter = dict()		#문자 정보 저장 딕셔너리
#문자 추출
for line in o_file:
	line = line.lower()
	t = tuple(line)		#문자 계수용 튜블생성
	if len(t) == 0:			#빈줄 건너뜀
		continue
	else:
		for letter in t:
			if letter in abc:		#영문자 판별
				dic_letter[letter] = dic_letter.get(letter, 0)+1 #영문자 계수 및 저장
			else:
				continue

#문자 빈도정렬
li_letter = list()	#문자 빈도 정렬용 리스트

for letter, count in dic_letter.items():
	li_letter.append((count,letter))
	
li_letter.sort(reverse=True)
for count, letter in li_letter:
	print(letter," ",count)

				