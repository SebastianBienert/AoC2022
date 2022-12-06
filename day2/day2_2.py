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

my_shapes = ['X', 'Y', 'Z']
oponent_shapes = ['A', 'B', 'C']

def get_correct_shape(oponent_shape, result):
    oponent_shape_index = oponent_shapes.index(oponent_shape)
    if result == 'Y':
        return my_shapes[oponent_shape_index]
    elif result == 'X':
        return my_shapes[(oponent_shape_index - 1) % 3]
    return my_shapes[(oponent_shape_index + 1) % 3]

input = [(x.split()[0], x.split()[1]) for x in open("day2.txt", "r").readlines()]
processed_input = [(x[0], get_correct_shape(x[0], x[1])) for x in input]
#print(processed_input)
rounds_score = [outcome_score[x] + shape_score[x[1]] for x in processed_input]
result = sum(rounds_score)
print(result)

