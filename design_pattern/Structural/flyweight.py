class SweetBirds(object): 
    #class for Birds
    def __init__(self): 
        pass
    def birds(self, bird_name): 
        return "Flyweightpattern[% s]" % (bird_name) 

class BirdKingdom(object): 
    bird_family = {}     #This stores ids of birds

    def __new__(coll,name, bird_family_ident): 
        try: 
            id = coll.bird_family[bird_family_ident] 

        except KeyError: 
            id = object.__new__(coll) 
            coll.bird_family[bird_family_ident] = id
        return id

    def put_bird_info(self, bird_info):
        #feed the  bird info

        bc = SweetBirds() 
        self.bird_info = bc.birds(bird_info) 

    def get_bird_info(self): 
        #return the bird info
        return (self.bird_info) 

if __name__ == '__main__': 

    bird_data = (('a', 1, 'Redbird'), ('b', 2, 'Yellowbird'), ('c', 2, 'Blurbird'), ('d',1,'Redbird')) 

    bird_family_objects = [] 

    for i in bird_data: 
        item = BirdKingdom(i[0], i[1]) 
        item.put_bird_info(i[2]) 

        bird_family_objects.append(item)  

    #If id same than they are same objects
    for j in bird_family_objects: 
        print(" id = " + str(id(j))) 
        print(j.get_bird_info())
