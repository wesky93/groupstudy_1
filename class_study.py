# 클래스 스터디

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hellow, how are you today?",self.name)


p = Person("sky")
p.say_hi()

