#!/usr/bin/python3

def factorial(n):
    temp=1
    for i in range(1,n+1):
	temp=temp*i
    print(temp)

num=int(input())
factorial(num)
