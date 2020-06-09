#Question 4

def main():
    beforeConv = input("\nEnter the String that you'd like to convert to Morse Code: ")
    afterConv = convertToMorse(beforeConv)
    print("\n",afterConv, sep = "")


def convertToMorse(value):
    result = ""
    for index in range(len(value)):
        currChar = value[index]
        if currChar == " ":
            result += " "

        elif currChar == ",":
            result += "--..--"

        elif currChar == ".":
            result += ".-.-.-"

        elif currChar == "?":
            result += "..--.."

        elif currChar == "0":
            result += "-----"

        elif currChar == "1":
            result += ".----"

        elif currChar == "2":
            result += "..---"

        elif currChar == "3":
            result += "...--"

        elif currChar == "4":
            result += "....-"

        elif currChar == "5":
            result += "...."

        elif currChar == "6":
            result += "-...."

        elif currChar == "7":
            result += "--..."

        elif currChar == "8":
            result += "---.."

        elif currChar == "9":
            result += "----."

        elif currChar.upper() == "A":
            result += ".-"

        elif currChar.upper() == "B":
            result += "-..."

        elif currChar.upper() == "C":
            result += "-.-."

        elif currChar.upper() == "D":
            result += "-.."

        elif currChar.upper() == "E":
            result += "."

        elif currChar.upper() == "F":
            result += "..-."

        elif currChar.upper() == "G":
            result += "--."

        elif currChar.upper() == "H":
            result += "...."

        elif currChar.upper() == "I":
            result += ".."

        elif currChar.upper() == "J":
            result += ".---"

        elif currChar.upper() == "K":
            result += "-.-"

        elif currChar.upper() == "L":
            result += ".-.."

        elif currChar.upper() == "M":
            result += "--"

        elif currChar.upper() == "N":
            result += "-."

        elif currChar.upper() == "O":
            result += "---"

        elif currChar.upper() == "P":
            result += ".--."

        elif currChar.upper() == "Q":
            result += "--.-"

        elif currChar.upper() == "R":
            result += ".-."

        elif currChar.upper() == "S":
            result += "..."

        elif currChar.upper() == "T":
            result += "-"

        elif currChar.upper() == "U":
            result += "..-"

        elif currChar.upper() == "V":
            result += "...-"

        elif currChar.upper() == "W":
            result += ".--"

        elif currChar.upper() == "X":
            result += "-..-"

        elif currChar.upper() == "Y":
            result += "-.-"

        elif currChar.upper() == "Z":
            result += "--.."

    return result

main()
