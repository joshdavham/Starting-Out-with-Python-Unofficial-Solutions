#Question 10

#Global constants
BMI_CONSTANT = 703

def main():
    weight = float(input("Enter you weight in pounds: "))
    height = float(input("Enter you height in inches: "))

    getBMI(weight, height)

def getBMI(weight, height):

    BMI = weight * BMI_CONSTANT / (height ** 2)

    if BMI < 18.5:
        print("\nYou are underweight - go eat a burger!")
    elif BMI >= 18.5 and BMI <= 25:
        print("\nYour weight is optimal - keep it up!")
    else: #BMI > 25
        print("\nYou are overweight - go for a run!")

main()
