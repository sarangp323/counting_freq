from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass

class BE(AbstractDegree):
    def info(self):
        print("Bachelor of Engineeing")

    def __str__(self):
        return "Bachelor of Engineering"

class ME(AbstractDegree):
    def info(self):
        print("Master of Engineeing")

    def __str__(self):
        return "Master of Engineering"

class MBA(AbstractDegree):
    def info(self):
        print("Master of Business Administration")

    def __str__(self):
        return "Master of Business Administration"

class Profilefactory():
    def __init__(self):
        self._degrees=[]
        self.createprofile()

    @abstractmethod
    def createprofile(self):
        pass
    
    def adddegree(self,degree):
        self._degrees.append(degree)

    def getdegree(self):
        return self._degrees

class Manageefactory(Profilefactory):
    def createprofile(self):
        self.adddegree(BE())
        self.adddegree(MBA())

class Engineerfactory(Profilefactory):
    def createprofile(self):
        self.adddegree(BE())
        self.adddegree(ME())

if __name__=='__main__':
    profile_type=input("which profile u like to create? Manager/Engineer-")
    profile=eval(profile_type + 'factory')()
    print("creating profile of ", profile_type)
    print("profile has following degrees:-")
    for deg in profile.getdegree():
        print("-",deg)
