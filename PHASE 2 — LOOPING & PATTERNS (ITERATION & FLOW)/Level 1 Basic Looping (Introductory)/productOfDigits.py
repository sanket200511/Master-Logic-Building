# Question: productOfDigits
inp = input("Enter any number: ")
prod = 1
for i in range(len(inp)):
    prod *= int(inp[i])
print("Product of digits is: ",prod)