from abc import ABCMeta, abstractmethod

class Ihandler(metaclass = ABCMeta):
    @abstractmethod
    def next_successor(self,successor):
        pass
    @abstractmethod
    def handle(self,amount):
        pass

class Withdraw_10(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor=successor

    def handle(self,amount):

        if amount>=10:
            num=amount//10
            rem = amount%10
            print(f"Dispensing {num} 10 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)

class Withdraw_20(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor = successor

    def handle(self,amount):

        if amount>=20:
            num=amount//20
            rem = amount%20
            print(f"Dispensing {num} 20 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)
            
class Withdraw_50(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor = successor

    def handle(self,amount):

        if amount>=50:
            num=amount//50
            rem = amount%50
            print(f"Dispensing {num} 50 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)

class Withdraw_100(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor = successor

    def handle(self,amount):

        if amount>=100:
            num=amount//100
            rem = amount%100
            print(f"Dispensing {num} 100 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)

class Withdraw_500(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor = successor

    def handle(self,amount):

        if amount>=500:
            num=amount//500
            rem = amount%500
            print(f"Dispensing {num} 500 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)

class Withdraw_2000(Ihandler):

    def __init__(self):
        self._successor=None

    def next_successor(self,successor):
        self._successor = successor

    def handle(self,amount):

        if amount>=2000:
            num=amount//2000
            rem = amount%2000
            print(f"Dispensing {num} 2000 rupee note")
            if rem!=0:
                self._successor.handle(rem)

        else:
            self._successor.handle(amount)



class Atm_Dispence():

    def __init__(self):

        self.chain1 = Withdraw_2000()
        self.chain2 = Withdraw_500()
        self.chain3 = Withdraw_100()
        self.chain4 = Withdraw_50()
        self.chain5 = Withdraw_20()
        self.chain6 = Withdraw_10()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
        self.chain3.next_successor(self.chain4)
        self.chain4.next_successor(self.chain5)
        self.chain5.next_successor(self.chain6)


atm = Atm_Dispence()
Amount = int(input("How much money you want to withdraw"))

if Amount<10 or Amount%10!=0:
    print("Please enter amount in multiple of 10s.")

atm.chain1.handle(Amount)
            
            
            
                       

    
        
            

