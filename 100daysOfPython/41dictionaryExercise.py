webDescription = {"name": None, "url": None, "description": None, "rating": None }   # starting with only keys, making all values none
for name, values in webDescription.items():
    # taking user input using keys
    webDescription[name] = input(f"{name}: ")
print()

for name, values in webDescription.items():
    # prints the keys and values
    print(f"{name}: {values}")
