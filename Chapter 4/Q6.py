#Question 6

#Global constants
DOLLAR = 1.00
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

def main():
    print("Welcome to the dollar game!", \
         "\nIf the total sum of money entered equals a dollar then you win!")

    pennies = int(input("\nHow many pennies? "))

    nickels = int(input("\nHow many nickels? "))

    dimes = int(input("\nHow many dimes? "))

    quarters = int(input("\nHow many quarters? "))

    #We check whether the total sums to a dollar or not
    isDollar(pennies, nickels, dimes, quarters)

def isDollar(pennies, nickels, dimes, quarters):

    total = (pennies * PENNY) + (nickels * NICKEL) + (dimes * DIME) + (quarters * QUARTER)

    if total == DOLLAR:
        print("\nYou win!")
    else:
        print("\nYou lose...")

main()
