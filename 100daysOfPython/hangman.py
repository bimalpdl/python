import random
names = ["tom", "jerry", "bob", "oggy"]

word = random.choice(names)
pickedLetters = []
score = 10

while True:
    letter = input("Enter a letter: ").lower()
    if letter in pickedLetters:
        print(f"{letter} is already in the list.")
        continue

    pickedLetters.append(letter)

    if letter in word:
        print("You found a letter!")
    else:
        print("Nope, you missed.")
        score -= 1
        print(f"You have {score} lives left.")

    allFound = True
    print()
    for i in word:
        if i in pickedLetters:
            print(i, end="")
        else:
            print("_", end = "")
            allFound = False
    print()

    if allFound:
        print(f"You won with score {score}\nThe word was {word}")
        break
    else:
        print(f"You lose, the word was {word}")
        break


