# Problem: largestOfThree
inp = list(map(int , input("Enter a number: ").split()))

if inp[0] > inp[1] and inp[0] > inp[2]:
    print(f"{inp[0]} is greatest")
elif inp[1] > inp[0] and inp[1] > inp[2]:
    print(f"{inp[1]} is greatest")
else:
    print(f"{inp[2]} is greatest")