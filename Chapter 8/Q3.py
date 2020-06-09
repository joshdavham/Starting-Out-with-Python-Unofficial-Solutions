#Question 3

YEAR = 12 #Number of months in a year

def main():
    rain = get_input()
    total = get_total(rain)
    avg = get_avg(rain)
    lowestMonth = get_lowest(rain)
    highestMonth = get_highest(rain)

    print("\nTotal rainfall for the year: ", total, \
          "\nAverage monthly rainfall: ", avg, \
          "\nLeast rainy month: Month #", lowestMonth, \
          "\nMost rainy month: Month #", highestMonth, sep = "")

def get_input():
    rain = [0] * 12
    for month in range(YEAR):
        rain[month] = float(input("How much rainfall in month " + str(month+1) + ": "))

    return rain

def get_total(rain):
    total = 0
    for month in range(YEAR):
        total += rain[month]

    return total

def get_avg(rain):
    total = 0
    for month in range(YEAR):
        total += rain[month]

    avg = total / len(rain)

    return avg

def get_highest(rain):
    highest = max(rain)
    highestMonth = rain.index(highest) + 1
    return highestMonth

def get_lowest(rain):
    lowest = min(rain)
    lowestMonth = rain.index(lowest) + 1
    return lowestMonth


main()
