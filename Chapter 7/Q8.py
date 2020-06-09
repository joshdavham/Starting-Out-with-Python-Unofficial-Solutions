#Question 8

def main():
    inFile = open("numbers.txt", "r")

    line = inFile.readline()
    total = 0
    numCount = 0
    while line != "":
        num = int(line)
        total += num
        numCount += 1
        line = inFile.readline()

    inFile.close()

    print("Total:", total, \
          "Number of random numbers:", numCount)


main()
