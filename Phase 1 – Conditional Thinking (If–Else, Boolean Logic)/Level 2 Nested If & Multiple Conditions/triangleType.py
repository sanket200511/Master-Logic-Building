# Problem: triangleType
inp = list(map(float,input("Enter three sides of a triangle: ").split()))

if inp[0] == inp[1] == inp[2]:
    print("Triangle is equilateral triangle")
elif inp[0] == inp[1] or inp[0] == inp[2] or inp[1] == inp[2]:
    print("Triangle is isoscales triangle")
else:
    print("Triangle is a scalene triangle")
