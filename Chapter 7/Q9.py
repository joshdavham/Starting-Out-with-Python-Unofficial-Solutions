#Question 9

def main():

    try:
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

    except IOError:
        print("An error occured trying to read")
        print("the file", "nubers.txt")

    except ValueError:
        print("Non-numeric data found in the file.")

    else:
        avg = total / numCount
        print("The average is:", avg)


main()
