class SchoolMember:
    """학교 멤버를 소개합니다."""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("학교 멤버를 설정했습니다 : {}".format(self.name))

    def tell(self):
        """내 상세정보를 말하시오"""
        print("이름 : {}, 나이 : {}".format(self.name, self.age))

class Teacher(SchoolMember):
    '''선생님을 소개'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("선생님 설정 : {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("월급 : {:d}".format(self.salary))

class Student(SchoolMember):
    '''학생을 소개'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("학생 설정 : {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("점수 : {:d}".format(self.marks))

# 프로그램 시작
t = Teacher("문재인",40,30000)
s = Student("신재현",22, 80)

print()

members = [t,s]
for member in members:
    member.tell()

