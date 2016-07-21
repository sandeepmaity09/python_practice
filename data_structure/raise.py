#!/usr/bin/python3

import collections

def sum(values):
	if not isinstance(values,collections.Iterable):
		raise TypeError('Paramenter must be an iterable type')
	total=0
	for v in values:
		if not isinstance(v,(int,float)):
			raise	TypeError("Elements must be numeric")
		total=total+v
	return total


