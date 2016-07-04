#!/usr/bin/python3

# Code for list combination

print([(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y])


# Same code with full code

combs=[]
for x in [1,2,3]:
	for y in [1,2,3]:
		if x!=y:
			combs.append((x,y))

print(combs)
