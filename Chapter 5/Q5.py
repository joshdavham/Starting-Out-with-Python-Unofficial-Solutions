#Question 5

def main():
    totalRain = 0
    totalMonths = 0
    years = int(input("How many years? "))

    for year in range(years):
        print("\nYear " + str(year+1) + ":")
        for month in range(12):
            rain = float(input("\tHow many inches of rainfall for month: " + str(month+1) + "? "))
            totalRain += rain
            totalMonths += 1

    avgRainFall = totalRain / totalMonths

    print("\nTotal number of months:", totalMonths, \
          "\nTotal rainfall:", totalRain, "inches.", \
          "\nAverage monthly rainfall:", avgRainFall, "inches per month.")

main()
