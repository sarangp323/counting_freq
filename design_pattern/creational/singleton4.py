from abc import ABCMeta, abstractstaticmethod

class Iperson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        pass

class Personsingleton(Iperson):

    __instance=None

    @staticmethod
    def get_instance():
        if Personsingleton.__instance == None:
            PersonSingleton("Default Name",0)
        return PersonSingleton.__instance

    def __init__(self,name,age):

        if Personsingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name=name
            self.age=age
            Personsingleton.__instance=self

    
    @staticmethod
    def print_data():
        print(f"Name: {Personsingleton.__instance.name},  Age: {Personsingleton.__instance.age}")



p=Personsingleton("Mike",20)
print(p)
p.print_data()
            
