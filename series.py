#!/usr/bin/python3

ls=list()
ls.append(6)
temp=6
for i in range(1,106):
    temp+=16
    ls.append(ls[i-1]+temp)
# print(ls)                         for debug only

stt=list()
for i in range(len(ls)):
    temp=str(ls[i])
    if len(temp) < 6:
        l1=len(temp)
        l2=5-l1
        tmp='0'*l2
        newtemp=tmp+temp
        stt.append(newtemp)
    else:
        stt.append(str(ls[i]))
# print(stt)                          for debug only

"""
num=int(input())
z=0
for p in range(1,1+num):
    for q in range(1,p+1):
        print(stt[z],end=' ')
        z+=1
    print()
"""

"""
num=int(input())
z=0
temp=num
for p in range(1,1+num):
    for q in range(1,temp):
        print(' ',end='')
    temp=temp-1
    l=1
    while ( l <= ((2*p)-1)):
        print(stt[z],end=' ')
        z=z+1
        l=l+1
    print('')
"""

num=int(input())
z=0
row=1
p=num
while p>0:
    for q in range(1,p):
        print(' ',end='')
    for r in range(1,row+1):
        print(stt[z],end=' ')
        z=z+1
    print('\n')
    row=row+1
    p=p-1
