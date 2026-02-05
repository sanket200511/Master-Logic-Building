# Problem: medianOfThree
num = list(map(int,input("Enter a number: ").split()))

if num[1] <= num[0] <= num[2] or num[2] <= num[0] <= num[1]:
    print("Median: " , num[0])
elif num[0] <= num[1] <= num[2] or num[2] <= num[1] <= num[0]:
    print("Median: " , num[1])
else:
    print("Median: " , num[2])