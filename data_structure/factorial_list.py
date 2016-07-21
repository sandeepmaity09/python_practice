#!/usr/bin/python3

def factorial_list(S):
	"""Takes a list S and returns a list of factorial's"""
	#A Quardatic Approach

	n=len(S)
	A=[0]*n
	for i in range(n):
		total=1
		for j in range(1,S[i]+1):
			total*=j
		A[i]=total
	return A
