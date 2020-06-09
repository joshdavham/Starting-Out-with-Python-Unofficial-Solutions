#Question 4

class Employee:

    def __init__(self, name, IDNum, dept, job):
        self.__name = name
        self.__IDNum = IDNum
        self.__dept = dept
        self.__job = job

    def __str__(self):
        return self.__name + "\t" + self.__IDNum + "\t" + self.__dept + "\t" + self.__job





def main():
    emp1 = Employee("Susan Meyers","47899","Accounting","Vice President")
    emp2 = Employee("Mark Jones","39119","IT       ","Programmer")#Weird spacing to get proper alignment
    emp3 = Employee("Joy Rogers","81774","Manufacturing","Engineer")

    print("Name \tID Number \tDepartment \tJob Title", \
          "\n---------------------------------------------------"
          "\n", emp1, \
          "\n", emp2, \
          "\n", emp3, sep="")


main()
