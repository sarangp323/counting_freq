from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):

    @abstractmethod
    def person_method():
        pass

class Student(Person):

    def __init__(self):
        self.name="Basic Student Name"

    def person_method(self):
        print("I am a Student")

class Teacher(Person):

    def __init__(self):
        self.name="Basic Teacher Name"

    def person_method(self):
        print("I am a Teacher")

class Personfactory():
    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()

        if person_type == 'Teacher':
            return Teacher()

        else:
            print("Invalid Type")


if __name__=='__main__':
    choice=input("what type of person u want to create?\n")
    person=Personfactory.build_person(choice)
    person.person_method()
    
        

    
