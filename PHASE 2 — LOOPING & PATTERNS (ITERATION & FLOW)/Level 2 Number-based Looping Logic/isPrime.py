# Question: isPrime
'''
import sys
inp = int(input("Enter any number to check whether it is prime or not: "))
num = 2

while num < inp//2:
    if inp % num == 0:
        print(inp,"is not prime number")
        sys.exit()
    num += 1
print(inp,"is prime number")
'''

import math

inp = int(input("Enter any number: "))

if inp <= 1:
    print(inp, "is not a prime number")
    exit()

for num in range(2, int(math.sqrt(inp)) + 1):
    if inp % num == 0:
        print(inp, "is not a prime number")
        break
else:
    print(inp, "is a prime number")
