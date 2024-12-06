import random
numbers = []
for i in range(5):
    number = random.randint(0,100)
    numbers.append(number)

numbers.sort()
print(numbers)
