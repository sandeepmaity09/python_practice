#!/bin/usr/python3

words=['cat','window','defenestrate']
for w in words[:]:
	if len(w) > 6:
		words.append(w)
	
print(words)
