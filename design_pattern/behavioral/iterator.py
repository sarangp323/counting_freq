from abc import ABCMeta , abstractmethod

class Iiterator(metaclass = ABCMeta):

    @abstractmethod
    def has_next(self):#return bool whether end of collection or not
        pass

    @abstractmethod
    def next(self):#return collection of obj.
        pass

class Iterable(Iiterator):

    def __init__(self,aggregates):
        self.index=0
        self.aggregates = aggregates

    def next(self):
        if self.index<len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index +=1
            return aggregate
        raise Exception("AtEndOfIteratorException","At End of Iterator")

    def has_next(self):
        return self.index<len(self.aggregates)

class Iaggregate(metaclass = ABCMeta):

    @abstractmethod
    def method(self):
        pass

class A(Iaggregate):
    def method(self):
        print("This method A() in invoked")

class B(Iaggregate):
    def method(self):
        print("This method B() in invoked")

class C(Iaggregate):
    def method(self):
        print("This method c() in invoked")

AGGREGATES = [A(), B(), C(), A()]
ITERABLE = Iterable(AGGREGATES)
while ITERABLE.has_next():
    ITERABLE.next().method()
    

