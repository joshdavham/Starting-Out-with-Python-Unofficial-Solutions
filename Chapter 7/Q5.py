#Question 5

def main():
    inFile = open("numbers.txt", "r")

    line = inFile.readline()
    total = 0
    while line != "":
        num = float(line)
        total += num
        line = inFile.readline()

    inFile.close()

    print("The total is:", total)


main()
