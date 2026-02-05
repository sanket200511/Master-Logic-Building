# Problem: vowelConsonantChecker
inp = input("Enter a character: ").lower()
vowel = ("a" , "e" , "i" , "o " , "u")

if inp in vowel:
    print("It is vowel")
else:
    print("It is consonant")