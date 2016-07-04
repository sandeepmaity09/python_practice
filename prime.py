#!/bin/usr/python3

num = int(input("Enter a Number\n"))
if(num<0):
	print("Please enter a positive number")
elif num==1:
	print("Prime Number")
elif num>=2:
	for i in range(2,num):
		if num%i==0:
			print(num,'equals',i,'*',num//i)
			print(num,'is not a prime number')
			break
	else:
		print(num,'is a prime number')

