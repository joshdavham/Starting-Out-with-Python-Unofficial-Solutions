#Question 4

def main():
    loan = float(input("How much is your monthly loan? "))
    insurance = float(input("How much is your monthly insurance? "))
    gas = float(input("How much do you spend on gas in a month? "))
    oil = float(input("How much do you spend on oil in a month? "))
    tires = float(input("How much money do you spend on tires in a month? "))
    maintenance = float(input("How much is monthly maintenance? "))

    print()#Clear a line.
    calcMonthlyCost(loan, insurance, gas, oil, tires, maintenance)
    calcYearlyCost(loan, insurance, gas, oil, tires, maintenance)

def calcMonthlyCost(loan, insurance, gas, oil, tires, maintenance):
    monthlyCost = loan + insurance + gas + oil + tires + maintenance
    print("Your total monthly cost is: $", format(monthlyCost, '.2f'), ".", sep = "")

def calcYearlyCost(loan, insurance, gas, oil, tires, maintenance):
    yearlyCost = 12 * (loan + insurance + gas + oil + tires + maintenance)
    print("Your total monthly cost is: $", format(yearlyCost, '.2f'), ".", sep = "")

main()
