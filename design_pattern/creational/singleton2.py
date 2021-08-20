class Singleton():
    def __init__(self,klass):
        self.klass=klass
        self.instance=None

    def __call__(self,*args,**kwargs):
        if self.instance==None:
            self.instance=self.klass(*args,**kwargs)
        return self.instance


@Singleton
class Logger():
    def __init__(self):
        self.start=None

    def write(self,message):
        if self.start:
            print(self.start,message)
        else:
            print(message)

logger1=Logger()
logger1.start='#'
print('logger 1', logger1)
logger1.write("logger1 is created")


logger2 = Logger()
logger2.start='$'
print('logger 2', logger2)
logger2.write("Logger 2 is created")

logger1.write("Logger 2")
            
