from abc import ABCMeta, abstractmethod

class Ihandler(metaclass = ABCMeta):
    @abstractmethod
    def next_successor(self,successor):
        pass
    @abstractmethod
    def handle(self,animal):
        pass

class Dog(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor=successor

    def handle(self,animal):

        if animal == "dog":
            print("I am a dog, bowh! bowh!")

        else:
            #print("there is no dog")
            self._successor.handle(animal)

class Cat(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor=successor

    def handle(self,animal):

        if animal == "cat":
            print("I am a cat, meow! meow!")

        else:
            #print("There is no cat")
            self._successor.handle(animal)


class Monkey(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor=successor

    def handle(self,animal):

        if animal == "monkey":
            print("I am a monkey and I love Banana")

        else:
            #print("there is no  monkey")
            self._successor.handle(animal)

class Animal_show():

    def __init__(self):

        self.chain1= Dog()
        self.chain2=Cat()
        self.chain3=Monkey()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)

k=["dog","cat","monkey"]

Animal = Animal_show()

for i in k:
    Animal.chain1.handle(i)
    

        


            
            
                  

