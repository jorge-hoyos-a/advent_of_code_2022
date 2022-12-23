# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen. 
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

import os, sys

a = "rock"
b = "paper"
c = "scissors"
# Points for selected shape
pt_a = 1
pt_b = 2
pt_c = 3
# Point for the outcome of the round
pt_lost = 0
pt_draw = 3
pt_win = 6

#Creating a list of tuples, where each tuple is one entry of the strategy guide
with open(os.path.join(sys.path[0],'data_d2.txt'), 'r') as f:
    data = [i for i in f.read().split('\n')]
    data2 = [tuple(i.replace(' ','')) for i in data]
    #print(data2)        #Optional, to keep track of how the file is changing
    print('-------------------')

# Running the strategy to obtain the total score
total_score = 0
for x in data2:
    pt_round = 0
    if x[0] == 'A':
        elf = a
    elif x[0] == 'B':
        elf = b
    else:
        elf = c
    
    if x[1] == 'X':
        me = a
        pt_round += pt_a
    elif x[1] == 'Y':
        me = b
        pt_round += pt_b
    elif x[1] == 'Z':
        me = c
        pt_round += pt_c
    total_score += pt_round
    
    # round
    if elf == me:
        total_score += pt_draw
    elif (me == a and elf == c) or (me == b and elf == a) or (me == c and elf == b):
        total_score += pt_win
    else:
        total_score += pt_lost
        
print(f'Total score: {total_score}')
print('-------------------')

# Part 2
# the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

total_score2 = 0

for x in data2:
    pt_round2 = 0
    if x[0] == 'A':
        elf = a
    elif x[0] == 'B':
        elf = b
    elif x[0] == 'C':
        elf = c
        
    if x[1] == 'X':
        total_score2 += pt_lost
        if elf == a:
            pt_round2 += pt_c
        elif elf == b:
            pt_round2 += pt_a
        else:
            pt_round2 += pt_b
    elif x[1] == 'Y':
        total_score2 += pt_draw
        if elf == a:
            pt_round2 += pt_a
        elif elf == b:
            pt_round2 += pt_b
        else:
            pt_round2 += pt_c
        
    elif x[1] == 'Z':
        total_score2 += pt_win
        if elf == a:
            pt_round2 += pt_b
        elif elf == b:
            pt_round2 += pt_c
        else:
            pt_round2 += pt_a
    total_score2 += pt_round2

print(f'Total score part 2: {total_score2}')
print('-------------------')