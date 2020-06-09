#Question 3

def main():

    codes = {"A":"!", "B":"@", "C":"#", "D":"$", "E":"%", "F":"^", "G":"&", "H":"*", \
            "I":"(", "J":")", "K":"_", "L":"+", "M":"1", "N":"2", "O":"3", "P":"4", \
            "Q":"5", "R":"6", "S":"7", "T":"8", "U":"9", "V":"`", "W":"~", "X":",", \
            "Y":".", "Z":"/", " ":" "}

    inFile = open("Q3input.txt", "r")
    outFile = open("Q3output.txt", "w")

    line = inFile.readline()
    while line != "":

        for index in range(len(line)):
            char = line[index].upper()
            if char in codes:
                outFile.write(str(codes[char]))

        outFile.write("\n")


        line = inFile.readline()

    inFile.close()
    outFile.close()


main()
