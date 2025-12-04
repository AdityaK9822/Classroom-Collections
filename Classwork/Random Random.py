import random
print(random.random())
print(random.randint(1,10))
print(random.choice(["Apple","Cherry","Banana"]))
print(random.choice([1,2,3,4,5]))
print(random.sample(range(100), 5))

cards = ['A', 'B', 'C', 'D', 'E']
print("Original:", cards)
random.shuffle(cards)
print("Shuffled:", cards)
print("Sample:", random.sample(cards, 3))