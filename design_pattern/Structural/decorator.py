def decorator_func(inner_fun): #creating Decorator_func and giving another function as a parameter
    def wrap_func(): # creating Inner func named wrap_func
        print("this will print first")
        inner_fun()  # invoking Another func passed as parameter 
        print("this will print last")
    return wrap_func #returning function 

@decorator_func  # decorator
def magic_fun(): # creating func that will be called
    print("This is Magical !!!")

@decorator_func    
def normal():
    print("Using Decorator in another func...")
    

output = magic_fun() # calling func
print("\n \n ********************* \n \n ")
output=normal()


