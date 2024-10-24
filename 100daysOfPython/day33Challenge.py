def main():
    toDo = []
    while True:
        choice = input("Add | View | Remove ?: ")
        if choice == "add" or choice =="Add":
            add(toDo)
        elif choice == "remove" or choice == "Remove":
            Remove(toDo)
        elif choice == "view" or choice == "View":
            view(toDo)



def add(toDo):
    item = input("Enter item to add: ")
    toDo.append(item)

def Remove(toDo):
    item = input("Ente item to remove: ")
    if item in toDo:      # checks if the item is present in the given list.
        toDo.remove(item)
    else:
        print("{} isn't in the list.".format(item))
    


def view(toDo):
    if len(toDo) == 0:    # checks whether the list is empty.
        print("The list is empty!")
    else:
        print(f"Items in the TODO list are: \n{toDo}")

main()
