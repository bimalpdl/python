# Python Set provides different built-in methods to perform mathematical
# set operations like union() or | , intersection() or & , subtraction or - , and symmetric difference or ^ , = =.

# We use the | operator or the union() method to perform the set union operation.
set1 = {1, 2, 3, 4,5}
set2 = {4, 5, 6, 7}
print("Elements in set1:", set1)
print("Elements in set2:", set2)
print(f"Union using pipe | : {set1 | set2}")
print(f"Union using union() method : {set1.union(set2)}\n")

# use the '&' operator or the intersection() method to perform the set intersection operation.
print("Intersection using ampersand '&' :", set1 & set2)
print("Intersection using intersection() :", set1.intersection(set2),"\n")

# The difference between two sets A and B include elements of set A that are not present on set B.
# use the - operator or the difference() method to perform the difference between two sets.
print("Difference using '-' :", set1 - set2)
print("Difference using difference() :", set1.difference(set2),"\n")


# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
# we use the ^ operator or the symmetric_difference() method to perform symmetric differences between two sets.
print("Symmetric difference using '^' :", set1 ^ set2)
print("Symmetric difference using symmetric_difference() :", set1.symmetric_difference(set2),"\n")

# use the (= =) operator to check whether two sets are equal or not
set3 = {"Bimal", "Paudel", True}
set4 = {"Bimal", "Paudel", True}

print("Elements in set3:", set3)
print("Elements in set4:", set4)
print("Set3 and set4 are equal.\n" if set3 == set4 else "Set3 and set4 are not equal.\n")


print("Elements in set1:", set1)
print("Elements in set2:", set2)
if set1 == set2:
    print("Set1 and set2 are equal.")
else:
    print("Set1 and set2 are not equal.")
