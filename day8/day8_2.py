input = [list(x.strip()) for x in open("day8.txt", "r").readlines()]

def get_scenic_score(plane, x, y):
    height = int(plane[y][x])
    trees_to_left = [int(h) for h in plane[y][:x]]
    trees_to_left.reverse()
    trees_to_right = [int(h) for h in plane[y][x + 1:]]
    trees_above = [int(column[x]) for column in plane[:y]]
    trees_above.reverse()
    trees_under = [int(column[x]) for column in plane[y + 1:]]
    
    left_score = scenic_score(height, trees_to_left)
    above_score = scenic_score(height, trees_above)
    right_score = scenic_score(height, trees_to_right)
    under_score = scenic_score(height, trees_under)
    return left_score * above_score * right_score * under_score

def scenic_score(height, trees):
    if len(trees) == 0:
        return 0
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            break
    return score

trees_score = []
for y in range(len(input)):
    for x in range(len(input[0])):
        scenic_score_all = get_scenic_score(input, x, y)
        trees_score.append(scenic_score_all)
            
print(max(trees_score))