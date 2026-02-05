# Problem: geometricProgression
import sys
inp = list(map(int,input("Enter three numbers: ").split()))
check = 0
'''
print(inp[0] / inp[1])
print(inp[1] / inp[2])

if inp[0] / inp[1] == inp[1] / inp[2]:
    print("All three numbers are in Geometric Progression")
else:
    print("The numbers are not in Geometric Progression")
'''
check = inp[0] / inp[1]

for i in range(2,len(inp)):
    if not check == inp[i - 1] / inp [i]:
        print("The numbers are not in Geometric Progression")
        sys.exit()
print("All numbers are in Geometric Progression")