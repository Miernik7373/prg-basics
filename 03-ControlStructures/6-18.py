x = int(input("Enter the first coordinate for the point P: "))
y = int(input("Enter the second coordinate for the point P: "))
quadrant = 0
if x == 0 and y != 0:
    print(f"The point is located on Y-axis, with y={y}")
elif y == 0 and x != 0:
    print(f"The point is located on X-axis, with x={x}")
elif x == 0 and y == 0:
    print(f"Point P({x},{y}) is located in the position (0,0))")
if x>0 and y>0:
    quadrant = "first"
    print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
elif x<0 and y>0:
    quadrant = "second"
    print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
elif x<0 and y<0:
    quadrant = "third"
    print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
elif x>0 and y<0:
    quadrant = "fourth"
    print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
