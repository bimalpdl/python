# We create a list by placing elements inside square brackets [], separated by commas.
# A list can hold elements with different data types
# list index starts with 0
items = ["Red", "Green", "Blue", True, 123, 12.5]
print("Items in the list are: ")
for item in items:
    print(item)

emptyList = []
print("This is empty list",emptyList)

# We can use the built-in list() function to convert other iterables (strings, dictionaries, tuples, etc.) to a list.
name = "Bimal"
print(list(name))  # converts the string to list of each character

"""
name = "Bimal"
result = list(name)
print(result)   // ['B', 'i', 'm', 'a', 'l']
"""

i = range(10,-1,-1)
print(list(i))    # converts the range elements to list


# Lists are:
#     Ordered - They maintain the order of elements.
#     Mutable - Items can be changed after creation.
#     Allow duplicates - They can contain duplicate values.

# we can use index to access the list elements, list index starts from 0
print(items[2])   # Blue from index 2 of list 'items'


# we can also use negative indexing to access the list elements, negetive index starts from -1
list2 = ["Acer", "Lenovo", "Xiaomi", "Disney"]
print(list[-1])   # prints the first element from back
print(list2[-3])   # Lenovo from negative index -3 (last element index is -1)

# use the append() method to add an element to the end of a Python list
print("Original list: ",list2)

# it is possible to access a section of items from the list using the slicing operator ( : )
list3 = ['B', 'I', 'M', 'A', 'L', 'I']
print(list3[2:5])   # prints item from index 2 to index 4
print(list3[2:])   # prints item from index 2 to end
print(list3[:])   # prints item from beginning to end
