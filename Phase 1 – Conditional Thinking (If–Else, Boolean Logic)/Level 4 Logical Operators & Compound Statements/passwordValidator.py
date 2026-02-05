# Problem: passwordValidator
from re import search

password = input("Enter a password: ")

if not search(r"[A-Z]",password):
    print("Password Must contains at least 1 uppercase")
if not search(r"[a-z]",password):
    print("Password Must contains at least 1 lowercase")
if not search(r"[!@#$%^&*(),.?\":{}|<>]",password):
    print("Password Must contains at least 1 special characters")
if not search(r"\d",password):
    print("Password Must contains at least 1 digit")

