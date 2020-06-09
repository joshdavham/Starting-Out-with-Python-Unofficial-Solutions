#Question 1

class Employee:

    def __init__(self, name, num):
        self.__name = name
        self.__num = num

    def getName(self):
        return self.__name

    def getNum(self):
        return self.__num


class ProductionWorker(Employee):

    def __init__(self, name, num, shift, payRate):
        Employee.__init__(self,name,num)
        self.__shift = shift
        self.__payRate = payRate

    def getShift(self):
        return self.__shift

    def getPayRate(self):
        return self.__payRate


def main():
    name = input("Enter the worker's name: ")
    num = input("Enter the worker's employee number: ")
    shift = int(input("Enter the worker's shift (1=day, 2=night): "))
    payRate = float(input("Enter the employee's payRate: "))

    myWorker = ProductionWorker(name,num,shift,payRate)

    print("\nProduction Worker info:", \
          "\n-----------------------", \
          "\nName: ", myWorker.getName(), \
          "\nEmployee #: ", myWorker.getNum(), \
          "\nShift #: ", str(myWorker.getShift()), \
          "\nPayRate: $", format(myWorker.getPayRate(), '.2f'), sep="")

main()
