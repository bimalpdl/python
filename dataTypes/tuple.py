# tuple is similar to list in python,The primary difference is that we cannot modify a tuple once it is created.
# tuples are immutable
# We create a tuple by placing items inside parentheses ()
numbers = (1,"Two",3,4,5,"Six", True)
print(numbers)

# We can also create a tuple using a tuple() constructor.
names = tuple(("Rohini", "Nirmal", "Indira", "Om prasad"))
for i in names:    # iterate through a tuple
    print(i)

# empty tuple
emptyTuple = ()
print(emptyTuple)

# tuple can hold similar or mixed data types
#
# Tuples are:
#     Ordered - They maintain the order of elements.
#     Immutable - They cannot be changed after creation.
#     Allow duplicates - They can contain duplicate values.

#     tuples can be accessed using index number, starting from 0
print("Element at 0th index is:",names[0])


# Python tuples are immutable (unchangeable). We cannot add, change, or delete items of a tuple.
# If we try to modify a tuple, we will get an error.

# names[0] = "Matrika"     // this will throw an error]

# len() function is used to find the length of the tuple
print("Length of the tuple is:", len(names))


# We use the 'in' keyword to check if an item exists in the tuple
print("Is 'Bimal' present in names? ", "Bimal" in names)
print("Is 'Rohini' present in names? ", "Rohini" in names)

# We cannot delete individual items of a tuple. However, we can delete the tuple itself using the del statement.
print(names)
print("Deleting entire tuple is allowed.")
del names
# print(names)   // the tuple 'names'' in already deleted so can't print tuple 'names'

# to create a tuple with single element
name = ("Bimal")   # this will be treated as a string, to make it tuple, palce a comma(,) after the element
print("The type of name is", type(name))    # str
name1 = ("Bimal",)
print("Type of name1 is", type(name1))    # tuple

# a tuple can hold another tuple or list within tuple body
tup = (1,(2,3),[4,5])
print(tup,"\n")


# The count() method returns the number of times the specified element appears in the tuple.
# The count() method takes a single parameter

tup1 = ("Kathmandu", "Pokhara", "Bhaktapur", "Lalitpur", "Banke", "Kathmandu")
print(tup1)
print("Number of apperance of \"Kathmandu\" in given tuple is", tup1.count("Kathmandu"))
print("Number of apperance of \"Janakpur\" in given tuple is", tup1.count("Janakpur"),"\n")


# count() to Count List and Tuple Elements Inside Tuple
tup2 = (1, 2, ('a','b'), [3,4],('a','b') , 5, ('a','b'))
print("Elements in tup2", tup2)
print(f"The number of appearance of tuple ('a','b') in tup2 is, {tup2.count(('a','b'))}")
print(f"The number of appearance of list [3,4] in tup2 is, {tup2.count([3,4])} ")
