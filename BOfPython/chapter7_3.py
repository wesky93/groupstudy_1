#문제 풀이
별 = "*"
공백 = " "

def 첫번째문제():
    print("첫번째 문제 풀이")
    for i in range(5):
        print(별,end="")
    print(" ")

def 두번째문제():
    print("두번째 문제 풀이")
    for i in range(4):
        for i in range(5):
            print(별,end="")
        print(" ")


def 세번째문제():
    print("세번째 문제 풀이")
    for i in range(5):
        별수 = i+1
        for i in range(별수):
            print(별,end="")
        print(공백)

def 네번째문제():
    print("네번째 문제 풀이")
    for i in range(5):
        별수 = i-5
        공백수 = i+1
        while 별수 < 0:
            print(별,end="")
            별수 += 1
        for i in range(공백수):
            print(공백,end="")
        print(공백)

def 다섯번째문제():
    print("다섯번째 문제 풀이")
    for i in range(5):
        공백수 = i-4
        별수 = i+1
        while 공백수 < 0:
            print(공백,end="")
            공백수 += 1
        for i in range(별수):
            print(별,end="")
        print(공백)

def 여섯번째문제():
    print("여섯번째 문제 풀이")
    for i in range(5):
        별수 = i-5
        공백수 = i
        for i in range(공백수):
            print(공백, end="")
        while 별수 < 0:
            print(별,end="")
            별수 += 1
        print(" ")

def 일곱번째문제():
    print("일곱뻔째 문제 풀이")
    for i in range(5):
        별수 = 1+i*2
        공백수 = int((9-별수)/2)
        print(공백*공백수,별*별수,공백*공백수)

def 여덜번째문제():
    print("여덜번째 문제 풀이")
    for i in range(5):
        별수 = 9-(i*2)
        공백수 =  i
        print(공백*공백수,별*별수,공백*공백수)

def 아홉번째문제():
    print("아홉번째 문제 풀이")
    apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
    arrears = [101, 203, 301, 404]
    for i in range(4):
        아파트_동 = apart[i]
        for i in range(4):
            아파트_호 = 아파트_동[i]
            미납확인 = False
            for 미납세대 in arrears:
                if 아파트_호 == 미납세대:
                    미납확인 = True
            if 미납확인 == True:
                print("띵동!",아파트_호,"호님 구독료 납부하세요")
                continue
            print(아파트_호,"호 배달완료")
        print(i+1,"동 배달완료")
    print("신문 배달 완료")
#문제 실행

첫번째문제()
print(" ")
두번째문제()
print(" ")
세번째문제()
print(" ")
네번째문제()
print(" ")
다섯번째문제()
print(" ")
여섯번째문제()
print(" ")
일곱번째문제()
print(" ")
여덜번째문제()
print(" ")
아홉번째문제()
print("문제 다 풀었다")