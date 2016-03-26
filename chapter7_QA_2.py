#7_2
#변수 선언
count = 0		#스팸 측정 갯수
spam_su = 0 #스팸 총합
spam_av = 0 #스팸 평균
find_start = "X-DSPAM-Confidence:"
slice_start = len(find_start)


#파일입력 처리
try:
	title = input("Enterile name: ")
	o_file = open(title)
except:
	print ("file can't found")
	exit()

for line in o_file:
	if line.startswith(find_start):
		count = count+1
		spam_su = spam_su+float(line[slice_start:])
		
spam_av = spam_su/count
print (spam_av)