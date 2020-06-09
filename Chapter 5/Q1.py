#Question 1

def main():
    totalBugs = 0

    for day in range(1,8):
        bugs = int(input("How many bugs did you catch on day " + str(day) + "? "))
        totalBugs += bugs

        #Eats a line
        print()

    print("You have collected", totalBugs, "bugs this week.")

main()
