#!/usr/bin/python3

def fib(n): #write Fibonacci series up to n
	"""Print a Fibonacci series up to n steps."""
	a,b=0,1
	temp=0
	while temp < n:
		print(a,end=' ')
		a,b=b,a+b
		temp=temp+1
	print()

#Now call the function we just defined
fib(20)
