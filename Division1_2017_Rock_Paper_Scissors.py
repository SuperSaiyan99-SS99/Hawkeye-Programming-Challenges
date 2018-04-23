# -*- coding: utf-8 -*-
import os
import sys

'''
Rock Paper Scissors

Today we have a tournament of Rock Paper Scissors! 
Given an input of players and their random list of options 
return the result of the tournament following the rules of 
RPS below. Assume each round the player uses the next option 
that isn’t used in their list. If there is a tie, then both 
players move on to their next option. You will not return 
ties in your tournament results.

Scissors cuts Paper
Paper covers Rock
Rock crushes Scissors

Key: Rock: R, Scissors: S, Paper: P

Input Format
8
1,R,P,S,R,P,S,R,P,S
2,S,R,S,P,R,S,P,P,S
3,R,S,P,S,S,S,R,P,R
4,R,S,R,R,R,R,S,R,R
5,R,R,R,R,R,R,R,R,R
6,S,S,S,S,S,S,S,S,S
7,P,S,P,S,P,S,P,S,P
8,R,S,P,S,R,P,S,R,P

Constraints
The first line tells you how many players there are in this tournament.
Each line in the output represents a round in the tournament and we want to see every round and 
the move that the player used for that round. Assume that there are enough players to make an even tournament like below.
To build your bracket, you are to pair up 2 players in numerical order, i.e. 1 and 2, 3 and 4 etc.
Each player is represented by an integer and each game option is represented by a single uppercase letter.
The goal is to end up with one winner, and also show what move he would use in that last round.
Each player has enough options to win.

Sample Input 0
8
1,R,P,S,R,P,S,R,P,S
2,S,R,S,P,R,S,P,P,S
3,R,S,P,S,S,S,R,P,R
4,R,S,R,R,R,R,S,R,R
5,R,R,R,R,R,R,R,R,R
6,S,S,S,S,S,S,S,S,S
7,P,S,P,S,P,S,P,S,P
8,R,S,P,S,R,P,S,R,P

Sample Output 0
(1R,2S),(3P,4R),(5R,6S),(7P,8R)
(1P,3S),(5R,7S)
(3S,5R)
(5R)
'''

lines = None

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Division1_2017_Rock_Paper_Scissors.txt')
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except IOError:
    print('File ' + filename + ' doesn\'t exist, cannot continue!! Exiting!')
    sys.exit(1)
    

# Construct every team into a dictionary and store it into a dictionary
teams = []
number_of_rounds = int(lines[0].strip())
for i in range(1, number_of_rounds + 1, 1):
    team_number, options = i, lines[i].split(',')[1:]
    options[-1] = options[-1].rstrip() # Remove newline character on last element
    team = {'number': i, 'options': options, 'loser': False}
    teams.append(team)

def get_loser(team1, team2):
    loser = None
    while loser is None:
        t1option = team1['options'][0]
        t2option = team2['options'][0]
        
        # If the options are the same, attempt to shoot again
        if t1option == t2option:
            del team1['options'][0]
            del team2['options'][0]
            continue
                
        sys.stdout.write('({}{},{}{})'.format(team1['number'], team1['options'][0], team2['number'], team2['options'][0]))
        if i != len(teams) - 2:
            sys.stdout.write(',')
    
        if t1option == 'R' and t2option == 'P':
            del team2['options'][0]
            loser = team1
        elif t1option == 'R' and t2option == 'S':
            del team1['options'][0]
            loser = team2
        elif t1option == 'P' and t2option == 'R':
            del team1['options'][0]
            loser = team2
        elif t1option == 'P' and t2option == 'S':
            del team2['options'][0]
            loser = team1
        elif t1option == 'S' and t2option == 'R':
            del team2['options'][0]
            loser = team1
        elif t1option == 'S' and t2option == 'P':
            del team1['options'][0]
            loser = team2
     
    return loser


while len(teams) != 1:
    for i in range(0, len(teams), 2):   # Go through the teams array two at a time 
        team1 = teams[i]
        team2 = teams[i+1]
        
        loser = get_loser(team1, team2)
        if loser == team1:
            team1['loser'] = True
        elif loser == team2:
            team2['loser'] = True
        
    print
    
    # Delete all losers
    for i in range(len(teams)-1, -1, -1):
        if teams[i]['loser']:
            del teams[i]
   
        
print('({}{})'.format(teams[0]['number'], teams[0]['options'][0]))      
            
