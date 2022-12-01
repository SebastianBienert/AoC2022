input = [x for x in open("day1.txt", "r").readlines()]
elfs = [[]]
elfs.extend([] for x in input if x=='\n' or elfs[-1].append(int(x.rstrip())))
elfs_sums = [sum(items) for items in elfs]
day_1_result = max(elfs_sums)
print(day_1_result)