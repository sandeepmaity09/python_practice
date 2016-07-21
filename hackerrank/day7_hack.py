#!/usr/bin/python3

from __future__ import print_function

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
        try:
            query=input()
            if query in dic.keys():
                print('{}={}'.format(query,dic[query]))
            elif query not in dic.keys():
                print("Not found")
        except (EOFError):
            break
