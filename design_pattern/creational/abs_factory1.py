from abc import ABCMeta , abstractmethod

class Carfactory(metaclass=ABCMeta):

    @abstractmethod
    def build_parts(self):
        pass

    @abstractmethod
    def build_car(self):
        pass

class Sedan_factory(Carfactory):

    def build_parts(self):
        return Sedancarpartsfactory()

    def build_car(self):
        return Sedancarassemblefactory()

class Suv_factory(Carfactory):

    def build_parts(self):
        return Suvcarpartsfactory()

    def build_car(self):
        return Suvcarassemblefactory()

class Carpartfactory(metaclass=ABCMeta):
    def build(self):
        pass

class Sedancarpartsfactory(Carpartfactory):
    def build(self):
        print("Sedan car parts are built")

    def __str__(self):
        return "Sedan car parts are built"

class Suvcarpartsfactory(Carpartfactory):
    def build(self):
        print("Suv car parts are built")

    def __str__(self):
        return "Suv car parts are built"

class Carassemblefactory(metaclass=ABCMeta):
    def assemble(self):
        pass

class Sedancarassemblefactory(Carpartfactory):
    def assemble(self,parts):
        print(f"Sedan car is assemble here using {parts}")

    

class Suvcarassemblefactory(Carpartfactory):
    def assemble(self,parts):
        print(f"Suv car is assemble here using {parts}")


if __name__ == '__main__':
    for factory in (Suv_factory(),Sedan_factory()):
        car_parts=factory.build_parts()
        car_build=factory.build_car()
        car_build.assemble(car_parts)
    
