#!/usr/bin/python3

arr=list()

for i in range(2,1000):
	prime=True
	for j in range(2,i+1):
		if (i%j==0):
			prime=False
		if prime:
			arr.append(i)

arrset=set(arr)
print(arrset)
