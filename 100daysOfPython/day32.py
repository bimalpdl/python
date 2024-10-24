import random
greetings = ["Namaste", "Hello", "Hola", "Konnichiwa", "Guten Tag", "Bore Da"]
name = input("Enter your name: ")
choice = random.randint(0,5)
print("{}, How are you doing?\nHave a nice day!".format(greetings[choice]))
