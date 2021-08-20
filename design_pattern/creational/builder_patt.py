class Robot():

    def __init__(self):
        self.bipedal=False
        self.Quadripedal=False
        self.wheeled=False
        self.flying=False
        self.traversal=[]
        self.detection_system=[]

    def __str__(self):
        string=""
        if self.bipedal:
            string+="BIPEDAL"

        if self.Quadripedal:
            string+="QUADRIPEDAL"

        if self.flying:
            string+="FLYING ROBOT"
            
        if self.wheeled:
            string+="ROBOT ON WHEELS"

        else:
            string +="ROBOT\n"

        if self.traversal:
            string+="Traversal Module Installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_system:
            string += "Detection system Installed:\n"

        for system in self.detection_system:
            string += "- " + str(system) + "\n"

        return string


class Bipedallegs():
    def __str__(self):
        return "two legs"

class Quadripedal():
    def __str__(self):
        return "Four legs"

class Arms():
    def __str__(self):
        return "Two arms"

class Wings():
    def __str__(self):
        return "Wings"

class Blades():
    def __str__(self):
        return "blades"

class Fourwheels():
    def __str__(self):
        return "four wheels"

class Twowheels():
    def __str__(self):
        return "Two Wheels"

class Cameradetection:
    def __str__(self):
        return "cameras"

class Infrareddetection():
    def __str__(self):
        return "Infrared"


from abc import ABCMeta, abstractmethod

class Robotbuilder(metaclass=ABCMeta):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass

class Androidbuilder(Robotbuilder):

    def __init__(self):
        self.product=Robot()

    def reset(self):
        self.product=Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal=True
        self.product.traversal.append(Bipedallegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):

        self.product.detection_system.append(Cameradetection())


builder = Androidbuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())


    







    





            
            
