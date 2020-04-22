
s = 'Hello \n World'
print(str(s))
print(repr(s))

#for x in range(1,11):
#    print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(3)[:3])

table = {'Thang': '300491', 'Huy': '130891', 'Linh': '041291'}
print('Thang: {Thang}; Huy: {Huy}; Linh: {Linh}'.format(**table))

import math
print('The value of PI is approximately %6.4f' % math.pi)

contents = 'Tỏi'
print('My hovercraft is full of {0} with the ACSII code of {0!a}.'.format(contents))

'''
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
'''
