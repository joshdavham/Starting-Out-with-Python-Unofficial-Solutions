import pickle
#Question 6

class Employee:

    def __init__(self, name, IDNum, dept, job):
        self.__name = name
        self.__IDNum = IDNum
        self.__dept = dept
        self.__job = job


    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def setIDNum(self, IDNum):
        self.__IDNum = IDNum

    def setDept(self, dept):
        self.__dept = dept

    def setJob(self, job):
        self.__job = job



    def __str__(self):
        return "Name:" + self.__name + ", ID Number:" + self.__IDNum + ", Department:" + self.__dept + ", Job:" + self.__job

#Global Varibles
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = "employeeDct"

def main():

    employeeDct = loadEmployees()

    choice = 0

    while choice != QUIT:

        choice = getMenuChoice()

        if choice == LOOK_UP:
            lookUp(employeeDct)
        elif choice == ADD:
            add(employeeDct)
        elif choice == CHANGE:
            change(employeeDct)
        elif choice == DELETE:
            delete(employeeDct)

    saveContacts(employeeDct)

def loadEmployees():

    try:#If 'employee.dat' exists
        inFile = open(FILENAME, "rb")

        employeeDct = pickle.load(inFile)

        inFile.close()

    except IOError:#If 'employee.dat' does not exist
        employeeDct = {}

    return employeeDct

def getMenuChoice():
    print()
    print("Menu")
    print("------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice

def lookUp(employeeDct):
    name = input("Enter a name: ")

    print(employeeDct.get(name, "That name is not found."))

def add(employeeDct):
    name = input("Name: ")
    IDNum = input("ID Number: ")
    dept = input("Department: ")
    job = input("Job: ")

    newEmployee = Employee(name,IDNum,dept,job)

    if name not in employeeDct:
        employeeDct[name] = newEmployee
        print("The entry has been added.")
    else:
        print("That name already exists.")

def change(employeeDct):
    name = input("Enter a name: ")

    if name in employeeDct:
        IDNum = input("Enter a new ID number: ")
        dept = input("Enter the new Department: ")
        job = input("Enter the new Job: ")

        employee = Employee(name,IDNum,dept,job)

        employeeDct[name] = employee
        print("Information updated.")
    else:
        print("That name is not found.")

def delete(employeeDct):
    name = input("Enter a name: ")

    if name in employeeDct:
        del employeeDct[name]
        print("Entry deleted.")
    else:
        print("That name is not found.")

def saveContacts(employeeDct):
    outFile = open(FILENAME, "wb")

    pickle.dump(employeeDct, outFile)

    outFile.close()

main()
