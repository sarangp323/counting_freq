class Momento():

    def __init__(self,score,inventory,level,location):
        self.score=score
        self.inventory=inventory
        self.level=level
        self.location=location

class Gamecharacter():

    def __init__(self):
        self._score=0
        self._inventory=set()
        self._level=0
        self._location={"x":0,"y":0,"z":0}

    @property
    def score(self):
        return self._score

    def register_kill(self):
        self._score+=100

    def add_inventory(self,item):
        self._inventory.add(item)

    def progress_level(self):
        self._level+=1

    def move_forward(self,position):
        self._location["z"]+=position

    def __str__(self):
        return (f"Score:{self._score}, "
                f"Level:{self._level}, "
                f"Location:{self._location}\n"
                f"Inventory:{self._inventory}\n")

    @property
    def momento(self):
        return Momento(self._score,self._inventory.copy(),self._level,self._location.copy())

    @momento.setter
    def momento(self,momento):
        self._score=momento.score
        self._inventory=momento.inventory
        self._level = momento.level
        self._location = momento.location

class Caretaker():

    def __init__(self,originator):
        self._originator=originator
        self._mementos=[]

    def save(self):

        print("Game Save")
        momento = self._originator.momento
        self._mementos.append(momento)

    def restore(self,index):
        print("Restoring Gaming Detail")
        momento = self._mementos[index]
        self._originator.momento = momento

GAME_CHARACTER = Gamecharacter()
CARETAKER = Caretaker(GAME_CHARACTER)

# start the game
GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.add_inventory("sword")
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("rifle")
GAME_CHARACTER.move_forward(1)
print(GAME_CHARACTER)

# save progress
CARETAKER.save()

GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_level()
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("motorbike")
GAME_CHARACTER.move_forward(10)
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# save progress
CARETAKER.save()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_level()
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# decide you made a mistake, go back to first save
CARETAKER.restore(0)
print(GAME_CHARACTER)

# continue
GAME_CHARACTER.register_kill()
        

