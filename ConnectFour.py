import random

def intro():
    print("\n-----CONNECT FOUR-----")
    print("Get 4 in a row against the computer.\n")

def printBoard():
    print("\033[1m" + "-CONNECT FOUR-" + "\033[0m")
    for row in board:
        print(" ".join(row))

    axisList = [1, 2, 3, 4, 5, 6, 7]
    for num in axisList:
        print( "\033[1m" + str(num) +"\033[0m", end = " ")

def game():
    playing = True

    while playing == True:
        userSpaceValidation = False
        while userSpaceValidation == False:
            columnCheck = False
            while columnCheck == False:
                userColumn = int(input("\n\nWhat column would you like to choose? ")) - 1

                columnCount = 0
                for row in range(rows):
                    if board[row][userColumn] == "X" or board[row][userColumn] == "O":
                        columnCount += 1

                # Checks if column is out of the board's range\
                outOfRange = False
                if userColumn > (columns - 1) or userColumn < 0:
                    print("Column out of range (1 - 7)\n")
                    outOfRange = True

                # Checks to see if column is filled
                filled = False
                if columnCount == rows:
                    print("The column is completely filled\n")
                    filled = True

                if filled == False and outOfRange == False:
                    columnCheck = True
               
            board[(rows - 1) - columnCount][userColumn] = "X"
            print("You chose column " + str(userColumn + 1) + "\n")
            printBoard()
            userSpaceValidation = True
        
        # Horizontal User Win
        for row in range(rows):
            for column in range(columns - 3):
                if board[row][column] == "X" and board[row][column + 1] == "X" and board[row][column + 2] == "X" and board[row][column + 3] == "X":
                    playing = False
                    print("After Game" + str(userWins))
                    print("\n\nCongratulations! You Win!\n")

        # Vertical User Win
        for row in range(rows - 3):
            for column in range(columns):
                if board[row][column] == "X" and board[row + 1][column] == "X" and board[row + 2][column] == "X" and board[row + 3][column] == "X":
                    playing = False
                    print("\n\nCongratulations! You Win!\n")                    

        # Tie Game
        dashCounter = 0
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "-":
                    dashCounter += 1

        if dashCounter == 0:
            playing = False
            print("\nTie Game! Nobody Wins!\n")

        # Computer's Move
        if playing == True:
            computerSpaceValidation = False
            while computerSpaceValidation == False:
                if userColumn == 0:
                    computerColumn = random.randint(userColumn, (userColumn + 1))
                elif userColumn == (columns - 1):
                    computerColumn = random.randint((userColumn - 1), userColumn)
                else:
                    computerColumn = random.randint((userColumn - 1), (userColumn + 1))
                
                computerColumnCount = 0
                for row in range(rows):
                    if board[row][computerColumn] == "X" or board[row][computerColumn] == "O":
                        computerColumnCount += 1

                # Checks to see if column is filled
                if computerColumnCount == rows:
                    print("The column is completely filled\n")
                
                else:
                    board[(rows - 1) - computerColumnCount][computerColumn] = "O"
                    print("\nThe computer chose column " + str(computerColumn + 1) + "\n")
                    printBoard()
                    computerSpaceValidation = True

        # Horizontal Computer Win
        for row in range(rows):
            for column in range(columns - 3):
                if board[row][column] == "O" and board[row][column + 1] == "O" and board[row][column + 2] == "O" and board[row][column + 3] == "O":
                    playing = False
                    print("\n\nGame Over! You Lose!\n")

        # Vertical Computer Win
        for row in range(rows - 3):
            for column in range(columns):
                if board[row][column] == "O" and board[row + 1][column] == "O" and board[row + 2][column] == "O" and board[row + 3][column] == "O":
                    playing = False
                    print("\n\nGame Over! You Lose!\n")

def sessionSummary():
    winPercentage = (userWins / gamesPlayed)
    lossPercentage = (userLosses / gamesPlayed)
    tiePercentage = (ties / gamesPlayed)
    print("\n\n*****Session Summary*****")
    print("Games Played: " + str(gamesPlayed))
    print("Wins: " + str(userWins) + " (" + str(winPercentage) + "%)")
    print("Losses: " + str(userLosses) + " (" + str(lossPercentage) + "%)")
    print("Ties: " + str(ties) + " (" + str(tiePercentage) + "%)")

active1 = True

gamesPlayed = 0
userWins = 0
userLosses = 0
ties = 0

while active1 == True:
    board = []
    rows = 6
    columns = 7
    for i in range(rows):
        board.append(["-"] * columns)

    intro()
    printBoard()
    game()
    gamesPlayed += 11
    #sessionSummary()
    
    active2 = True
    while active2 == True:
        choice = input("\n Do you want to play again? (yes/no): ")
        print("")
        if choice == "yes":
            active2 = False
        elif choice == "no":
            print("Goodbye")
            active2 = False
            active1 = False
        else:
            print("That is not a valid input")