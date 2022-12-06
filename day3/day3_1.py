def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

input = [(list(x)[:len(x)//2], list(x)[len(x)//2:]) for x in open("day3.txt", "r").readlines()]
intersections = [list(set(x[0]) & set(x[1])) for x in input]
priorites = [get_priority(x[0]) for x in intersections]
result = sum(priorites)
print(result)
