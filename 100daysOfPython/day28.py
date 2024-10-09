import random, os, time
def calculteHealth():
    # function to calculate character health
    sixSided = random.randint(1,6)
    twelveSided = random.randint(1,12)
    finalHealth = (sixSided * twelveSided)/2+10
    return finalHealth

def calculteStrength():
    # function to calculate character strength
    sixSided = random.randint(1,6)
    eightSided = random.randint(1,12)
    finalStrength = (sixSided * eightSided)/2+12
    return finalStrength
        
def replay1( param = "yes" ):
    replay = input("Replay the round? ")
    if replay == "yes" or replay == "Yes" or replay =="y":
        return True
    else:
        return False
while True:
    print("Character Builder")
    name = input("Enter name of the character: ")
    print("Select character type:\n(Human, Elf, Wizard,Orc)")
    charType = input("> ")
    time.sleep(0.2)
    os.system("clear")
    health = calculteHealth()
    strength = calculteStrength()

    time.sleep(0.2)
    os.system("clear")

    print("Opponent character")
    name1 = input("Enter name of the character: ")
    print("Select character type:\n(Human, Elf, Wizard,Orc)")
    charType1 = input("> ")
    time.sleep(0.2)
    os.system("clear")
    health1 = calculteHealth()
    strength1 = calculteStrength()


    os.system("clear")

    print(f"Character name: {name}\nCharacter type: {charType} ")
    print(f"Health of the character is: {health}")
    print(f"Strength of the character is: {strength}")
    
    print()

    print(f"Character name: {name1}\nCharacter type: {charType1} ")
    print(f"Health of the character is: {health1}")
    print(f"Strength of the character is: {strength1}")
    
    while True:
        diff = abs(strength1 - strength)
        if health1 > 0 and health > 0:
          if strength > strength1:
            print("\n")
            print(f"{name} won the round!")
            print()
            health1 -= diff
            print(f"Character name: {name}")
            print(f"Health of the character is: {health}")
            print(f"Strength of the character is: {strength}")
            print()

            print(f"Character name: {name1}")
            print(f"Health of the character is: {health1}")
            print(f"Strength of the character is: {strength1}")
            print()


            if replay1():
                strength = calculteStrength()
                strength1 =calculteStrength()
            else:
                break
          elif strength1 > strength:
            print("\n")
            print(f"{name1} won the round!")
            print()
            health -+ diff
            print(f"Character name: {name1} ")
            print(f"Health of the character is: {health1}")
            print(f"Strength of the character is: {strength1}")
            print()
            
            print(f"Character name: {name}")
            print(f"Health of the character is: {health}")
            print(f"Strength of the character is: {strength}")
            print()


            if replay1():
                strength = calculteStrength()
                strength1 = calculteStrength()
            else:
                break

          else:
            print("Draw game!")
            break
        else:
            if health1 > health:
                print(f"{name1} won the game!")
                break
            elif health > health1:
                print(f"{name} won the game!")
                break
            else:
                print("Draw game!")
                break

    replay = input("Replay the game? ")
    if replay == "Yes" or replay == "yes" or replay == "y":
        print("Lets replay the game!")
        os.system("clear")
        continue
    elif replay == "No" or replay == "no" or replay =="n":
        print("Good bye!")
        break
    else:
        print("Invalid input!")
        exit()
