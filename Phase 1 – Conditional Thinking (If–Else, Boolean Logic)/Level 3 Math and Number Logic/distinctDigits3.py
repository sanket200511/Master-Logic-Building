# Problem: distinctDigits3
'''
inp = str(input("Enter a three digit number: "))

if inp[0] == inp[1] or inp[0] == inp[2] or inp[1] == inp[2]:
    print("All three digits are not distinct")
else:
    print("All three digits are distinct")

'''

inp = int(input("Enter a three digit number: "))

first_num = second_num = third_num = 0

third_num = inp % 10
inp //= 10
second_num = inp % 10
inp //= 10
first_num = inp % 10
inp //= 10

if first_num == second_num or first_num == third_num or second_num == third_num:
    print("All three digits are not distinct")
else:
    print("All three digits are distinct")