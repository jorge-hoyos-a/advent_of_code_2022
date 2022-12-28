# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

import sys
import os
dat = ['vJrwpWtwJgWrhcsFMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
priorities = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

with open(os.path.join(sys.path[0], 'data_d3.txt'), 'r') as f:
    data = [i.rstrip() for i in f.readlines()]
    # print(data)


def priority_part1(data_list):
    total_priority = 0
    for i in data_list:
        n = len(i)
        
        if n % 2 == 0:
            s1 = i[0:n//2]
            s2 = i[n//2:]
        else:
            s1 = i[0:(n//2+1)]
            s2 = i[(n//2+1):]

        common = ''.join(set(s1).intersection(s2))
        #print(common)
        priority = priorities[common]
        total_priority += priority

    print(total_priority)
    return total_priority

priority_part1(data)

# Part 2
# Take packs of 3 elves and find the common character, then repeat the operation in part 1

total_priority2 = 0

#Creates a chunk list of 3 elements from data
for i in range(0, len(data), 3):
    chunk = data[i:i+3]
    
    #Transforms each string of chunk in a set to apply the intersect function
    sets = [set(s) for s in chunk]
    common_chars = set.intersection(*sets)
    
    #Transforms the common element in a list and then stores the value in a variable to find the priority from the dictionary
    common_list = list(common_chars)
    common = common_list[0]
    
    priority = priorities[common]
    total_priority2 += priority
print(total_priority2)
