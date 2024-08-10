# In Python, is and is not are used to check if two values are located at the same memory location.

# It's important to note that having two variables with equal values doesn't necessarily mean they are identical.
#
# is => True if the operands are identical (refer to the same object)
# is not => True if the operands are not identical (do not refer to the same object)
var1 = 18
var2 = 18
var3 = '18'
var4 = "Hello"
var5 = "Hello"
var6 = [1,2,3]
var7 = [1,2,3]
print("var1 is var2:",var1 is var2)      # returns true since var1 and var2 are of same data type and hold same value
print("var1 is var3:",var1 is var3)    # returns false; although var1 and var2 hold same value they are different data type
print("var1 is not var3:",var1 is not var3)    # returns true is data type of var1 and var3 are different

# 'is' is somehow similar to triple eqaulity operator (= = =) in JS/PHP i.e it checks for same value as well as same data type (it's not entirely true')

print("var4 is var5:",var4 is var5)   # prints True
print("var6 is var7:",var6 is var7)   # prints False
# var6 and var7 are lists. They are equal but not identical.
# It is because the interpreter locates them separately in memory, although they are equal.
print("var5 is not var6:",var5 is not var6)    # prints True
