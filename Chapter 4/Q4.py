#Question 4

def main():
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the last two digits of the current year: "))

    #We figure out whether the date is magic.
    isMagic(day, month, year)

def isMagic(day, month, year):
    if day * month == year:
        print("\nThe date is magic!")
    else:
        print("\nThe date is not magic :(")

main()
