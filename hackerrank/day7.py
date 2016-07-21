#!/usr/bin/python5

T=int(input())
dic=dict()
for i in range(T):
	string=str(input())
	sstring=string.split(' ',2)
	key=sstring[0]
	value=int(sstring[1])
	dic.update({key:value})

check=True
while check:
	query=input()
	if query == '':
		check = False
	else:
		if query in dic.keys():
			print(query,'=',dic[query])
		elif query not in dic.keys():
			print("Not found")
