import os, time 
for i in range(5):
    print(i)
    time.sleep(0.2)  # sleeps for specified time in seconds
    os.system("clear")    # clears the console

print("Hello there, how are you doing today? Hope you're doing well.")
time.sleep(0.8)
userName = input("Please enter your username to login: ")
passwd = input("Please enter your password: ")
if (userName == "Bimal" or userName == "bimal") and passwd == "hello$123":
    os.system("clear")
    print("Hello, Bimal ! Welcome to the most useless login system.")
else:
    print("Who the hell are you? Get lost !")


