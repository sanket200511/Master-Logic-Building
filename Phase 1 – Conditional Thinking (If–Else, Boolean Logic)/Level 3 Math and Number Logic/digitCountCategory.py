# Problem: digitCountCategory
inp = int(input("Enter any integer: "))

check = inp % 1000

if check < 10:
    print("Single-Digit")
elif check >= 10 and check < 100:
    print("Double-Digit")
else:
    print("Multi-Digit")