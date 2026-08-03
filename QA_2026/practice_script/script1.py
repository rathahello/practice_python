# class Student:
#     @staticmethod
#     def exam():
#         print("exam")
#     def attendance(self):
#         print("attendance")
#
# stud = Student()
# stud.exam()
# stud.attendance()


# class personDetail:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def personInfo(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# people = personDetail("Ratha",18)
# people.personInfo()


class Family:
    def child(self):
        print("child")

class Children(Family):
    def name(self):
        print("Name")

def sumNumber(a, b):
    result = a + b
    print(result)
def minus(a, b):
    result = a - b
    print(result)
def multiply(a, b):
    result = a * b
    print(result)
def divide(a, b):
    result = a / b
    return result


fam = Children()
fam.name()
fam.child()