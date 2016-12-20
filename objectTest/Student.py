class Student(object):
    def __init__(self,name,score):
        self._name = name
        self._score= score

    def print_score(self):
        print('%s , %s' %(self._name,self._score))



class Animal():
    def run(self):
        print("Animal is running ")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

from enum import Enum

Month = Enum('Month',('first','second','three','thour'))
for name , member in Month.__members__.items():
    print(name, '-->',member,',',member.value)

if __name__ == '__main__':
    bart = Student("jiang",100)
    bart.print_score()

    Dog().run()
    Cat().run()

    print(isinstance(Dog(),Animal))

    print("getAttr _name value = ",getattr(bart,"_name"))
    print("hasAttr _name value = ",hasattr(bart,"_name"))

