# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

from functools import reduce
import os
import sys

with open(os.path.join(sys.path[0],'data_d1.txt'), 'r') as f:
    data = [i for i in f.read().strip().split('\n')]
    #print(data)

# Creation of a list of lists
data_list = []
tem = []
for i in data:
    if i == '':
        data_list.append(tem)
        tem = []
    else:
        tem.append(int(i))
#print(data_list)       #Optional, to keep track of how the file is changing
print('------------------------------')

# Use the reduce function to find the elf with the most calories
final_data = []
for i in data_list:
    result = (reduce(lambda y,z: y+z, i))
    final_data.append(result)
#print(final_data)      #Optional, to keep track of how the file is changing
print('------------------------------')

print(f'The elf with the most calories carries: {max(final_data)} calories')

# PART 2
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

#Sorting the final_data list will allow me to slice the list to obtain only the first 3 values
final_data.sort(reverse = True)
part2= final_data[:3]
part2_final = reduce(lambda x,y: x+y, part2)
print(f'The top three elves carrying the most calories are carrying {part2_final} calories')
