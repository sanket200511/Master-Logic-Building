# Problem: parityComparison
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")

elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd")

elif num1 % 2 == 0 and num2 % 2 != 0:
    print("num1 is even and num2 is odd")

else:
    print("num1 is odd and num2 is even")
