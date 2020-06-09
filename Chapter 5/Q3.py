#Question 3

def main():
    budget = float(input("What was you monthly budget? "))

    #Initialize at 0
    monthlyExpenses = 0
    print("\nYou may begin entering each of your expenses for the month,", \
          "\nPress enter after every entry and enter 0 when you are finished.")

    keepGoing = True
    while keepGoing:
        expense = float(input("\nEnter an expense: "))
        monthlyExpenses += expense

        if expense == 0:
            keepGoing = False

    if monthlyExpenses > budget:
        difference = monthlyExpenses - budget
        print("\nYou are over budget by $", format(difference, '.2f'), ".", sep = "")

    elif monthlyExpenses < budget:
        difference = budget - monthlyExpenses
        print("\nYou've saved $", format(difference, '.2f'), " this month.", sep = "")

    else: #monthlyExpenses == budget
        print("\nYou've spent exactly you budget this month!")

main()
