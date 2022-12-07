input = open("./day6.txt", "r").read().strip()
#print(input)

for idx in range(0, len(input), 1):
    distinct_chars = set(input[idx : idx + 14])
    #print(distinct_chars)
    if len(distinct_chars) == 14:
        print(idx + 14)
        break