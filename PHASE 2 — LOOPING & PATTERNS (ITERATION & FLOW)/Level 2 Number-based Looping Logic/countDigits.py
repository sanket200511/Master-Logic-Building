# Question: countDigits
'''
inp = input("Enter any digit: ")

print("No. of Digits:",len(inp))
'''
inp = int(input("Enter any number: "))
count = 0

while inp > 0:
    inp //= 10
    count +=1

print("No. of digits: ",count)