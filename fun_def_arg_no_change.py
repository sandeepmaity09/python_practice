#!/usr/bin/python3

#The default values are evaluated at the point of function defination in the defining scope so that i will print 5 in all condition

i=5
def f(arg=i):
	print(arg)
i=6
f()
i=23
f()
i=26523423
f()
