# In how many assignment pairs does one range fully contain the other?
import os
import sys

example_data = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

def contained_ranges(dat:list):
    counter = 0
    for i in dat:
        # Split the string by the comma to obtain a list ob 2 strings
        x = i.split(',')
        
        # Split each string by the score, then cast the str into int, and form the ranges as l1, r1 and l2, r2 
        x2, y2 = x[0].split('-'), x[1].split('-')
        x3, y3 = [int(ii) for ii in x2], [int(ii) for ii in y2]
        l1, r1 = x3[0], x3[1]
        l2, r2 = y3[0], y3[1]

        # Check if one range contains the other
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r1 <= r2):
            counter += 1
    print(counter)
    return counter

#contained_ranges(example_data)

with open(os.path.join(sys.path[0],'data_d4.txt'), 'r') as f:
    data = [i.strip() for i in f.readlines()]

contained_ranges(data)

# Part 2 ------
def overlap(dat:list):
    counter2 = 0
    for i in dat:
        # Split the string by the comma to obtain a list ob 2 strings
        x = i.split(',')
        
        # Split each string by the score, then cast the str into int, and form the ranges as l1, r1 and l2, r2 
        x2, y2 = x[0].split('-'), x[1].split('-')
        x3, y3 = [int(ii) for ii in x2], [int(ii) for ii in y2]
        l1, r1 = x3[0], x3[1]+1
        l2, r2 = y3[0], y3[1]+1
        range_a = range(l1,r1)
        range_b = range(l2,r2)

        # cast the range a into a set to use the intersection method
        set_a =set(range_a)
        result = set_a.intersection(range_b)
        
        # Check if intersesction result is not empty
        if result:
            counter2 += 1
    print(counter2)
    return counter2

overlap(example_data)
overlap(data)