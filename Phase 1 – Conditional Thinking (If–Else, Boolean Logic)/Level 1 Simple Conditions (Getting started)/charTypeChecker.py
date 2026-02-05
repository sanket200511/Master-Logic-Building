# Problem: charTypeChecker
inp = input("Enter a character: ")

if inp.isupper():
    print("It is in uppercase")
elif inp.islower():
    print("It is in lowercase")
elif inp.isdigit():
    print("It is a digit")
else:
    print("It is special character")