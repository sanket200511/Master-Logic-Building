# Problem: digitSumVsProduct
inp = int(input("Enter any  integer between (1-9999): "))
first_digit = second_digit = third_digit = forth_digit = 0

if inp > 1000:
    forth_digit = inp % 10
    inp //= 10
    third_digit = inp % 10
    inp //= 10
    second_digit = inp % 10
    first_digit = inp // 10
    if first_digit + second_digit + third_digit + forth_digit > first_digit * second_digit * third_digit * forth_digit:
        print("Sum is greater than multiplication")
    elif first_digit + second_digit + third_digit + forth_digit < first_digit * second_digit * third_digit * forth_digit:
        print("Multiplication is greater than sum")
    else:
        print("Both sum and multiplication are equal")
elif inp > 100:
    third_digit = inp % 10
    inp //= 10
    second_digit = inp % 10
    first_digit = inp // 10
    if first_digit + second_digit + third_digit > first_digit * second_digit * third_digit:
        print("Sum is greater than multiplication")
    elif first_digit + second_digit + third_digit < first_digit * second_digit * third_digit:
        print("Multiplication is greater than sum")
    else:
        print("Both sum and multiplication are equal")
elif inp > 10:
    second_digit = inp % 10
    first_digit = inp // 10
    if first_digit + second_digit > first_digit * second_digit:
        print("Sum is greater than multiplication")
    elif first_digit + second_digit < first_digit * second_digit:
        print("Multiplication is greater than sum")
    else:
        print("Sum and Multiplication both are equal")
else:
    print("Digit is single digit")

