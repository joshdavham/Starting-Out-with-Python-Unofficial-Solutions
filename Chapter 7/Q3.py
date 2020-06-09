#Question 3

def main():
    fileName = input("What is the file's name? ")
    inFile = open(fileName, "r")

    line = inFile.readline().rstrip("\n")
    lineNum = 1
    while line != "":
        print(lineNum, ": ", line, sep = "")
        line = inFile.readline().rstrip("\n")
        lineNum += 1

    inFile.close()



main()
