# Problem: validTriangle
import sys

inp = list(map(float,input("Enter the side: ").split()))
try:
    a,b,c = inp
except Exception as e:
    print(e)
    sys.exit()
    
if a + b > c and b + c > a and a + c > b:
    print("It forms a valid triangle")
else:
    print("It does not forms a valid triangle")