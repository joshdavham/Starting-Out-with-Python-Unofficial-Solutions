#Question 7

def main():
    fat = float(input("How many grams of fat did you consume today? "))
    carbs = float(input("How many grams of carbs did you consume today? "))

    print() #Clear a line
    calcFatCal(fat)
    calcCarbCal(carbs)

def calcFatCal(fat):
    calories = 9 * fat
    print("You've consumed", calories, "from fat today.")

def calcCarbCal(carbs):
    calories = 4 * carbs
    print("You've consumed", calories, "from carbs today.")

main()
