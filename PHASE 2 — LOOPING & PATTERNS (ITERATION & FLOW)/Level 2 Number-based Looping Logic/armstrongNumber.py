# Question: armstrongNumber
inp = input("Enter a number: ")
length = len(inp)
sum = 0

for i in range(length):
    sum += int(inp[i])**length

if sum == int(inp):
    print(inp,"is armstrong digit")
else:
    print(inp,"is not armstrong digit")


'''

#Enter input
num = int(input("Enter 3-digit number : "))
 
sum = 0
temp = num
#Define a function
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10
 
if sum==num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')

'''