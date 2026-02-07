# Question: fibonacciSeries
inp = int(input("Enter max number to find fibonnaci series: "))
count = 0
first_digit,second_digit,temp = 0,1,0
fib = [0,1]

while count <= inp:
    temp = first_digit + second_digit
    first_digit = second_digit
    second_digit = temp
    fib.append(second_digit)
    count += 1
print(fib)


