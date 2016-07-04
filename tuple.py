#!/usr/bin/python3

empty=()  # creating tuple
print(type(empty))
empty=tuple()  # creation tuple
print(type(empty))
empty="hello",  # <---- note trailing comma for create a tuple with only one item
print(empty)
empty=23,34,'heelo' # to create tuple

x,y,z=empty               # sequence unpacking of tuple 
print(type(x))
print(type(y))
print(type(z))

