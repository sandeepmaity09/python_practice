#!/usr/bin/python3

T=int(input())
for i in range(T):
	string=str(input())
	print(string[::2],end=' ')
	print(string[1::2])

