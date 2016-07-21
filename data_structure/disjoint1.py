#!/usr/bin/python3

#Three-Way Set Disjointness:- determine if the intersection of the three sequences is empty.
#Running time analysis = O(n) power 3
def disjoint1(A,B,C):
	"""Return True if there is no element common to all three lists."""
	for a in A:
		for b in B:
			for c in C:
				if a==b==c:
					return False
	return True
