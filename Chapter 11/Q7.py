#Question 7

class RetailItem:

    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    #Added in Q7
    def getUnits(self):
        return self.__units

    #Added in Q7
    def getPrice(self):
        return self.__price

    def __str__(self):
        return "Description: " + self.__description + ", Units: " + str(self.__units) + ", Price: $" + format(self.__price, '.2f')

class CashRegister:


    def __init__(self):
        self.__items = []

    def purchase_item(self, item):
        self.__items.append(item)

    def get_total(self):

        total = 0
        if len(self.__items) > 0:

            for index in range(len(self.__items)):
                currItem = self.__items[index]
                currUnits = currItem.getUnits()
                currPrice = currItem.getPrice()
                total += currUnits * currPrice

        return total

    def show_items(self):

        if len(self.__items) > 0:
            for index in range(len(self.__items)):
                currItem = self.__items[index]
                print("Item #" + str(index+1) + ": " + str(currItem) + "\n")
        else:
            print("Your shopping cart is empty.")

    def clear(self):
        self.__items = []


def main():

    myCashRegister = CashRegister()

    choice = "y"
    while choice.lower() == "y":
        itemName = input("\nEnter the name of the item you would like to purchase: ")
        numUnits = int(input("Enter the amount of " + itemName + "'s you'd like to purchase: "))
        itemPrice = float(input("Enter the price of each unit of " + itemName + ": "))
        newItem = RetailItem(itemName,numUnits,itemPrice)
        myCashRegister.purchase_item(newItem)

        choice = input("\nEnter y to keep shopping or anything else to quit: ")

    print("\nYour shopping cart:", \
          "\n-------------------\n")
    myCashRegister.show_items()
    print("Total Price: $", format(myCashRegister.get_total(), '.2f'), \
          "\n------------")


main()
