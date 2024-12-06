userInput = True
while userInput == True:
    from getpass import getpass as input
    player1 = input("Enter the choice for playr1 R | P | S : ")
    player2 = input("Enter the choice for player2 R | P | S : ")
    if player1 == "R" or player1 == "r":
        if player2 == "R" or player1 == "r":
            print("You both choose rock so draw!")
        elif player2 == "P" or player2 =="p":
            print("Player1 was rock and player2 was paper so player2 won!")
        elif player2 == "S" or player2 == "s":
            print("Player1 was rock and player2 was scissors so player player1 won!")
        else:
            print("Invalid Input!")
    elif player1 == "P" or player1 == "p":
        if player2 == "P" or player2 == "p":
            print("You both choose Paper so draw!")
        elif player2 == "R" or player2 =="r":
            print("Player1 was paper and player2 was rock so player1 won!")
        elif player2 == "S" or player2 == "s":
            print("Player1 was paper and player2 was scissors so player player2 won!")
        else:
            print("Invalid choice!")
    elif player1 == "S" or player1 == "s":
        if player2 == "S" or player2 == "s":
            print("You both choose scissors so draw!")
        elif player2 == "R" or player2 == "r":
            print("Player1 was scissors and player2 was rock so player2 won!")
        elif player2 == "P" or player2 == "p":
            print("Player1 was scissors and player2 was paper so player player1 won!")
    else:
        print("Invalid input!")


    userInput1 = input("Enter R to replay the gama and enter Q to quit the game: ")
    if userInput1 == "R" or userInput1 == "r":
      print("You chose the replay the game !")
      print()
      userInput = True
    elif userInput1 == "Q" or userInput1 == "q":
      print("Good Bye!")
      userInput = False
    else:
        print("Invalid input!!")
        exit()
 

