from abc import ABCMeta, abstractmethod
import random

class State():

    def __init__(self):
        self.state_handles = [Addition(),
                              Substraction(),
                              Division()]
        self.handle=None

    def request(self):

        self.handle=self.state_handles[random.randint(0,2)].func(5,9)
        return self.handle

class Istate(metaclass = ABCMeta):

    @abstractmethod
    def func(self,x,y):
        pass

class Addition(Istate):

    def func(self,x,y):
        k=x+y
        return f"Addition of {x} and {y} is {k}"

class Substraction(Istate):

    def func(self,x,y):
        k=x-y
        return f"Addition of {x} and {y} is {k}"

class Division(Istate):

    def func(self,x,y):
        k=x/y
        return f"Addition of {x} and {y} is {k}"

    
CONTEXT = State()
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())

