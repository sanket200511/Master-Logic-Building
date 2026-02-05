# Problem: multipleOrEndWith7
inp = int(input("Enter any Number: "))

if inp % 7 == 0 or inp % 10 == 7:
    print("Number is either multiple of 7 or ends with 7")
else:
    print("Number is neither multiple of 7 nor ends with 7")
