class Conversion():
    def __init__(self,meter,conversion_to=None):
        self.meter=meter
        self.conversion_to = conversion_to

    def After_conversion(self):
        if self.conversion_to:
            conversion = self.conversion_to(self)
        return conversion

    def __repr__(self):
        statement = "Unit :{} meter , After conversion:{}"
        return statement.format(self.meter,self.After_conversion())
        


def Km(unit):
    return f"{unit.meter/1000} km"

def Feet(unit):
    return f"{unit.meter*3.281} feet"

def Centi(Unit):
    return f"{unit.meter*100} centimeter"

if __name__ == '__main__':
  

    print(Conversion(100, conversion_to = Km))
    print(Conversion(100, conversion_to = Feet))

        

