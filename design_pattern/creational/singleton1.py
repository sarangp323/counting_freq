class Borg(object):
    _shared={}

    def __init__(self):
        self.__dict__=self._shared

class Singleton(Borg):
    def __init__(self,arg):
        Borg.__init__(self)
        self.val=arg

o1=Singleton("Sarang")
print("Object-1 ==>",o1)
print("Object-1 data ==>",o1.val)
      

o2=Singleton("Aarav")
print("Object-2 ==>",o2)
print("Object-2 data ==>",o2.val)
print("Object-1 data ==>",o1.val)
