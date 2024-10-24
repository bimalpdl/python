names = []
while True:
    name = input("Enter your full name: ").strip().title()
    if name not in names:
        names.append(name)
        print("Current list items are: \n",names)
    else:
        print(f"{name} already exists.")
