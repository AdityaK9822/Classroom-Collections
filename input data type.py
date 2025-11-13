variable=input("Enter a something:")
if variable.isdigit():
    print("You have entered a number")
elif variable.isalpha():
    print("You have entered a string")
elif variable.isalnum():
    print("You have entered a alphanumeric")
else:
    print("You have entered a special character")
