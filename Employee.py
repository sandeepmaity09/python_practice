#!/usr/bin/python3

class Employee:
	'Common base class for all employess'
	empCount=0

	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1

	def __del__(self):
		class_name=self.__class__.__name__
		print(class_name,"destroyed")

	def displayCount(self):
		print("Total Employee",Employee.empCount)

	def displayEmployee(self):
		print("Name:",self.name,"\n","Salary:",self.salary)
	
	
print("Employee.__doc__",Employee.__doc__)
print("Employee.__name__",Employee.__name__)
print("Employee.__module__",Employee.__module__)
print("Employee.__bases__",Employee.__bases__)
print("Employee.__dict__",Employee.__dict__)
