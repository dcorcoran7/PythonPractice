import random

def intro():
    print("-----TIC TAC TOE-----")
    print("Get 3 in a row against the computer\n")

def printBoard():
    for row in board:
        print(" ".join(row))

def game():
    playing = True
    while playing == True:
        userSpaceValidation = False
        while userSpaceValidation == False:
            # Checks if the column is out of the board's range
            # Player column input
            columnCheck = False
            while columnCheck == False:
                playerColumn = int(input("\nWhich column would you like to play? ")) - 1
                if playerColumn > (columns - 1) or playerColumn < 0:
                    print("That column does not exist\n")
                else:
                    columnCheck = True

            # Checks if the row is out of the board's range
            # Player row input
            rowCheck = False
            while rowCheck == False:
                playerRow = int(input("Which row would you like to play? ")) - 1
                if playerRow > (rows - 1) or playerRow < 0:
                    print("That row does not exist\n")
                else:
                    rowCheck = True

            # Checks if space is taken by an X or a O
            if board[playerRow][playerColumn] != "-":
                print("Sorry, that space is taken. Choose another space\n")
            # Places an X on the user defined space
            else:
                board[playerRow][playerColumn] = "X"
                userSpaceValidation = True
                print("")

        # Horizontal User Win
        for row in range(rows):
            column = 0
            if board[row][column] == "X" and board[row][column + 1] == "X" and board[row][column + 2] == "X":
                playing = False
                print("\nCongratulations! You Win!\n")
                printBoard()

        # Vertical User Win
        for column in range(columns):
            row = 0
            if board[row][column] == "X" and board[row + 1][column] == "X" and board[row + 2][column] == "X":
                playing = False
                print("\nCongratulations! You Win!\n")
                printBoard()

        # Diagonal User Win
        count1 = 0
        count2 = 0
        for row in range(rows):
            if board[row][row] == "X":
                count1 += 1
            if board[row][(rows - 1) - row] == "X":
                count2 += 1
            if count1 == 3 or count2 == 3:
                playing == False
                print("\nCongratulations! You Win!\n")
                printBoard()
        
        # Tie Game
        dashCounter = 0
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "-":
                    dashCounter += 1

        if dashCounter == 0:
            playing = False
            print("\nTie Game! Nobody Wins!\n")
            printBoard()

        # Computer's move
        computerSpaceValidation = False
        while computerSpaceValidation == False:
            computerRow = random.randint(0, 2)
            computerColumn = random.randint(0, 2)
            # Checks if space is taken by an X or a O
            if board[computerRow][computerColumn] != "-":
                pass
            # Places an O on the computer defined space and prints the new board
            else:
                board[computerRow][computerColumn] = "O"
                computerSpaceValidation = True
                print("")
                if playing == True:
                    printBoard()

        # Horizontal Computer Win
        for row in range(rows):
            staticColumn = 0
            if board[row][staticColumn] == "O" and board[row][staticColumn + 1] == "O" and board[row][staticColumn + 2] == "O":
                playing = False
                print("\nGame Over! You Lose!\n")
                printBoard()

        # Vertical Computer Win
        for column in range(columns):
            staticRow = 0
            if board[staticRow][column] == "O" and board[staticRow + 1][column] == "O" and board[staticRow + 2][column] == "O":
                playing = False
                print("\nGame Over! You Lose!\n")
                printBoard()

        # Diagonal Computer Win
        computerCount1 = 0
        computerCount2 = 0
        for row in range(rows):
            if board[row][row] == "O":
                computerCount1 += 1
            if board[row][(rows - 1) - row] == "O":
                computerCount2 += 1
            if computerCount1 == 3 or computerCount2 == 3:
                playing == False
                print("\nGame Over! You Lose!\n")
                printBoard()

active1 = True 
while active1 == True:
    board = []
    rows = 3
    columns = 3
    for i in range(rows):
        board.append(["-"] * columns)

    intro()
    printBoard()
    game()
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