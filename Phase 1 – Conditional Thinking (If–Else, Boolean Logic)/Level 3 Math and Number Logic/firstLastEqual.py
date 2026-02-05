# Problem: firstLastEqual
inp = int(input("Enter 4 digit number: "))

last_digit = first_digit = 0

last_digit = inp % 10
first_digit = inp // 1000

if first_digit == last_digit:
    print("first digit is equal to last digit")
else:
    print("first digit is not equal to last digit")

