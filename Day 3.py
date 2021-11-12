#This was attempt number 1 but I got lost in my own logic


#def get_tree_count(map, x_move, y_move):
#    count = 0
#    x_cord, y_cord = 0,0
#    x_length, y_length = len(map), len(map[0])

#    while (y_cord + 1) <= y_length:
#        if map[y_cord][x_cord % x_length] =='#':
#            count += 1
#            x_cord += x_move
#            y_cord += y_move
#        return count()

#def part1(map):
#    return get_tree_count (map, 3,1)




# attempt number 2: part 1

with open('Input 3.txt', 'r') as f:
    lines = f.readlines()

curve_x = 0
slope_x = 3
slope_y = 1
trees = 0

for curve_y, each_line in enumerate(lines):
    if each_line[curve_x] == "#":
        trees += 1
    curve_x = (curve_x + slope_x) % len(each_line[:-1])
print(f"The Solution Is: {trees}")

#part 2

slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]
mult_trees=1
for slope in slopes:
    print ("Slope: ", slope)
    slope_x, slope_y = slope
    trees = 0 
    curve_x = 0 
    for curve_y, each_line in enumerate(lines):
        if curve_y%slope_y == 0:
            if each_line[curve_x] == "#":
                trees += 1
            curve_x = (curve_x + slope_x) % len(each_line[:-1])
    print ("Trees On This Slope: ", trees)
    mult_trees = trees
print("Solution: ", mult_trees)