from abc import ABCMeta, abstractmethod
import random

class Cook(metaclass=ABCMeta):
    @abstractmethod
    def dish_type(self):
        pass

class Dessert(Cook):
    
    def dish_type(self):
        dish=["icecream","chocolate pie", "cake","Brownie"]
        k=random.choice(dish)
        print("Started making your {}".format(k))

class Breakfast(Cook):
    
    def dish_type(self):
        dish=["Poha","Dosa","Idli","Sabudana Khichadi"]
        k=random.choice(dish)
        print("Started making your {}".format(k))

class Lunch(Cook):
    
    def dish_type(self):
        dish=["Sandwich","Superfood Salad","Fried Rice"]
        k=random.choice(dish)
        print("Started making your {}".format(k))


class Dinner(Cook):
   
    def dish_type(self):
        dish=["Kaju Curry","Egg Curry","Paneer Tikka","kofta"]
        k=random.choice(dish)
        print("Started making your {}".format(k))


class Cookfactory():

    @staticmethod
    def cook_dish(person_choice):
        if person_choice=="Dessert":
            return Dessert()
        if person_choice=="Breakfast":
            return Breakfast()
        if person_choice=="Lunch":
            return Lunch()
        if person_choice=="Dinner":
            return Dinner()

if __name__ =='__main__':
    choice=input("Sir, What you would u like to have:- \n1) Dessert\n2) Breakfast \n3)Lunch \n4)Dinner\n")
    
    dis=Cookfactory.cook_dish(choice)
    dis.dish_type()


        





    
