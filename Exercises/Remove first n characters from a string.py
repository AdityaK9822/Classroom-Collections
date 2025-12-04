String = input("Enter a string: ")
n = int(input("Enter no. characters to be removed: "))
if n<len(String):
    print(String[n:])
else:
    print("Invalid input")