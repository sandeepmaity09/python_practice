#!/usr/bin/python3

def largest(num):
	arr=list()
	primearr=list()
	for i in range(2,num):
		if (num%i==0):
			arr.append(i)
	#print(arr)
	for j in range(len(arr)):
		if arr[j]==2:
			pass
		for k in range(2,arr[j]):
			if arr[j]%k==0:
				break
		else:
			primearr.append(arr[j])
	#print(arr)
	#print(primearr)
	primearr.reverse()
	return primearr[0]
