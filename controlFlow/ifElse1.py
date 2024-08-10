# In certain situations, the if statement can be simplified into a single line.
number = int(input("Enter a number: "))
if number > 0: print("The number is greater than zero.")  # it is used when there's only one statement inside 'if' block.
else: ("The number is lesser than zero.")      #  but I think else statement doesn't work in this case.

# Python doesn't have a ternary operator.
# However, we can use if...else to work like a ternary operator in other languages

marks = int(input("Enter your marks: "))
result = 'Fail' if marks < 50 else 'Pass'
# result = if val <50 'Fail' else 'Pass'    // this won't work
print(result)
