import random, os, time
def calculteHealth():
    # function to calculate character health
    sixSided = random.randint(1,6)
    twelveSided = random.randint(1,12)
    print(f"Six sided: {sixSided}, TwelveSided: {twelveSided}")
    finalHealth = (sixSided * twelveSided)/2+10
    return finalHealth

def calculteStrength():
    # function to calculate character strength
    sixSided = random.randint(1,6)
    eightSided = random.randint(1,12)
    print(f"Six sided: {sixSided}, eightSided: {eightSided}")
    finalStrength = (sixSided * eightSided)/2+12
    return finalStrength
while True:
    print("Character Builder")
    name = input("Enter name of the character: ")
    print("Select character type:\n(Human, Elf, Wizard,Orc)")
    charType = input("> ")
    time.sleep(0.5)
    os.system("clear")
    print("Name of the character: ")
    health = calculteHealth()
    strength = calculteStrength()

    time.sleep(1.5)
    os.system("clear")
    print(f"Character name: {name}\nCharacter type: {charType} ")
    print(f"Health of the character is: {health}")
    print(f"Strength of the character is: {strength}")

    replay = input("Replay the game? ")
    if replay == "Yes" or replay == "yes":
        print("Lets replay the game!")
        continue
    elif replay == "No" or replay == "no":
        print("Good bye!")
        break
    else:
        print("Invalid input!")
        exit()
