var = "Hello, Duniya"
dict1 = {"Hello":"Duniya", 1: "Bimal", "isStudent": True}

print("H in var:", "H" in var)    # checks if 'H' is present in variable var;  => prints True
print("Hello in var:", "Hello" in var)   # prints True
print("hello in var:", "hello" in var)   # 'hello' with lowercase 'h' isn't present in given variable; prints False

# in searches for the given element in the key; not in the value
print("Hello in dict1:", "Hello" in dict1)   # prints True since "Hello is present as key in dict1 "
print("Duniya in dict1:", "Duniya" in dict1)  # prints False since there no "Duniya" in as key in given dictionary 'dict1'

print("isStudent in dict1:", "isStudent" in dict1)

print("1 not in dict1:", 1 not in dict1)    # false sice 1 is present as key in given dict1
