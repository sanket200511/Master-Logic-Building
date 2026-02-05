# Problem: taxEligibility
age = int(input("Enter your age: "))
if age > 18:
    income = float(input("Enter your income: "))
    if income > 500000:
        print("You have to pay taxes")
    else:
        print("You dont have to pay any taxes")
else:
    print("You are not eligible for paying taxes")