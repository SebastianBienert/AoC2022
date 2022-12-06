import re
from collections import deque

# stacks = [
#     deque(['Z','N']),
#     deque(['M', 'C', 'D']),
#     deque(['P'])
# ]

stacks = [
    deque(list('BZT')),
    deque(list('VHTDN')),
    deque(list('BFMD')),
    deque(list('TJGWVQL')),
    deque(list('WDGPVFQM')),
    deque(list('VZQGHFS')),
    deque(list('ZSNRLTCW')),
    deque(list('ZHWDJNRM')),
    deque(list('MQLFDS'))
]

input = [re.search(r"move (\d+) from (\d+) to (\d+)", x.strip()).groups() for x in open("day5.txt", "r").readlines()]

print(stacks)
for instruction in input:
    elements_to_move = int(instruction[0])
    move_from = int(instruction[1])
    move_to = int(instruction[2])
    popped_elements = []
    for _ in range(elements_to_move):
        popped_elements.append(stacks[move_from - 1].pop()) 
    popped_elements.reverse()
    for popped in popped_elements:
         stacks[move_to - 1].append(popped)
    #print(stacks)


result = ''.join([x.pop() for x in stacks])
print(result)