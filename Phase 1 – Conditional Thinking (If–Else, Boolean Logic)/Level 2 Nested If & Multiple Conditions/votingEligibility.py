# Problem: votingEligibility
inp = int(input("Enter your age: "))

if inp < 18:
    print("You are not eligible")
elif inp >= 18:
    print("You are eligible for voting")
else:
    print("Invalid input")