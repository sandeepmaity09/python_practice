#!/usr/bin/python3

def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

	fibTotal=0
	n=1
	while(fib(n)<4000000):
		if(fib(n)%2==0):
			fibTotal=fibTotal+fib(n)
		n+=1
	print(fibtotal)
