#Question 3

#Global(heh) Constant 
GRAVITY = 9.8 #Acceleration of objects due to gravity when near the surface of the earth.

def main():
    mass = float(input("Please enter the mass of the object: "))

    weight = mass * GRAVITY

    processWeight(weight)

def processWeight(weight):
    if weight > 1000:
        print("\nThe object weighs:", weight, "newtons, which is over 1000 newtons.", \
              "\nIt is too heavy!")

    elif weight < 10:
        print("\nThe object weighs:", weight, "newtons which is under 10 newtons." \
              "\nIt is too light!")

    else: # 10 <= weight <= 1000
        print("\nThe object weighs:", weight, "newtons.", \
             "\nJust right!")

main()
