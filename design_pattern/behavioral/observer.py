from abc import ABCMeta, abstractmethod
import random


class Subject(metaclass = ABCMeta):
    @abstractmethod
    def attach(self,Observer):
        pass

    @abstractmethod
    def detach(self,Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

def Operation(Subject):
    def __init__(self):
        self._observer =[]

    def attach(self,observer):
        self._observer.append(observer)

    def detach(self,observer):
        self._observer.remove(observer)

    def notify(self,*args):
        for observer in self._observer:
            observer.update(self)

    def perform_operation(self):
        total=1
        for i in range(random.randint(10)):
            total+=i
        print(f"result of operation is {total}")
        self.notify


class Observer(metaclass = ABCMeta):

    def update(self,Subject):
        pass

class ObserverA(Observer):
    def update(self,Subject):
        print("ObserverA :react on event")

class ObserverB(Observer,Subject):
    def update(self):
        print("ObserverB :react on event")
        
if __name__ == '__main__':

    subject = Operation()

    A = ObserverA()
    B = ObserverB()

    subject.attach(A)
    subject.attach(B)

    subject.perform_opeartion()
    subject.perform_operation()

    subject.detach(A)
    subject.perform_operation()
    
        
    
        
        
            
        

