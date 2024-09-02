# A Python dictionary is a collection of items, similar to lists and tuples.
# However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).
# We create a dictionary by placing key: value pairs inside curly brackets {}, separated by commas. For example,
countryCapitals = {    # v
    "Nepal" : "Kathmandu",
    "India" : "New Delhi",
    "Japan" : "Tokyo",
    "USA" : "Washing ton",
    "Bangladesh" : "Dhaka",
 }

#    We can also create a dictionary using a Python built-in function dict()
print(countryCapitals)
print()
# We can access the value of aA dictionary item by placing the key inside square brackets.
print("Capital of Nepal is:", countryCapitals["Nepal"])
print("Capital of Japan is: ", countryCapitals["Japan"])


# Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys.
dict1 = {1 : "One", "Twoo": "Two", (1,2) : "One and Two"}      # integer, string and tupes as key
print(dict1)

# Dictionary value can have any data type
dict2 = {1: "Bimal", "Address" : "Kandaghari" , ("NTC", "NCELL") : [ 9843, 98032]}
print(dict2)

# Dictionary values are mutable data types, key is used to specify the changing value
dict2["Address"] = "Thapa Chok"
print(dict2)

# adding items to the dictionary
# We can add an item to a dictionary by assigning a value to a new key
dict2["Age"] = 22


# Iterating through dictionary
# accessing keys of dictionary using for loop
for keys in dict2:
    print(keys, end = " ")
print()

# accessing values using for loop
for values in dict2:
    print(dict2[values], end=" ")
print()

# to access both keys and values
for key in dict2:
    print(key, ":", dict2[key], end= " ")
print()


# len() function is used to find the length of the dictionary
print("Length of dict2 is: ",len(dict2))


# We can use the del statement to remove an element from a dictionary.
del dict2["Age"]
print("After one deletion, the lenght is:", len(dict2))

print(dict2)

# If we need to remove all items from a dictionary at once, we can use the clear() method??
dict2.clear()
print(dict2)

print()
# We can check whether a key exists in a dictionary by using the in and not in operators
dict3 = {"fname" : "Bimal", "Age" : 22, "Address" : "Kandaghari", "Sex" : "Male"}
print("Items in dict3:",dict3)
print("Is fname present in dict3?", "fname" in dict3)
print("Is lname present in dict3?", "lname" in dict3)
