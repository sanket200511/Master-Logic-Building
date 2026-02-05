# Problem: sumFirstLastEqualMid
inp = int(input("ENter a three digit number: "))

last_digit = inp % 10
inp //= 10
middle_digit = inp % 10
first_digit = inp // 10

if first_digit + last_digit == middle_digit:
    print("First digit and Last digit is equal to Middle digit")
else:
    print("First digit and Last digit is not equal to Middle digit")


