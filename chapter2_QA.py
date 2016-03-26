# ex2.2
# Q : raw_input을 사용하여 사용자의 이름을입력받고 환영하는 프로그램을작성하세요.
# 파이썬3에서는 raw_input이 아닌 input입니다.
name = input("Enter yout name : ")
print ("hello "+ name)

# ex2.3
# Q = 급여를지불하기위해서사용자로부터근로시간과시간당임금을 계산하는 프로그램을작성하세요.
hours = input("Enter Hours : ")
rate = input("Enter Rate : ")
hours = int(hours)
rate = float(rate)
pay = hours * rate
print ("Pay : "+ str(pay))

# ex2.4
# Q = 다음 대입문장을 실행한다 가정시 width =17  height = 12.0
#			다음 표현식 각각에 대해서, 표현식의 값과 자료형을 작성하세요
width = 17
height = 12.0

print(type(width/2))
print(type(width/2.0))
print(type(height/3))
print(type(1+2*5))

# ex2.4
# Q = 사용자로부터섭씨온도를입력받아화씨온도로변환하고,변환된 온도를 출력하는 프로그램을작성하세요.
print("Temperature Unit Converter")
celsius = input("Please enter the Celsius temperature\n")
celsius = float(celsius)
fahrenheit = celsius*9/5+32
print("Celsius "+str(celsius)+" is fahrenheit "+ str(fahrenheit))