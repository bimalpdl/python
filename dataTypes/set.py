# set is collection of unique data i.e it can't hold duplicate data
# set is defined inside {}, it can hold different datatypes like, int, float, str, tuple etc
# but a set cannot have mutable elements like lists, sets or dictionaries as its elements.
# sets are mutable, means we can change/update/delete even after set declaration.
# Un-ordered - set doesn't maintain the order of elements.

set1 = {1, 2, 3, 4, 5, 6, 7}
print("Numbers in set1 are: {}".format(set1))

set2 = {"Bimal", "Rohini", True, 123, 34.56, (2,3)}
for i in set2:
    print(i)
print("Elements in set2 are:", set2)

# When you run this code, you might get output in a different order. This is because the set has no particular order.

# empty set
# Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python
# To make a set without any elements, we use the set() function without any argument.

var = {}
var1 = set()
print(f"Type of var is: {type(var)}")
print(f"Type of var1 is: {type(var1)}")

# even if we dare to add duplicate element in the set, it'll only stores it once.
set3 = {1, 2, 3, 1, 4, 5,2}
print("Elements in set3 are:",set3)   # prints {1, 2, 3, 4, 5}

# use min() method to find smallest item from the list
print("Mininum element in set3 is,",min(set3))
# use max() method to find largest item from the list
print("Mixnimum element in set3 is,",max(set3))


# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. The set data type does not support it.

# add() method is used to add element to a set

set4 = {"Bimal", "Rohini", "Nirmal"}
print("Original elements in set4 are:", set4)
set4.add("Matrika")
print("After adding an element,", set4)


# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc)
cities = {"Kathmandu", "Pokhara", "Butwal"}
cities1 = ["Bhaktapur", "Patan", "Bhaktapur"]
print(f"Elements in set cities: {cities}")
print(f"Elements in list cities1: {cities1}")
cities.update(cities1)     # note that duplicate entries in list are ignored
print(f"After performing cities.update(cities1):, {cities}")

# discard() method is used to remove the specified item from the set
cities.discard("Kathmandu")
print("Cities, after deleting kathmandu:", cities)

# len() method is used to findout the number of elements in the set
print(f"Length of set cities is:", len(cities))
