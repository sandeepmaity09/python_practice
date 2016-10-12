#!/usr/bin/python3

# Annotations are stored in the __annotations__ attribute of the function as a dictionary.
# No side effect on any other part of the function.
# Parameter annotations are defined by colon after the parameter name.
# Return annotations are defined by a literal ->, followed by an expression.

def f(ham:str,eggs:str='eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:",ham,eggs)
    return ham+' and '+eggs
 
