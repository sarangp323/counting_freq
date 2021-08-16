class Duck():

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("come on it, the water is lovely")

    def quack(self):
        print("Quack Quack")

class Penguin():
    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("come on in, but it's a bit chilly this far south")

    def quack(self):
        print("I am a Penquin")
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
