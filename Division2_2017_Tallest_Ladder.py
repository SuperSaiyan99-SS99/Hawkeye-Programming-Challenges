''' Tallest Ladder '''
import os
from sys import exit

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Division2_2017_Tallest_Ladder.txt')
print(filename)

lines = None
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except IOError:
    print('Cannot open file ' + filename + '! Exiting')
    exit(1)
 
ladders = [int(ladder.rstrip()) for ladder in lines[1:]]
print(max(ladders))