

def print_plane(plane):
    for line in plane:
        print(line)
    print('\n')
        
def print_knot_on_plane(plane, knot):
    plane[knot.y][knot.x] = knot.type
    
def clear_knot_from_plane(plane, knot):
    plane[knot.y][knot.x] = '.'
    
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
       

head = Knot(0, yMax - 1, 'H')
tail = Knot(0, yMax - 1, 'T')

#main loop
#print_knot_on_plane(plane, tail)
#print_knot_on_plane(plane, head)
#print_plane(plane)
for series in input:
    steps = series[1]
    for _ in range(0, steps):
        #clear_knot_from_plane(head)
        #clear_knot_from_plane(tail)
        head.move(series[0], 1)
        if not head.is_knot_touching(tail):
            if head.x == tail.x or head.y == tail.y:
                tail.move(series[0], 1)
            else:
                if series[0] == 'R' or series[0] == 'L':
                    if tail.y > head.y:
                        tail.move(series[0] + 'U', 1)
                    else:
                        tail.move(series[0] + 'D', 1)
                else:
                    if tail.x > head.x:
                        tail.move('L' + series[0], 1)
                    else:
                        tail.move('R' + series[0], 1)
        #print_knot_on_plane(tail)
        #print_knot_on_plane(head)
        #print_plane(plane)

print(len(tail.visited_positions))
#print(tail.visited_positions)
#print_position(plane, tail.visited_positions)
#print_plane(plane)
