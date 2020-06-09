#Question 8

def main():
    classA = int(input("How many Class A seats were sold? "))
    classB = int(input("How many Class B seats were sold? "))
    classC = int(input("How many Class C seats were sold? "))

    print() #clear a line
    calcIncome(classA, classB, classC)

def calcIncome(classA, classB, classC):
    income = (15 * classA) + (12 * classB) + (9 * classC)

    print("Total ticket income: $", format(income, '.2f'), sep = "")

main()
