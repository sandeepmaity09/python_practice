#!/usr/bin/python3

num=int(input())
lis=list()
while num > 0:
	rem=num%2
	lis.append(rem)
	num=num//2
sorted(lis)
count=0
for i in range(len(lis)):
	if lis[i]==0:
		continue
	else:
		count+=1
print(count)

