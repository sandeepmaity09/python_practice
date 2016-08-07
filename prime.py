#!/usr/bin/python3


numb=int(input())
prime=list()
import math
for num in range(1,numb):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       prime.append(num)
print(prime)
