#Question 5

#Our global constants
ASSESSMENT_PERCENT = 0.6 #60%
PROPERTY_TAX = 0.0064 #0.64% - Charged on Assessment

def main():
    price = float(input("How much is your property worth? "))

    print() #Clear a line
    calculate(price)

def calculate(price):
    assessment = price * ASSESSMENT_PERCENT
    tax = assessment * PROPERTY_TAX

    print("Your assessment is: $", format(assessment, '.2f'), \
          "\nYour property tax is: $", format(tax, '.2f'), sep = "")

main()
