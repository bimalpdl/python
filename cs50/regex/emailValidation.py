# simplest email validation
email: str = input("Enter your email: ").strip()
if "@" in email:
    print(f"Your email: {email} is valid.")
    print("It contains '@' sign.")
else:
    print(f"The email you entered: {email} is invalid!\nexpected'@'")
print()

# validate email for both @ and period(.)
if "@" in email and "." in email:
    print(f"{email} is valid and contains \"@\" and \".\" .")
else:
    print(f"The email you entered: {email} is invalid!")
    print("'@' and '.' both expected.")
print()


# separates username and domain name then performs validation.
try:
    userName, domainName = email.split("@")
    if userName and "." in domainName:
        print(f"Username: {userName}\nDomain name: {domainName}")
    else:
        print("Either invalid username or invalid domain name.")
except:
    print("Can't determine username and domain name, '@' is expected.")
# error handling works at least for this block of code, other blocks may throw error
print()


# check whether the email endswith '.com'
if userName and domainName.endswith(".com"):
    print(f"{email} ends with '.com'.")
else:
    print(f".com is expected at the end.")

