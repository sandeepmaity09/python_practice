#!/usr/bin/python3

# format styling 1
for x in range(1,11):
    print(repr(x).rjust(5),repr(x*x).rjust(5),repr(x*x*x).rjust(5),end=' ')
    print(repr(x*x*x).ljust(5),repr(x*x).ljust(5),repr(x).ljust(5))

# format styling 2
for x in range(1,11):
    print('{0:5d}{1:5d}{2:5d}'.format(x,x*x,x*x*x),end=' ')
    print('{0:-5d}{1:-5d}{2:-5d}'.format(x*x*x,x*x,x))

# str.ljust()
# str.rjust()
# str.center()
# str.zfill()

for x in range(1,11):
    print(repr(x).zfill(5),repr(x*x).zfill(5),repr(x*x*x).zfill(5))


# use positional args in str.format()

print('We are the {} who say "{}"'.format('knight','Ni!'))

# use keyword args in str.format()

print("This {food} is {adjective}.".format(food='spam',adjective='absolutely horrible'))

# use positional and keyword arguments

print('The story of {0}, {1}, and {other}.'.format('Bill','Manfred',other='Georg'))


# use of !r in the code

import math
print('The value of PI is approx {}'.format(math.pi))
print('The value of PI is approx {!r}'.format(math.pi))

# use of : in the str.format()

print('The value of PI is approx {0:.3f}.'.format(math.pi))

# Preety tables

tables={'Sjoerd':4125,'Jack':12322,'Dcab':12353}
for name,phone in tables.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))

# if you don't want to split the string 

table={'Sjored':12321,'Jack':123123123,'Dcab':23123123123123}
print('Jack:{0[Jack]:d}; Sjoerd:{0[Sjored]:d}; Dcab:{0[Dcab]:d}'.format(table))

# old style string formatting python2 style

print("The value of PI is approx %5.3f."%math.pi)

