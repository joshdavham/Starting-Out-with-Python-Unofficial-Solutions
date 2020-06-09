#Question 3

class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def __str__(self):
        return "Name: " + self.__name + ", Address: " + self.__address + ", Phone: " + self.__phone




class Customer(Person):

    def __init__(self, name, address, phone, custNum, mail):
        Person.__init__(self,name,address,phone)
        self.__custNum = custNum
        self.__mail = mail


    def __str__(self):
        return Person.__str__(self) + ", Customer Number: " + self.__custNum + ", Mailing List: " + str(self.__mail)


def main():

    name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    phone = input("Enter the customer's phone number: ")
    custNum = input("Enter the customer's customer number: ")
    mail = input("Is this customer on the mailing list? Enter True for 'yes' or False for 'no': ")
    if mail.lower() == "true":
        mail = True
    else:
        mail = False

    myCust = Customer(name,address,phone,custNum,mail)

    print("\nMy customer info:" + \
          "\n-----------------" + \
          "\n" + str(myCust))


main()
