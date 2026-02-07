# Question: palindromeCheck

import sys
inp = input("Enter any number: ")

start = 0
end = len(inp) - 1

for i in range(len(inp) // 2):
    if not inp[start] == inp[end]:
        print("Number is not palindrome")
        sys.exit()
    start += 1
    end -= 1

print("Number is palindrome")
'''

if inp == inp[::-1]:
    print("Nummber is palindrome")
else:
    print("Number is not palindrome")

'''

