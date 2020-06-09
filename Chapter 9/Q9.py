#Question 9

def main():
        string = input("Enter a string: ")

        numCons = getConsonantCount(string)
        numVows = getVowelCount(string)

        print("\nYour string had", numCons, "consonants and", numVows, "vowels.")



def getConsonantCount(string):
    numCons = 0
    for index in range(len(string)):
        currChar = string[index].lower()

        if currChar == "b" or currChar == "c" or currChar == "d" or currChar == "f" or currChar == "g" or currChar == "h" \
        or currChar == "j" or currChar == "k" or currChar == "l" or currChar == "m" or currChar == "n" or currChar == "p" \
        or currChar == "q" or currChar == "r" or currChar == "s" or currChar == "t" or currChar == "v" or currChar == "w" \
        or currChar == "x" or currChar == "z":
            numCons += 1

    return numCons


def getVowelCount(string):
    numVows = 0
    for index in range(len(string)):
        currChar = string[index].lower()

        if currChar == "a" or currChar == "e" or currChar == "i" or currChar == "o" or currChar == "u" or currChar == "y":
            numVows += 1

    return numVows



main()
