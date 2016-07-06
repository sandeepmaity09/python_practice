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
	query=str(input())
	if query == EOF:
		check = False

	if query in dic.keys():
		print(query,'=',dic[query])
	else:
		print("Not found")
