# Problem: validCalendarDate
import sys
date = int(input("Enter Date: "))
month = int(input("Enter Month: "))

no_of_days = {1 : "31" , 2 : "28" , 3 : "31" , 4 : "30" , 5 : "31" , 6 : "30" , 7 : "31" , 8 : "31" , 9 : "30" , 10 : "31" , 11 : "30" , 12 : "31"}

if month not in no_of_days:
    print("Enter a valid month")
    sys.exit()

days = int(no_of_days[month])

if 1 <= date <= days:
    print("It forms a valid calender")
else:
    print("It does not forms valid calender")