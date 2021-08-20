def mydecorator(func1):
    
    def wrapper(*args,**kwargs):
        func1(*args,**kwargs)
        print("I am wrapper Fuction")
        func1(*args,**kwargs)
    return wrapper

@mydecorator
def hello(x,y):
    print(x+y)
    

hello(10,20)

