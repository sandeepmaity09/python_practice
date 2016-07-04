#!/usr/bin/python3

# Function Annotations are completely optional metadata info about the types used by user-defined functions

def f(ham:str,eggs:str='eggs') -> str:
	print("Annotations:",f.__annotations__)
	print("Arguments:",ham,eggs)
	return ham+' and '+eggs
f('spam')
print(f('spam'))
