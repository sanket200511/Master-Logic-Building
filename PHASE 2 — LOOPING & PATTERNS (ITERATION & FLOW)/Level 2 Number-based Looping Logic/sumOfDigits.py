# Question: sumOfDigits
inp = int(input("Enter any number: "))
sum = 0

while inp > 0:
    sum += inp % 10
    inp //= 10

print("Sum is:",sum)