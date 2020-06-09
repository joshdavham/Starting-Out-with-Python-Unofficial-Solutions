#Question 9

#Global constants
PAINT_PER_AREA = 1 / 115 #1 gallon of paint per 115ft^2
TIME_PER_AREA = 8 / 115 #8hrs per 115ft^2
PRICE_PER_HOUR = 20 #$20 per hour of work


#Global variables - despite our textbook warning against it >:)
#All initialized to 0
paint = 0 #Gallons of paint required
time = 0 #The hours of labour required
paintCost = 0 #The total cost of paint
labour = 0 #The cost of labour
cost = 0 #The total cost of the job

def main():
    wallSpace = float(input("How much wall space must be painted? (in square feet) "))
    pricePerPaint = float(input("How much is each gallon of paint? "))

    calcPaint(wallSpace)
    calcTime(wallSpace)
    calcPaintCost(pricePerPaint)
    calcLabour()
    calcCost()
    printSummary()

def calcPaint(wallSpace):
    global paint
    paint = int((wallSpace * PAINT_PER_AREA) + 1) #'+1' to round up.

def calcTime(wallSpace):
    global time
    time = int((wallSpace * TIME_PER_AREA) + 1) #We also round up the amount of hours worked

def calcPaintCost(pricePerPaint):
        global paintCost
        paintCost = paint * pricePerPaint

def calcLabour():
    global labour
    labour = time * PRICE_PER_HOUR

def calcCost():
    global cost
    cost = labour + paintCost

def printSummary():
    print("\n", paint, " gallons of paint are required." \
          "\nThe job will take ", time, " hours." \
          "\nThe cost of paint: $", format(paintCost, '.2f'), "." \
          "\nThe cost for labour: $", format(labour, '.2f'), "." \
          "\nTotal cost: $", format(cost, '.2f'), sep = "")

#We call our main() function
main()
