#!/usr/bin/python3

class Parent:
	__parentAttr=100
	def __init__(self):
		print("Calling Parent Constructor")
	
	def parentMethod(self):
		print("Calling Parent Method")

	def setAttr(self,attr):
		Parent.__parentAttr=attr

	def getAttr(self):
		print("Parent Attribute",Parent.__parentAttr)

	def myMethod(self):
		print("Calling parent Method")

class Child(Parent):
	def __init__(self):
		print("Calling Child Constructor")

	def childMethod(self):
		print('Calling child Method')

	def myMethod(self):
		print("calling Child Method")


c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
