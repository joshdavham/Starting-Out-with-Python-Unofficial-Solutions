#Question 4

def main():

    wordSet = set()

    inFile = open("Q4input.txt", "r")

    line = inFile.readline()

    while line != "":
        words = line.split()
        wordSet.update(words)
        line = inFile.readline()

    inFile.close()
    print("\nList of unique words in the file:", \
          "\n", wordSet, sep="")



main()
