#Question 5

class RetailItem:

    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def __str__(self):
        return self.__description + "\t" + str(self.__units) + "\t\t$" + format(self.__price, '.2f')


def main():
    item1 = RetailItem("Jacket",12,59.95)
    item2 = RetailItem("Designer Jeans",40,34.95)
    item3 = RetailItem("Shirt",20,24.95)

    #Warning: The alignment is totally off
    print("\tDescription \tUnits in Inventory \tPrice", \
          "\n---------------------------------------------------------", \
          "\nItem #1   ", item1, \
          "\nItem #2   ", item2, \
          "\nItem #3   ", item3, sep="")


main()
