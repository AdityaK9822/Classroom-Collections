# Mini Project - Student Report Card

# taking inputs
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# calculations
total = maths + science + english
average = round(total / 3, 2)
# result condition (change 40 if your pass marks are different)
if average >= 35:
    result = "PASS"
else:
    result = "FAIL"

# printing report card
print("----- Student Report Card -----")
print("Name   : ", name)
print("Roll No: ", roll_no)
print("Total  : ", total)
print("Average: ", average)
print("Result : ", result)
print("--------------------------------")