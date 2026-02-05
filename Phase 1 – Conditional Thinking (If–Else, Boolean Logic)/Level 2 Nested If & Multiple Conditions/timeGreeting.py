# Problem: timeGreeting
hour = int(input("Enter an hour: "))

if hour >= 1 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >=17 and hour <= 20:
    print("Good Evening")
else:
    print("Good Night")