#!/usr/bin/python3

squares=list(map(lambda x:x**2,range(10)))
print(squares)


#Another Method

squares=[x**2 for x in range(10)]
print(squares)
