#!/usr/bin/python3

def factorial(n):
	if n==1:
		return n
	else:
		return n*factorial(n-1)
num=int(input())
fact=factorial(num)
print(fact)
