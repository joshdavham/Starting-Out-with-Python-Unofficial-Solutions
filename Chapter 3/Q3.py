#Question 3

def main():
    repCost = float(input("How much is the cost of replacement? "))
    calcInsurCost(repCost)

#Takes in the cost of replacement for a building and prints the
#recommended amount of insurance to buy
def calcInsurCost(repCost):
    insurPerc = 0.8 #The percent that the user should invest in insurance
    insurance = insurPerc * repCost

    #Print the results
    print("\nIt is recommended that you invest $", format(insurance, '.2f'), \
          " on insurance.", sep = "")

#Call the main function
main()
