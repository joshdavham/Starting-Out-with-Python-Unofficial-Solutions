#Question 2

#No exception catchers are included in this example
#so if the file does not exist the program will crash
def main():
    fileName = input("What is the file's name? ")
    inFile = open(fileName, "r")

    line = inFile.readline().rstrip("\n")
    lineCount = 0
    while line != "" and lineCount < 5:
        print(line)
        line = inFile.readline().rstrip("\n")
        lineCount += 1

    inFile.close()


main()
