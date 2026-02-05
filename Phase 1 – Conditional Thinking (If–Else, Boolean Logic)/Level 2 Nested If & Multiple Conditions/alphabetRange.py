# Problem: alphabetRange
import sys

inp = input("Enter an alphabet: ").lower()
try:
    inp = ord(inp)
except Exception as e:
    print("Invalid input enter single alphabet from a - z")
    sys.exit()

if inp >= 97 and inp <= 109:
    print("Alphabet is in range a-m")
elif inp >= 110 and inp <= 122:
    print("Alphabet is in the range n-z")
else:
    print("Invalid input enter single alphabet from a - z")