#Question 5

def main():
    alphaTele = input("Enter a telephone number in the format 'XXX-XXX-XXXX': ")
    numTele = getNumericTelephone(alphaTele)

    print("\nThe telephone number is:", numTele)

def getNumericTelephone(alphaTele):
    result = ""
    for index in range(len(alphaTele)):
        currChar = alphaTele[index]

        if currChar.upper() == "A" or currChar.upper() == "B" or currChar.upper() == "C":
            result += str(2)

        elif currChar.upper() == "D" or currChar.upper() == "E" or currChar.upper() == "F":
            result += str(3)

        elif currChar.upper() == "G" or currChar.upper() == "H" or currChar.upper() == "I":
            result += str(4)

        elif currChar.upper() == "J" or currChar.upper() == "K" or currChar.upper() == "L":
            result + str(5)

        elif currChar.upper() == "M" or currChar.upper() == "N" or currChar.upper() == "O":
            result += str(6)

        elif currChar.upper() == "P" or currChar.upper() == "Q" or currChar.upper() == "R" or currChar.upper() == "S":
            result += str(7)

        elif currChar.upper() == "T" or currChar.upper() == "U" or currChar.upper() == "V":
            result += str(8)

        elif currChar.upper() == "W" or currChar.upper() == "X" or currChar.upper() == "Y" or currChar.upper() == "Z":
            result += str(9)

        else:
            result += currChar

    return result 




main()
