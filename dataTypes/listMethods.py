# commonly used list methods: append(), extend(), remove(), del, sort(), len(), pop(), reverse(), clear()
# use the append() method to add an element to the end of a Python list
list1 = ["Acer", "Lenovo", "HP", "Dell", "Xiaomi"]
print("Items in the original list are:",list1)
list1.append("Thinkpad")
print("Items appendin an item:", list1, "\n")



# The insert() method adds an element at the specified index
list1.insert(1,"Nitro")   # the previous element in index 1 and other elements after index1 are shifted right by 1 index position
print("List after inserting'Nitro' at index 1", list1,"\n")

# the extend() method is used to add elements of one list to another
list2 = [1, 2, 3, 4, 5]
list3 = [6,7,8]
print("Elements in original list:", list2)
print("Elements in second list:", list3)
list2.extend(list3)    # adds elements of list3 to list2
print("The extended list:", list2,"\n")

# We can change the items of a list by assigning new values using the = operator
print("Items in original list:",list1)
list1[0] = "Nokia"    # updates the value in index 0
print("Items in the list after changing the element of index 0:", list1, "\n")

# We can remove an item from a list using the remove() method, it removes the element by its name, not by index
list1.remove("Nokia")    # used to remove only one element from the list
print("List elements after removing 'NOkia'.", list1,"\n")

# del statement is used to delete one or more elements from the list, uses undex number to delete the element

list4 = ["Kathmandu", "Pokhara", "Butwal", "Narayangadh", "Muglin", "Chitwan","Bharatpur"]
print("Elements in original list:", list4)
del list4[2]  # deleltes the element in index 2
print("After deleting the element in index 2:", list4)

# to delete multiple elements from the list:
del list4[2:6]   # deletes the element from index 2 to index 5
print("After deleting the elements from index 2 to index 5:", list4,"\n")

del list4[:]   # deletes all elements from the list
# the above line can be written as, simply 'del list4'
print("After deleing all elements:", list4)


list5 = ["Kantipur", "Bhaktapur", "Lalitpur", "Patan", "Basantapur"]
# we can use len() method to find the length of the list:
print("The length of the list5 is:",len(list5))

# use a for loop to iterate over the elements of a list
print("Elements in list5 are: ")
for i in list5:
    print(i)

# pop() method is used to delete the last element from the list
list5.pop()
print("After performing 1 pop() operation:", list5,"\n")

# reverse() method is used to reverse the elements of the list
list5.reverse()
print("After reversing the list:", list5)

# sort() method is used to sort the element in the list, by default it sorts in ascending order
list5.sort()
print("After sort operation:",list5)

# to perform sort() in descenging order, use sort(reverse=True)
list5.sort(reverse=True)
print("Afte performing sort in descending order:", list5)


# clear() removes all elements form the list
list5.clear()
print("After applying clear() method on list5:", list5)
