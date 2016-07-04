#!/usr/bin/python3

def parrot(voltage,state='a staff',action='voom',type='Norwegin Blue'):
	print("-- This parrot wouldn't",action,end=' ')
	print("if you put",voltage,"volts through it.")
	print("--Lovely plumage, the",type)
	print("--It's",state,"!")

parrot(1000)                        #1 positional argument
parrot(voltage=1000)                #1 keyword argument
parrot(voltage=1000000,action='VOOOOM') #2 Keyword argument
parrot(action='Vooooom',voltage=1000000) #2 keyword argument
parrot('a million','bereft of life','jump') #3 positional argument
parrot('a thousand',state='pushing up the daisies') #1 positional, 1 keyword


