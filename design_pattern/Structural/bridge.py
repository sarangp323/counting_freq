from abc import ABCMeta, abstractmethod

class Material(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class Cobblestone(Material):
    def __init__(self):
        pass

    def __str__(self):
        return "CobbleStone"

class Wood(Material):
    def __init__(self):
        pass

    def __str__(self):
        return "Wooden"

class Brick(Material):
    def __init__(self):
        pass

    def __str__(self):
        return "Bricks"

class Building(metaclass=ABCMeta):
    @abstractmethod
    def print_name(self):
        pass

class Tower(Building):
    def __init__(self,name,material):
        self.name=name
        self.material=material

    def print_name(self):
        print(self.name + " is made up of " + str(self.material))

class Mill(Building):
    def __init__(self,name,material):
        self.name=name
        self.material=material

    def print_name(self):
        print(self.name + " is made up of " + str(self.material))

class Wall(Building):
    def __init__(self,name,material):
        self.name=name
        self.material=material

    def print_name(self):
        print(self.name + " is made up of " + str(self.material))

cobb = Cobblestone()
local_mill = Mill("Hilltop mill",cobb)
local_mill.print_name()

wooden = Wood()
wood = Tower("Watch Tower",wooden)
wood.print_name()

wall = Brick()
wll = Wall("Hall Wall",wall)
wll.print_name()


        
        

