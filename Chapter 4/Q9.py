#Question 9

def main():

    weight = float(input("Enter the weight of you package: "))

    getRate(weight)

def getRate(weight):

    if weight <= 2:
        rate = 1.10
    elif weight > 2 and weight <= 6:
        rate = 2.20
    elif weight > 6 and weight <= 10:
        rate = 3.70
    else: #weight > 10
        rate = 3.80

    charges = rate * weight

    print("\nYour charge for shipping is $", format(charges, '.2f'), ".", sep = "")

main()
