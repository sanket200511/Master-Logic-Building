# Problem: perfectSquareNoSqrt
num = int(input("Enter any number to check: "))

if num < 0:
    print(num, "is NOT a perfect square.")
else:
    temp = num
    odd = 1

    while temp > 0:
        temp -= odd
        odd += 2

    if temp == 0:
        print(num, "is a perfect square.")
    else:
        print(num, "is NOT a perfect square.")
