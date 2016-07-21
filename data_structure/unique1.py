#!/usr/bin/python3

"""In the element uniquess problem, we are given a signle sequence S with n elements\
and asked whether all elements of that collection are distinct from each other or not."""

def unique1(S):
	"""Return True if there are no duplicates elements in sequence S."""
	for j in range(len(S)):
		for k in range(j+1,len(S)):
			if S[j]==S[k]:
				return False
	return True
