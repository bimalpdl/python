"""
Syntax: 
[expression for item in iterable if condition]

    Expression: This is the value or operation to be applied to each item from the iterable.
    Item: Represents each element in the iterable (e.g., list, tuple, range, string, etc.).
    Iterable: The collection or sequence you're iterating over (e.g., list, range, string).
    Condition (Optional): A filtering condition that determines whether the current item will be included in the list. Only items that satisfy the condition are included.
"""
list1 = [x for x in range(21)]
print(list1)

list2 = [even for even in list1 if even % 2 ==0]
print(list2)

"""
List comprehensions can handle more complex tasks like generating a Cartesian product of two sets. For example, if you want to generate all pairs (i, j) where i is from 0 to 1 and j is from 0 to 2:"""
cartesian_product = [(i, j) for i in range(2) for j in range(3)]
print(cartesian_product)

"[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]"

# using function in list comprehension
def square(x):
    return x ** 2

squares = [square(x) for x in range(5)]
print(squares)



