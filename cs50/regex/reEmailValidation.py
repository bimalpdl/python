# built-in library're' has a number of built-in functions that can validate user inputs against patterns (used to check regular expressions).
""" One of the most versatile functions within the library re is search.
The search library follows the signature re.search(pattern, string, flags=0). Following this signature, we can modify our code as follows: """

"""

.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string

Note:
    if you user ^ inside [] it means "anything except .." it nolonger matches start of string.
    eg: [^@]  ==> anything except '@'

[]    set of characters
[^]   complementing the set (excluing)

"""
import re
email = input("Enter your email: ").strip()
if re.search(r"^.+@.+\.edu$", email):  # here, email is the string defined above
    # Placing an r in front of a string tells the Python interpreter to treat the string as a raw string
    # it is good practice to use 'r' flag as we used above when dealing with regular expressions
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid")
