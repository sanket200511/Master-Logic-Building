# Question: perfectNumber
import sys
inp = int(input("Enter any number to check whether it is perfect or not: "))
num = 1
sum = 0

while num <= inp//2:
    if inp % num == 0:
        sum += num
    num += 1
if sum == inp:
    print(inp,"is a perfect number")
else:
    print(inp,"is not a perfect number")
