class kettle():
    power_source="electricity"
    def __init__(self,make,price):
        self.make=make
        self.price=price
        self.on=False

    def switch_on(self):
        self.on=True
kenwood = kettle("kenwood",8.90)
print(kenwood.make)
print(kenwood.price)
kenwood.price=13
print(kenwood.price)

hamilton = kettle("hamilton",14.55)

print("models: {} = {}, {} = {}".format(kenwood.make,kenwood.price,
                                        hamilton.make,hamilton.price))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
print("changing power source")

kettle.power_source="atomic"
print(kettle.power_source)

kenwood.power_source="gas"
print(kenwood.power_source)
print(hamilton.power_source)
