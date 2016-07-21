#!/usr/bin/python3

def polynomial(S):
	"""Takes a list and gives the polynomial of n*n where n belongs to S"""
	
	n=len(S)
	A=[0]*n
	
	for j in range(n):
		total=1
		for i in range(0,S[j]):
			total=total*S[j]
		A[j]=total
	return A
