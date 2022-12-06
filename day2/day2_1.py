outcome_score = {
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('C', 'Y'): 0,

    ('A', 'X'): 3,
    ('B', 'Y'): 3,
    ('C', 'Z'): 3,


    ('A', 'Y'): 6,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
}

shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


input = [(x.split()[0], x.split()[1]) for x in open("day2.txt", "r").readlines()]
rounds_score = [outcome_score[x] + shape_score[x[1]] for x in input]
result = sum(rounds_score)
print(result)