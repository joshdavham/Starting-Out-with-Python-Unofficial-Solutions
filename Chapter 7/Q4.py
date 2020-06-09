#Question 4

def main():
    inFile = open("names.txt", "r")

    line = inFile.readline()
    lineCount = 0
    while line != "":
        lineCount += 1
        line = inFile.readline()

    inFile.close()

    print("There are", lineCount, "names stored in names.txt.")


main()
