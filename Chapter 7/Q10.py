#Question 10

def main():
    write_to_file()
    read_from_file()


def write_to_file():

    outFile = open("golf.txt", "w")

    keepWriting = True
    playerNum = 1
    while keepWriting:
        playerName = input("\nEnter name of player #" + str(playerNum) + ": ")
        playerNum += 1
        golfScore = float(input("Enter " + playerName + "'s score: "))

        outFile.write(playerName + "\n")
        outFile.write(str(golfScore) + "\n")

        print("\nKeep writing?")
        userInput = input("y = 'yes', anything else = 'no': ")
        if userInput != "y" and userInput != "Y":
            keepWriting = False

    outFile.close()

def read_from_file():
    inFile = open("golf.txt", "r")

    print("\nThe Records:" \
          "\n------------")

    name = inFile.readline().rstrip("\n")
    while name != "":
        score = inFile.readline()
        print(name, ":", score)
        name = inFile.readline().rstrip("\n")


main()
