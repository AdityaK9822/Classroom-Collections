from turtle import clear


a=["1","2","3","4","5","6","7","8","9"]
print(a[-4:])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

t = ("a","b","c","d","e")
(*x,y,z) = t
print(*x)

t = ("a","b","c","d","e")
(x,*y,z) = t
print(*y)

t = ("a","b","c","d","e")
(xaw,y,*z) = t
print(*z)