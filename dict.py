#!/usr/bin/python3

# Dictiionaries:- Assiciative Arrays or Memorys
# dict's are indexed by keys , immutable type, keys can be "string" or "numbers"
# Tuples can be used as keys if they contain strings numbers or tuples
# if you store using a key that is already in use , the old value associated with that key is forgotten.It is an error to extract a value using a now-existent key.

tel={'jack':4098,'sape':4238}
tel['guido']=2343
print(tel)
print(type(tel))
print(tel['jack'])
del tel['sape']
tel['irv']=2311
print(tel)
list(tel.keys())
sorted(tel.keys())
print('guido' in tel)
print('jack' not in tel)

# dict() constructor builds dict's directly from sequences of key-value pairs

print(dict([('sape',342),('jack',234),('guido',245)]))
print({x: x**2 for x in (2,4,6)})
