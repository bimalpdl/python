text = f"""Hello


This is some random text

that i want to store in the file.. Is it possible? Lets find out!

PS:Its actually possible to store text like this!! 

"""
with open("dummyFile", "a") as file:
    file.write(text)

with open("dummyFile", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
