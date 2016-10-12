#!/usr/bin/python3

# *name = tuple [im-mutable list]
# **name = dicttionary [ dictionary = Key-Value pair's]

# *name always comes before **name in arguments list

#import sys

def chesseshop(kind,*arguments,**keywords):
	print("--Do you have any",kind,"?")
	print("--I'm sorry, we're all out of",kind)
	print("-"*50)
	for arg in arguments:
		print(arg)
	print("-"*40)
	#keys=keywords.keys()
	#print(keys)
	keys=sorted(keywords.keys())
	#print(keys)
	for kw in keys:
		print(kw,":",keywords[kw])

chesseshop("Limburger","It's very runny,sir.","It's really very,VERY, runny,sir.","just go and fuck yourself","You don't have any limburger",shopkeeper="Michael palin",client="John Cleese",sketch="Cheese Shop Sketch")

#sys.exit(0)
