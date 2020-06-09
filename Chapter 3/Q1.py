#Question 1

def main():
    km = float(input("Enter a distance in 'kilometers' and" + \
                     "the program will convert it to miles."))
    kmToM(km)

def kmToM(km):
    miles = km * 0.6214
    print("\n", km, " kilometers = ", miles, " miles.", sep = "")

main()
