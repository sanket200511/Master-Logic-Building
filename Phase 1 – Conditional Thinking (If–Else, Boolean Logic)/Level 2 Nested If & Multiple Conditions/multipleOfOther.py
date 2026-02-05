num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == 0 or num2 == 0:
    print("0 cannot be a multiple or divisor in this context")
elif num1 >= num2:
    if num1 % num2 == 0:
        print(f"{num1} is a multiple of {num2}")
    else:
        print(f"{num1} is not a multiple of {num2}")
else:
    if num2 % num1 == 0:
        print(f"{num2} is a multiple of {num1}")
    else:
        print(f"{num2} is not a multiple of {num1}")
