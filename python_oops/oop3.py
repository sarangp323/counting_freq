class Car:
    def __init__(self,model,year,price):
        self.__model=model
        self.year=year
        self.price=price
    number_of_wheels=4

    def setmodel(self,model):
        self.__model=model

    def getmodel(self):
        return self.__model

car1=Car("nissan",2020,200000)
print(car1.getmodel())

car1.setmodel("BMW")
print(car1.getmodel())
