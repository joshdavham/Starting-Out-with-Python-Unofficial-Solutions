#Question 1

def main():
    num = int(input("Please enter an integer between 1 and 10: "))

    if num < 1 or num > 10:
        print("\nError: you must enter a number between 1 and 10, you entered: ", num, ".", sep = "")

    else:
        printRomanNumeral(num)

def printRomanNumeral(num):
    if num == 1:
        print("\nI")
    elif num == 2:
        print("\nII")
    elif num == 3:
        print("\nIII")
    elif num == 4:
        print("\nIV")
    elif num == 5:
        print("\nV")
    elif num == 6:
        print("\nVI")
    elif num == 7:
        print("\nVII")
    elif num == 8:
        print("\nVIII")
    elif num == 9:
        print("\nIX")
    else:
        print("\nX")

main()
