from abc import ABCMeta,abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self,name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self,name):
        print(f"Enginner {name} is created")


class Personfactory():
    @classmethod
    def createperson(cls,designation,name):
        eval(designation)().create(name)

if __name__ == '__main__':
    designation=input("pls enter designation - ")
    name = input("ps enter name - ")
    Personfactory.createperson(designation, name)
        
