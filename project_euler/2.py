#!/usr/bin/python3

def fibo():
	a,b=0,1
	arr=list()
	evenarr=list()
	total=0
	while b < 4000000:
		arr.append(b)
		a,b=b,a+b
	for i in range(len(arr)):
		if arr[i]%2==0:
			evenarr.append(arr[i])
	for j in range(len(evenarr)):
		total+=evenarr[j]
	print(evenarr)
	print(total)

fibo()
