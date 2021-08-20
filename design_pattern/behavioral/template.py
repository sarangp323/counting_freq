from abc import ABCMeta, abstractmethod
class Template(metaclass= ABCMeta):


    def template_method(self):

        self.animal()
        self.type_animal()
        #self.walk()
        self.voice()
        self.eat()

    def animal(self):
        print("Template class says: It is a animal")

    def type_animal(self):
        print("Template class says : Its a pet animal")
        
    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def eat():
        pass

class Dog(Template):

    def voice(self):
        print("Dog says: Bowh! Bowh!")

    def eat(self):
        print("Dog says : I love meat")

class Cat(Template):

    def voice(self):
        print("Cat says: Meow! Meow!")

    def eat(self):
        print("Cat says : I love Milk")

def Client(Template):

    Template.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    Client(Dog())
    print("")

    print("Same client code can work with different subclasses:")
    Client(Cat())
    
    
              

