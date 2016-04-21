

class Robot:
    """Represents a robot, with a name"""
    # A class variabel, counting the number of robots
    population = 0

    def __init__(self,name):
        """데이터 초기화"""
        self.name = name
        print("(Initializing {})".format(self.name))

        #만약 사람이 추가되면 로봇은 인구를 추가
        Robot.population += 1

    def die(self):
        """사람이 죽었다"""
        print("{}가 사라졌습니다!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{}는 마지막 이었습니다.".format(self.name))
        else:
            print("아직 {:d}명이 일하고 있습니다".format(Robot.population))

    def say_hi(self):
        """주인에게 인사"""
        print("안녕하세요 주인님 저를 {}라 불러주세요".format(self.name))

    @classmethod
    def how_many(cls):
        """인구수를 보여주기"""
        print("총 {:d}명이 있습니다.".format(cls.population))

드루이드1 = Robot("R2-D2")
드루이드1.say_hi()
Robot.how_many()

드루이드2 = Robot("C-3PO")
드루이드2.say_hi()
Robot.how_many()

print("\n 여기서 개노가다 하고 있습니다. \n")
print("모든작업을 마쳤고 이제 사라집니다")
드루이드1.die()
드루이드2.die()

Robot.how_many()