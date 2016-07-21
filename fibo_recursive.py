#!/usr/bin/python3

def fib(n):
	arr=list()
	if n < 2:
		arr.append(1)
	else:
		arr.append(int(fib(n-1)) + int(fib(n-2)))
