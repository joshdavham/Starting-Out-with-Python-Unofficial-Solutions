import random
#Question 12

def main():
    print("Rock, Paper, Scissors", \
        "\n---------------------\n")

    keepPlaying = True

    while keepPlaying:

        randNum = random.randint(1,3)

        if randNum == 1:
            computerChoice = "rock"
        elif randNum == 2:
            computerChoice = "paper"
        else:
            computerChoice = "scissors"

        userChoice = input("rock, paper, or scissors? ")
        print("The computer chose:", computerChoice)


        if userChoice == "rock" and computerChoice == "scissors":

            print("You win!")
            keepPlaying = False

        elif userChoice == "rock" and computerChoice == "paper":

            print("You lose...")
            keepPlaying = False

        elif userChoice == "paper" and computerChoice == "rock":

            print("You win!")
            keepPlaying = False

        elif userChoice == "paper" and computerChoice == "scissors":

            print("You lose...")
            keepPlaying = False

        elif userChoice == "scissors" and computerChoice == "rock":

            print("You lose...")
            keepPlaying = False

        elif userChoice == "scissors" and computerChoice == "paper":

            print("You win!")
            keepPlaying = False

        else:

            print("Tie! ===> Keep playing.\n")



main()
