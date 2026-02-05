# Problem: tempCategory
temp = float(input("Enter the temperature: "))

if temp < 15:
    print("Cold")
elif temp >= 15 and temp <= 30:
    print("Warm")
else:
    print("Hot")