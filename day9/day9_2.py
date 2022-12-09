def print_plane(plane):
    for line in plane:
        print(line)
    print('\n')
        
def print_knot_on_plane(plane, knot):
    plane[knot.y][knot.x] = knot.type
    
def print_knots_on_plane(plane, knots):
    for knot in reversed(knots):
        print_knot_on_plane(plane, knot)
    
def clear_knot_from_plane(plane, knot):
    plane[knot.y][knot.x] = '.'
    
def clear_knots_from_plane(plane, knots):
    for knot in knots:
        clear_knot_from_plane(plane, knot)
    
def print_position(plane, positions):
    for pos in positions:
        plane[pos[1]][pos[0]] = '#'
        
input = [(x.split()[0], int(x.split()[1])) for x in open("day9.txt", "r").readlines()]

xMax = 100000
yMax = 100000

#plane = [['.' for x in range(xMax)] for y in range(yMax)] 

class Knot:
    def  __init__(self, x, y, type):
       self.x = x
       self.y = y
       self.type = type
       self.visited_positions = set([(self.x, self.y)])
    
    def move(self, dir, step):
        if 'R' in dir:
            self.x += step
        if 'L' in dir:
            self.x -= step
        if 'U' in dir:
            self.y -= step
        if 'D' in dir:
            self.y += step
        self.visited_positions.add((self.x, self.y))
            
    def is_knot_touching(self, other_knot):
        return abs(self.x - other_knot.x) <= 1 and abs(self.y - other_knot.y) <= 1
       
yCord = 15
xCord = 11

head = Knot(xCord, yCord, 'H')
knots = [head, *[Knot(xCord, yCord, str(x)) for x in range(1, 10)]]


def knots_pair_move(head, tail):
    if not head.is_knot_touching(tail):
        if head.x == tail.x:
            if head.y > tail.y:
                tail.move('D', 1)
            elif head.y < tail.y:
                tail.move('U', 1)
        elif head.y == tail.y:
            if head.x > tail.x:
                tail.move('R', 1)
            elif head.x < tail.x:
                tail.move('L', 1)
        else:
            if head.y > tail.y and head.x > tail.x:
                tail.move('RD', 1)
            elif head.y < tail.y and head.x > tail.x:     
                tail.move('RU', 1)
            elif head.y > tail.y and head.x < tail.x:
                tail.move('LD', 1) 
            elif head.y < tail.y and head.x < tail.x:     
                tail.move('LU', 1)
                
               

#main loop
#print_knots_on_plane(plane, knots)
#print_plane(plane)
for series in input:
    steps = series[1]
    move = series[0]
    for _ in range(0, steps):
        #clear_knots_from_plane(plane, knots)
        head.move(move, 1)
        for idx, knot in enumerate(knots[:-1]):
            knots_pair_move(knot, knots[idx + 1])
        #print_knots_on_plane(plane, knots)
        #print_plane(plane)

    #print_knots_on_plane(plane, knots)
    #print_plane(plane)

print(len(knots[9].visited_positions))
#print(knots[9].visited_positions)

#clear_knots_from_plane(plane, knots)
#print_position(plane, knots[9].visited_positions)
#print_plane(plane)
