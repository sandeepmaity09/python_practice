#!/usr/bin/python3

def find_max(data):
	"""Find Maximum element from a non-empty Python list."""
	biggest=data[0]
	for val in data:
		if val > biggest:
			biggest = val
	return biggest
