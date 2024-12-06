import random
numbers = []
for i in range(9):
    number = random.randint(1,90)
    numbers.append(number)

for i in numbers:
    print(f"{i}", end = " ")

numbers.sort()
print()
for j in numbers:
    print(f"{j}", end = " ")
print()
print()
bingo = [ [numbers[0], numbers[1], numbers[2]],
         [numbers[3], "Bimal", numbers[4]],
         [numbers[5], numbers[6], numbers[7]]
        ]

for i in range(3):
    for j in range(3):
        print(f"{bingo[i][j]} ", end = " ")
    print()
