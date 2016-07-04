#!/usr/bin/python3

#A set is unordered collection with no duplicate elements uses for membership testing and eliminating duplicates entries.

basket={'apple','orange','aaple','pear','orange','banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

#Demonstrate set operations on unique letters from to words

a=set('abracadabra')
b=set('alacazam')
print(a)
print(a-b)   #difference
print(a|b)   #union
print(a&b)   #intersection
print(a^b)   #symmetric difference

# NOTE: to create empty set use set() function not the {}, This {} is used for empty dict
