dynamicList = []
while True:
    choice = input("Add or Remove?: ")
    if choice == "add" or choice == "Add":
        item = input("Enter item to add: ")
        dynamicList.append(item)
        print("Current items in the list are: ", dynamicList)

    elif choice == "remove" or choice == "Remove":
        print("Items in the list are: ", dynamicList)
        item = input("Enter item to remove: ")
        if item in dynamicList:    # to ensure the removing element exist at the first place.
            dynamicList.remove(item)    # remove() can remove only one item at a time.
        else:
            print(f"{item} is not in the list.")
        print("Current items in the list are: ", dynamicList)

