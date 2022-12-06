def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

input = [list(x.strip()) for x in open("day3.txt", "r").readlines()]
groups = [input[x: x + 3] for x in range(0, len(input), 3)]
intersections = [list(set(x[0]) & set(x[1]) & set(x[2])) for x in groups]
priorites = [get_priority(x[0]) for x in intersections]
result = sum(priorites)
print(result)

# intersections = [list(set(x[0]) & set(x[1])) for x in input]
# priorites = [get_priority(x[0]) for x in intersections]
# result = sum(priorites)
# print(result)
