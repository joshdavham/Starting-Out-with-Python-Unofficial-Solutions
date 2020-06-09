#Question 6

def main():
    weight = float(input("How much do you weigh in pounds? "))
    height = float(input("What is you height in inches? "))

    print() # clear a line.
    calcBMI(weight, height)

def calcBMI(weight, height):
    BMI = weight * 703 / (height ** 2)

    print("Your BMI is:", BMI, "(lbs * inches^-2)")


main()
