# Question: factorial
def fact(n):
    factorial = 1
    while n != 0 and n != 1:
        factorial *= n
        n -= 1
    return factorial
    # if n == 1 or n == 0:
    #     return 1
    # else:
    #     return fact(n - 1) * n

print(fact(int(input("Enter any number to find factorial: "))))