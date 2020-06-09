#Question 3

class Information:

    #Constructor
    def __init__(self, name, address, age, phoneNumber):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phoneNumber = phoneNumber

    #Setters
    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setAge(self, age):
        self.__age = age

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    #Getters
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getPhoneNumber(self):
        return self.__phoneNumber

    def __str__(self):
       return "Name: " + self.__name + ", Address: " + self.__address + ", Age: " + str(self.__age) + ", Phone Number: " + self.__phoneNumber



def main():
    myInfo = Information("Josh","123 Generic St.","20","555-123-4567")
    myFriend = Information("Hardip","456 Ordinary Ave.","19","555-890-1234")
    myFamily = Information("Barbara","789 Usual Ln.","50","555-567-8901")

    print("\nMy Information:", \
          "\n---------------")
    print(myInfo)

    print("\nFriend Information:", \
          "\n---------------")
    print(myFriend)

    print("\nFamily Information:", \
          "\n---------------")
    print(myFamily)


main()
