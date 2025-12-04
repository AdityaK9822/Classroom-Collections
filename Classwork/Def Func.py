print("1:")
def greet(name):
    print("Hello",name)
    
greet("Aditya")

print("2:")
def add(a,b):
    return a+b
result = add(5,10)

print(result)

print("3:")
x = 5#global variable
def func():
    x = 10#local variable
    print(x)
func()

print(x)

a = 10
b = 3.0
print(type(a))
print(type(b))
print(type(a/b))