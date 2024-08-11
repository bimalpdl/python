 # break exits the loop entirely
 # continue skips the current iteration and proceeds to the next one
num = int(input("Enter a number: "))
print("Printing odd numbers less than {}".format(num))
for i in range(num):
    if i % 2 == 0:
        continue
    print(i)

print("The number less than 10 is: ".format(num))
for i in range(num):
    if i == 10:
        break
    print(i)
