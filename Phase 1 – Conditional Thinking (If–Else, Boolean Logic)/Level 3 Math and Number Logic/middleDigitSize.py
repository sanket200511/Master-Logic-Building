# Problem: middleDigitSize
inp = int(input("Enter a three digit number: "))

first_num = second_num = third_num = 0

third_num = inp % 10
inp //= 10
second_num = inp % 10
inp //= 10
first_num = inp % 10
inp //= 10

if first_num > second_num and first_num > third_num:
    print(f"{first_num} is Greatest")
elif second_num > first_num and second_num > third_num:
    print(f"{second_num} is Greatest")
else:
    print(f"{third_num} is Greatest")