from abc import ABCMeta, abstractmethod

class Item(metaclass=ABCMeta):
	@abstractmethod
	def return_price(self):
		pass

class Box(Item):
	def __init__(self,contents):
		self.contents=contents

	def return_price(self):
		price=0
		for item in self.contents:
			price = price + item.return_price()
		return price

class Phone(Item):
	def __init__(self,price):
		self.price=price

	def return_price(self):
		return self.price
	 
class Charger(Item):
	def __init__(self,price):
		self.price=price

	def return_price(self):
		return self.price
	 
class Earphone(Item):
	def __init__(self,price):
		self.price=price

	def return_price(self):
		return self.price

phone_case_content = []
phone_case_content.append(Phone(20000))
phone_case_box = Box(phone_case_content)

Box_content = []
Box_content.append(phone_case_box)
Box_content.append(Earphone(550))
Box_content.append(Charger(1500))

box = Box(Box_content)

print("Total Price: " + str(box.return_price()))

	 

