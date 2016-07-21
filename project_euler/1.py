#!/usr/bin/python3

def multiofthreefive(num):
	arr=list()
	for j in range(1,num):
		if (j%3==0 or j%5==0):
			arr.append(j)
	total=0
	for i in range(len(arr)):
		total+=arr[i]
	print(total)
	print(arr)

		
