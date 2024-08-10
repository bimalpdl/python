# In Python, we use a for loop to iterate over sequences such as lists, strings, dictionaries, etc.
# we use indentation to define a block of code, such as the body of a loop.

# for through a list
names = ["Bimal", "Rohini", "Nirmal", "Bishwaksen"]    # list has 4 elements, the loop iterates 4 times.
for name in names:
    print(name)
    print(f"Hello {name}, how are you?")

# The for loop iterates over the elements of sequence in order. In each iteration, the body of the loop is executed.
# The loop ends after the last item in the sequence is reached.
# syntax=> for val in Sequence:

# loop through a string
word = "Bimali"
count = 0
for i in word:    # iterate over each character in language; the 'Bimali' has 8 characters so iterates 6 times
    print(i, end = " ")
print()

for i in word:    # the word 'Bimali' contains 6 charaters so iterates 6 times (starting from 0)
    print(count, end = " ")  # we can do whatever we want (not just printing the charaters of the given word/str)
    count += 1
print()

# the range() function returns a sequence of numbers.
for i in range(5):    # iterates from i = 0 to i = 4
    print("{}. Hello, World!".format(i))


# A for loop can have an optional else clause.
# This else clause executes after the iteration completes.
values = [10, 15, 16]
for value in values:
    print(value, end = " ")
# The else block will not execute if the for loop is stopped by a break statement.
else:
    print()
    print("Hello, There!")   #When the loop finishes, it executes the else block and prints 'Hello, There!'


# Using for loop without accessing items
count = 1
colors = ["Red", "Green", "Blue", "Navy"]   # 4 items in the list so iterates 4 times ( starts from 0 to 3)
for color in colors:
    print(f"{count}. Hello, Duniya!")    # we aren't accessing any items from the list
    count += 1
print()



# nested for loop:
for i in range(3):
    for j in range(3):
        print(f"(x = {i},y = {j})")
    print()
print()
