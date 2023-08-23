import random

def title():
    print("-----Rock Paper Scissors-----")
    print("Choose Rock Paper or Scissors against the computer. Best of 3. \n")
    print("\t ----GUIDE---- \n \t ROCK > SCISSORS \n \t PAPER > SCISSORS \n \t SCISSORS > PAPER \n")

def game():
    choices = ["rock", "paper", "scissors"]
    wins = 0
    losses = 0
    
    while wins < 2 and losses < 2:
        computerChoice = random.choice(choices).lower()
        validation = False
        while validation == False:
            pick = input("Rock, Paper, or Scissors? ").lower()
            if pick not in choices:
                print("That is not a valid option. Try again \n")
            else:
                validation = True

        print("\n-------------------------------")
        print("\nCOMPUTER: " + str(computerChoice))
        print("YOU: " + str(pick) + "\n")
        
        if pick == "rock":
            if computerChoice == "rock":
                print("Tie Game. Go Again.")
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "paper":
                print("You lose this round \n")
                losses += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "scissors":
                print("You win this round \n")
                wins += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")

        elif pick == "paper":
            if computerChoice == "paper":
                print("Tie Game. Go Again.")
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "scissors":
                print("You lose this round \n")
                losses += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "rock":
                print("You win this round \n")
                wins += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")

        if pick == "scissors":
            if computerChoice == "scissors":
                print("Tie Game. Go Again.")
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "rock":
                print("You lose this round \n")
                losses += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")
            elif computerChoice == "paper":
                print("You win this round \n")
                wins += 1
                print("\t--SCOREBOARD-- \n\tCOMPUTER: " + str(losses) + "\n\tYOU: " + str(wins) + "\n")

    if wins == 2:
        print("\nCONGRATS! YOU WIN! \n")  
    elif losses == 2:
        print("GAME OVER \n")

playing1 = True
while playing1 == True:
    title()
    game()
    playing2 = True
    while playing2 == True:
        playChoice = input("Would you like to play again? (yes/no): ").lower()
        if playChoice == "yes":
            playing2 = False
        elif playChoice == "no":
            print("Goodbye")
            playing2 = False
            playing1 = False
        else:
            print("That is not a valid input")