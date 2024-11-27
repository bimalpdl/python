print("Welcome to MokeBeast")
details = {"name": None, "type": None, "move": None, "hp": None, "mp": None}
for name, value in details.items():
    details[name] = input(f"{name}: ")
print()

# changes the output text color
if details["type"] == "fire":
    print("\033[31m", end="")
elif details["type"] == "water":
    print("\033[34m", end = "")
elif details["type"]  == "air":
    print("\033[37m", end = "")
elif details["type"] == "earth":
    print("\033[32m", end = "")
else:
    print("\033[37m", end = "")

# display the character details 
for name, value in details.items():
    print(f"{name:^15} : {value}")

