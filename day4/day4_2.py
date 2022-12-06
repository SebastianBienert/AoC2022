import re
input_numbers = [re.split(',|-', x.strip()) for x in open("day4.txt", "r").readlines()]
elf_pairs = [( set(range(int(x[0]), int(x[1]) + 1)), set(range(int(x[2]), int(x[3]) + 1)) ) for x in input_numbers]
result = sum(1 if (len(x[0] & x[1]) > 0) else 0 for x in elf_pairs)
print(result)