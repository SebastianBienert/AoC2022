input = [list(x.strip()) for x in open("day8.txt", "r").readlines()]

def get_visibility(plane, x, y):
    height = int(plane[y][x])
    trees_to_left = [int(h) for h in plane[y][:x]]
    trees_to_right = [int(h) for h in plane[y][x + 1:]]
    trees_above = [int(column[x]) for column in plane[:y]]
    trees_under = [int(column[x]) for column in plane[y + 1:]]
    
    return (
        are_trees_lower(height, trees_to_left),
        are_trees_lower(height, trees_above),
        are_trees_lower(height, trees_to_right),
        are_trees_lower(height, trees_under)
    )

def are_trees_lower(height, trees):
    if trees is None or len(trees) == 0:
        return True
    return all(height > tree for tree in trees)

visible_trees_count = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        (left, above, right, under) = get_visibility(input, x, y)
        if(left or above or right or under):
            visible_trees_count += 1
            
print(visible_trees_count)