import random
class Enemy:

    def __init__(self,name="Enemy",hit_points=0,lives=1): #initialization
        self.name=name
        self.hit_points=hit_points
        self.lives=lives
        self.alive=True


    def take_damage(self,damage): #function to calculate damage
        remaining_points=self.hit_points-damage
        if remaining_points>=0:
            self.hit_points=remaining_points
            print("I took {} points damage and have {} left".format(damage,remaining_points))
        else:
            self.lives-=1
            if self.lives>0: #checking lives>0
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive=False
                
            

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, hitpoints: {0.hit_points}".format(self)

class Troll(Enemy):#inheriting Enemy class

    def __init__(self, name): 
        super().__init__(name =name, lives=1,hit_points=23)

    def grant(self): #add functionalty diff. than base class
        print("Me {0.name}. {0.name} stamp you".format(self))

class Vampyre(Enemy): #inheriting Enemy class
    def __init__(self,name):
        super().__init__(name=name,lives=3,hit_points=12)

    def dodges(self): # adding its new fuction
        
        if random.randint(1,3)==3: # if random no. is 3 it will not take damage
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self,damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class Vampyreking(Vampyre):

    def __init__(self,name):
        super().__init__(name)
        self.hit_points=140

    def take_damage(self,damage):
        super().take_damage(damage//4)
    
