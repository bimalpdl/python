details = {"Name" :"Rohini", "Age": 31, "Gender": "Female"}
for i in details:
    # prints both key and values
    print(f"{i} : {details[i]}")

print()
print(details)
print()
for value in details.values():    # use values() to get only value of the dictionary
    print(value)

print()
# to get both keys and values, we can use 'items()'
for key, value in details.items(): # we must declare two variables, one for key and another for value
    print(f"{key} : {value}")
