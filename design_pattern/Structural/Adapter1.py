class Target():

	def request(self):
		return "Target : default target Behaviour"

class Adaptee():
	def specific_req(self):
		return "eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
	def request(self):
		return f" Adapter : (Translated) {self.specific_req()[::-1]}"

def Client_code(Target):
	print(Target.request(),end="")


if __name__ == '__main__':
	print("I can work fine with target objects:\n")
	target=Target()
	Client_code(target)

	adaptee =Adaptee()
	print("I can't understand Adaptee class , it has different interface")
	print(f"Adaptee interface is: {adaptee.specific_req()}",end="\n\n")

	print("I can work via Adapter")
	adapter = Adapter()
	Client_code(adapter)
