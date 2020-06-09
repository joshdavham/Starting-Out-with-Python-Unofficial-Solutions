#Question 8

#Global constants
PRICE = 99 #The price of each package.

def main():
    packages = int(input("How many packages are you purchasing? "))

    getDiscount(packages)

def getDiscount(packages):

    if packages < 10:
        percentOff = 0 #0% off
    elif packages >= 10 and packages <= 19:
        percentOff = 0.2 #20% off
    elif packages >= 20 and packages <= 49:
        percentOff = 0.3 #30% off
    elif packages >= 50 and packages <= 99:
        percentOff = 0.4 #40% off
    else: #packages >= 100
        percentOff = 0.5 #50% off

    discount = packages * PRICE * percentOff

    total = (packages * PRICE) - discount

    print("\nYou qualify for a discount of $", format(discount, '.2f'), \
          "\nTotal for purchase (after discount): $", format(total, '.2f'), sep = "")

main()
