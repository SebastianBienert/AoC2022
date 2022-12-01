input = [x for x in open("day1.txt", "r").readlines()]
elfs = [[]]
elfs.extend([] for x in input if x=='\n' or elfs[-1].append(int(x.rstrip())))
elfs_sums = [sum(items) for items in elfs]
elfs_sums.sort(reverse=True)
day_1_2_result = sum(elfs_sums[0:3])

print(day_1_2_result)
