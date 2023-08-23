import random

def intro():
    print("---BATTLESHIP---\n")

def printBoard():
    for row in board:
        print(" ".join(row))

def game():
    printBoard()
    guesses = 10
    print("\nGUESSES LEFT: " +  str(guesses))
    # Computer coordinates for the battleship
    computerRow = random.randint(1, 8) - 1
    computerColumn = random.randint(1, 8) - 1
    print(computerRow, computerColumn)
    playing = True
    while playing == True:
        userSpaceValidation = False
        while userSpaceValidation == False:

            rowValidation = False
            while rowValidation == False:
                # Get User Row Guess
                guessRow = int(input("\nWhich row do you guess? ")) - 1
                if guessRow > rows - 1 or guessRow < 0:
                    print("Out of Range")
                else:
                    rowValidation = True

            columnValidation = False
            while columnValidation == False:
                # Get User Column Guess
                guessColumn = int(input("Which column do you guess? ")) - 1
                if guessColumn > columns - 1 or guessColumn < 0:
                    print("Out of Range")
                else:
                    columnValidation = True

            if board[guessRow][guessColumn] == "X":
                print("That space is already taken\n")
            else:
                board[guessRow][guessColumn] = "X"
                print("")
                printBoard()
                guesses -= 1
                print("\nGUESSES LEFT: " + str(guesses))
                userSpaceValidation = True

        if ((guessRow) == computerRow) and ((guessColumn) == computerColumn):
            print("You Win!")
            playing = False
        if guesses == 0:
            print("Game Over! You Lose!")
            print("\n Answer:\n ROW: " + str((computerRow + 1)) + " COLUMN: " + str((computerColumn + 1)))
            playing = False


active1 = True 
while active1 == True:
    board = []
    rows = 8
    columns = 8
    for i in range(rows):
        board.append(["O"] * columns)
    
    intro()
    game()
    active2 = True
    while active2 == True:
        choice = input("\nDo you want to play again? (yes/no): ")
        print("")
        if choice == "yes":
            active2 = False
        elif choice == "no":
            print("Goodbye")
            active2 = False
            active1 = False
        else:
            print("That is not a valid input")