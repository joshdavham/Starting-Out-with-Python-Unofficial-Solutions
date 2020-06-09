#Question 3

class Employee:

    def __init__(self, name, num):
        self.__name = name
        self.__num = num

    def getName(self):
        return self.__name

    def getNum(self):
        return self.__num


class ShiftSupervisor(Employee):

    def __init__(self, name, num, salary, bonus):

        Employee.__init__(self,name,num)
        self.__salary = salary
        self.__bonus = bonus

    def getSalary(self):
        return self.__salary

    def getBonus(self):
        return self.__bonus


def main():
    name = input("Enter the supervisor's name: ")
    num = input("Enter the supervisor's employee #: ")
    salary = float(input("Enter the supervisor's annual salary: "))
    bonus = float((input("Enter the supervisor's bonus: ")))

    mySupervisor = ShiftSupervisor(name,num,salary,bonus)

    print("\nSupervisor info:" + \
          "\n----------------" + \
          "\nName: " + mySupervisor.getName() + \
          "\nEmployee #: " + mySupervisor.getNum() + \
          "\nSalary: $" + format(mySupervisor.getSalary(), ',.2f') + \
          "\nBonus: $" + format(mySupervisor.getBonus(), ',.2f'))


main()
