#Question 7

def main():
    books = int(input("How many books have you purchased this month? "))

    awardPoints(books)

def awardPoints(books):

    if books == 0:
        print("\nYou have been awarded 0 points.")
    elif books == 1:
        print("\nYou have been awarded 5 points.")
    elif books == 2:
        print("\nYou have been awarded 15 points.")
    elif books == 3:
        print("\nYou have been awarded 30 points.")
    elif books >= 4:
        print("\nYou have been awarded 60 points.")

main()
