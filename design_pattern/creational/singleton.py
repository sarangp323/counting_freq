class Singleton(object):
    def __new__(cls, *arg, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls,*arg,**kwargs)
        return cls._instance

o1 = Singleton()
print("Object - 1 ==>",o1)
o1.data=10

o2=Singleton()
print("Object - 2 ==>",o2)
print("Object-2 data ==>",o2.data)
o2.data=5

print("Object-1 ==>",o1.data)

