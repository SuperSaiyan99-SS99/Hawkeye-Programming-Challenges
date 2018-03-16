# -*- coding: utf-8 -*-
'''
Problem 5. March Angry Frustrations (Please don’t sue us)
'''
import sys

names = 'John, Tom, Abby, Susan, Emily, Bobby, Kevin, Alex'.split(', ')

while len(names) > 1:
    brackets = []
    for i in range(0, len(names), 2):
        brackets.append((names[i], names[i+1]))
        sys.stdout.write('({}, {})'.format(names[i], names[i+1]))
        if i < len(names) - 2:
            sys.stdout.write(', ')
    
    for bracket in brackets:
        if bracket[0] < bracket[1]:
            names.remove(bracket[1])
        else:
            names.remove(bracket[0])
    print()

print('({})'.format(names[0]))

    
