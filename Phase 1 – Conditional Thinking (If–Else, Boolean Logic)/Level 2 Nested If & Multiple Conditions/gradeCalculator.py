# Problem: gradeCalculator
marks = int(input("Enter your marks: "))

if 1 <= marks <= 40:
    grade = "F"
elif 41 <= marks <= 60:
    grade = "D"
elif 61 <= marks <= 80:
    grade = "C"
elif 81 <= marks <= 90:
    grade = "B"
elif 91 <= marks <= 100:
    grade = "A"
else:
    grade = "Invalid marks"

print("Your grade is:", grade)
