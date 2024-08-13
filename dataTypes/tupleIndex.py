# The index() method returns the index of the specified element in the tuple.
# and it returns ValueError exception if the element is not found in the tuple
tup1 = ('a', 'e', 'i','o', 'u' , 'i')
print(tup1)
print("The index of 'i' in given tuple is:", tup1.index('i'), "\n")
# note that the index() methos only returns the index of first element found in the tuple if same element is present multiple times
# in the example above, index of 'i' returned is 2 but not 5

# print("The index of 'b' in given tuple is:", tup1.index('b'))    // this will throw an error since 'b' isn't present in given tuple



# The index() method can take one to three parameters:
# index(element, start_index, end_index)
#     element - the item to scan
#     start_index (optional) - start scanning the element from the start_index
#     end_index (optional) - stop scanning the element at the end_index

tup2 = ('a', 'e', 'o', 'i', 'n', 'u', 'o', 'b')
print(tup2)
print("Index of 'e' in tup2 is", tup2.index('e'))
print(f"Index of second 'o' in given tuple is: {tup2.index('o',3,7)}")
