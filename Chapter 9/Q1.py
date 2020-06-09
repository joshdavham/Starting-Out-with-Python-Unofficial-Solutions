#Question 1

def main():
    name = input("Enter your full name: ")
    nameList = name.split()
    firstInitial = nameList[0][0].upper()
    middleInitial = nameList[1][0].upper()
    lastInitial = nameList[2][0].upper()

    print("Your initials:" \
          "\n" + firstInitial + ". " + middleInitial + ". " + lastInitial + ".")


main()
