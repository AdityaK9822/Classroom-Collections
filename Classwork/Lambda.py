square = lambda x: x * x
print(square(5))

nums = [1, 2, 3, 4]
result = list(map(square, nums))
print(result)

students = [("Alice", 85), ("Charlie", 92)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)