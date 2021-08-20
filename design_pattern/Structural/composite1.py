from abc import ABCMeta , abstractmethod

class Idepartment(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self,employees):
		pass
	@abstractmethod
	def print_department(self):
		pass


class Accounting(Idepartment):

	def __init__(self,employees):
		self.employees=employees

	def print_department(self):
		print(f"Accounting Department : {self.employees}")


class Scholarship(Idepartment):

	def __init__(self,employees):
		self.employees=employees

	def print_department(self):
		print(f"Scholarship Department : {self.employees}")


class Parentdepartment(Idepartment):
	def __init__(self,employees):
		self.employees=employees
		self.base_employees=employees
		self.sub_dept = []

	def add_dep(self,dept):
		self.sub_dept.append(dept)
		self.employees +=dept.employees

	def print_department(self):
		print("Parent Department")
		print(f"Parent Department Base employees : {self.base_employees}")
		for dept in self.sub_dept:
			dept.print_department()

		print(f"Total Employees: {self.employees}")

dept1 = Accounting(200)
dept2=Scholarship(140)
parent_dept=Parentdepartment(30)

parent_dept.add_dep(dept1)
parent_dept.add_dep(dept2)

parent_dept.print_department()

				
		








