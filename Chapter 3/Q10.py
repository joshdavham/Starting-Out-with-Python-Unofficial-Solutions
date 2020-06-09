#Question 10

#Global constants
STATE_TAX = 0.04 #4% tax
COUNTY_TAX = 0.02 #2% tax

def main():
    sales = float(input("Enter the total monthly sales. "))

    calculate(sales)

def calculate(sales):
    amountStateTax = sales * STATE_TAX
    amountCountyTax = sales * COUNTY_TAX
    totalTax = amountCountyTax + amountStateTax

    print("\nCounty sales tax: $", format(amountCountyTax, '.2f'), \
          "\nState sales tax: $", format(amountStateTax, '.2f'), \
          "\nTotal sales tax: $", format(totalTax, '.2f'), sep = "")

main()
