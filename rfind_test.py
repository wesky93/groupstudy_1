str1 = "this is iphone5 that is iphone6s, but wher is my iphone"
str2 = "is"

def countfindword(find,where):
  data = {}         #찾은 위치를 저장하는 딕셔너리
  count = 0         #찾은 횟수 카운트
  num = len(where)  # 처음 rfind 실행시 범위 지정
  while 1 == True:
    num = where.rfind(find,0,num)
    if num == -1:
      break
    else:
      count += 1
      data[count] = num
  print("%s가 총 %d개 발견되었습니다" % (str2,count))
  print(data)


countfindword(str2,str1)
