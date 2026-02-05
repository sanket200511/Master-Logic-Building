# Problem: pointOnAxis
# Problem: quadrantFinder
x = int(input("Enter co-ordinate of point x: "))
y = int(input("Enter co-ordinate of point y: "))

if x == 0 and y == 0:
    print(f"the {x},{y} co-ordinates lies at the origin")
elif x == 0 and y > 0 or x == 0 and y < 0:
    print(f"the {x},{y} co-ordinates lies on the y-axis")
elif x > 0 and y == 0 or x < 0 and y == 0:
    print(f"the {x},{y} co-ordinates lies on the x-axis")
elif x > 0 and y > 0:
    print(f"the {x},{y} co-ordinates lies on the first quadrant")
elif x < 0 and y > 0:
    print(f"the {x},{y} co-ordinates lies on the second quadrant")
elif x < 0 and y < 0:
    print(f"the {x},{y} co-ordinates lies on the third quadrant")
elif x > 0 and y < 0:
    print(f"the {x},{y} co-ordinates lies on the fourth quadrant")
