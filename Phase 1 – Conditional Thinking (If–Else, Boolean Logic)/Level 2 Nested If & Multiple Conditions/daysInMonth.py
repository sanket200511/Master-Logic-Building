# Problem: daysInMonth
inp = int(input("Enter the month number 1-12: "))
no_of_days = {1 : "31" , 2 : "28" , 3 : "31" , 4 : "30" , 5 : "31" , 6 : "30" , 7 : "31" , 8 : "31" , 9 : "30" , 10 : "31" , 11 : "30" , 12 : "31"}

print(f"No. of days in month {inp} is {no_of_days[inp]}")
