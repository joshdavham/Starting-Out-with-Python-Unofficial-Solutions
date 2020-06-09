#Question 1

def main():

    inFile = open("numbers.txt", "r")

    line = inFile.readline()
    while line != "":
        num = int(line)
        print(num)
        line = inFile.readline()

    inFile.close()


main()
