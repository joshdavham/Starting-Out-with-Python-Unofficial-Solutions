#Question 2

#Our Global constants
STATE_TAX = 0.04 #4% tax
COUNTY_TAX = 0.02 #2% tax

#Our Global variables - despite our textbook warning against it >:)
#All initialized at 0
amountStateTax = 0
amountCountyTax = 0
totalTax = 0
total = 0

def main():
    amountPurchase = float(input("How much is your purchase? "))
    calcStateTax(amountPurchase)
    calcCountyTax(amountPurchase)
    calcTotalTax()
    calcTotal(amountPurchase)
    printPurchase(amountPurchase)


def calcStateTax(amountPurchase):
    global amountStateTax
    amountStateTax = STATE_TAX * amountPurchase #How much must be paid to the state


def calcCountyTax(amountPurchase):
    global amountCountyTax
    amountCountyTax = COUNTY_TAX * amountPurchase #How much must be paid to the county

def calcTotalTax():
    global totalTax
    totalTax = amountStateTax + amountCountyTax


def calcTotal(amountPurchase):
    global total
    total = amountPurchase + totalTax #How much the customer must pay

def printPurchase(amountPurchase):
    print("Amount purchased: $", format(amountPurchase, '.2f'), \
      "\nState-Tax: $", format(amountStateTax, '.2f'), \
      "\nCounty-Tax: $", format(amountCountyTax, '.2f'), \
      "\nTotal Tax: $", format(totalTax, '.2f'), \
      "\nTotal: $", format(total, '.2f'), sep = "")

main() #We call our main function
