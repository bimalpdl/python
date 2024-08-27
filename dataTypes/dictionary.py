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

# Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys.
#    We can also create a dictionary using a Python built-in function dict()
print(countryCapitals)
print()
# We can access the value of aA dictionary item by placing the key inside square brackets.
print("Capital of Nepal is:", countryCapitals["Nepal"])
print("Capital of Japan is: ", countryCapitals["Japan"])
