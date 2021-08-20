import copy

class Prototype():

    def __init__(self):
        self.obj_dict={}

    def register_class(self,name,obj):
        self.obj_dict[name]=obj

    def unregister_class(self,name,obj):
        del obj_dict[name]

    def clone(self,name,**attr):
        obj_a = copy.deepcopy(self.obj_dict.get(name))
        obj_a.__dict__.update(attr)

        return obj_a


class Car():

    def __init__(self):
        self.name="BMW"
        self.color="red"
        self.option="tuned"

    def __str__(self):
        return "The obj.attributes {} | {} | {}".format(self.name,self.color,self.option)

car = Car()
p1=Prototype()
p1.register_class('BMW',car)
car_cloned = p1.clone('BMW',color='red', option='tuned')
print(car_cloned)

    
    
