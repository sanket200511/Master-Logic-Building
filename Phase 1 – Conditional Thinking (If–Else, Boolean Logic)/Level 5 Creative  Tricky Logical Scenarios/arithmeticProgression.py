# Problem: arithmeticProgression
import sys
inp = list(map(int,input("Enter three numbers: ").split()))
check = 0
inp.sort()

check = inp[1] - inp[0]

for i in range(1,len(inp) - 1):
    if not inp[i + 1] - inp[i] == check:
        print("The numbers are not in Arithmatic Progression")
        sys.exit()
print("All numbers are in Arithmatic Progression")
