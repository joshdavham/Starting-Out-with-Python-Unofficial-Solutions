#Question 8

def main():

    print("You are about to be asked to enter individual numbers to sum,", \
          "\nPress enter after every number has been typed then enter a negative number when you are done")

    num = float(input("\nEnter number 1: "))
    total = 0
    while num >= 0:
        total += num
        num = float(input("Enter the next number: "))

    print("\nThe sum of the numbers is", total)

main()
