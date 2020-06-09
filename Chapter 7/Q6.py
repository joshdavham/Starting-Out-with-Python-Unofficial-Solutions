#Question 6

def main():
    inFile = open("numbers.txt", "r")

    line = inFile.readline()
    total = 0
    numCount = 0 #The amount of numbers in the file
    while line != "":
        numCount += 1
        num = float(line)
        total += num
        line = inFile.readline()

    inFile.close()

    avg = total / numCount

    print("The average is:", avg)


main()
