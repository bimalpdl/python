# TODO : add editing option for existing items.
import os, time 
os.system("clear")
def main():
    print("TODO app: ")
    time.sleep(1)
    items = []
    while True:
        choice = input("Add | Remove | View | Exit\n>")
        if choice == "Add" or choice == "add":
            add(items)
        elif choice == "Remove" or choice == "remove":
            remove(items)
        elif choice == "View" or choice == "view":
            view(items)
        elif choice == "Exit" or choice == "exit":
            exit()
        else:
            print("Invalid choice!")

def add(items):
    userInput = input("Enter your task:\n> ")
    if userInput in items:
        print(f"The item '{userInput}' is already in the list.")
    else:
        items.append(userInput)


def remove(items):
    if len(items) == 0:
        print("The list is already empty.")
    else: 
        delete = input("Delete an item(D) | Clear the list(C): ")
        if delete == "D" or delete == "d":
            print(f"Current items in the list are:\n{items}. Which one to delete?")
            delItem = input("> ")
            verify = input("Delete the item? (Y | N): ")
            if verify == "Y" or verify == "y":
                items.remove(delItem)
            
            else:
                print("Nothing deleted yet.")
            
        elif delete == "C" or delete == "c":
            verify = input("Clear the list ? (Y | N): ")
            if verify == "Y" or verify == "y":
                items.clear()
            else:
                print("Invalid choice..")
        else:
            print("Invalid choice...")


def view(items):
    if len(items) == 0:
        print("The list is empty.")
    else:
        print(items)
    
main()
