#!/usr/bin/python3

#To loop over two or more sequences at the same time, the entries can be paired with zip() function

questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
	print('What is your {0}? It is {1}.'.format(q,a))  # <---- Here is .(dot) not ,(comma)

