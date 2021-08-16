#from player import Player
#tim = Player("Tim")

from enemy import Enemy , Troll, Vampyre, Vampyreking


dracula = Vampyreking("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

#random_monster = Enemy("Basic Enemy",12,1)
#print(random_monster)


#random_monster.take_damage(4)
#print(random_monster)

#random_monster.take_damage(8)
#print(random_monster)

#random_monster.take_damage(9)
#print(random_monster)

print("*********************************** \n \n")


ugly_troll = Troll("pug")
print("ugly troll-{}".format(ugly_troll))

another_troll = Troll("UG")
print("Another troll-{}".format(another_troll))
another_troll.take_damage(10)

#brother = Troll("Urg")
#print(brother)

ugly_troll.grant()

vamp = Vampyre("vald")
print(vamp)
vamp.take_damage(5)

#while vamp.alive:
    
#    vamp.take_damage(1)
 #   print(vamp)



