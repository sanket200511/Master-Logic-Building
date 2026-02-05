# Problem: posSumUnder100
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > 0 and num2 > 0 and num1 + num2 < 100:
    print("Both numbers are positive and their sum is less than 100")
else:
    print("Either both numbers are not positive or their sum is not less than 100 or both")

    
