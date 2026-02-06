# Question: sumOddUpToN
inp = int(input("Enter any number: "))
sum = 0
for i in range(1,inp+1,2):
    sum += i
print("Sum is :",sum)